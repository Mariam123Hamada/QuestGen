from pathlib import Path
import os

from sqlalchemy.ext.asyncio import AsyncSession

from services.db_service.project_service import ProjectService
from services.db_service.document_service import DocumentService
from services.db_service.question_service import QuestionService
from services.db_service.answer_service import AnswerService

from services.llm_service.chunk_service import ChunkService
from services.extractors.text_extraction_service import TextExtractionService
from services.llm_service.question_generator_service import (
    QuestionGeneratorService,
)

from schema.project import ProjectCreate
from schema.document import DocumentCreate
from schema.question import QuestionCreate
from schema.answer import AnswerCreate


class UploadService:

    def __init__(
        self,
        db: AsyncSession,
        project_service: ProjectService,
        document_service: DocumentService,
        question_service: QuestionService,
        answer_service: AnswerService,
    ):
        self.db = db

        self.project_service = project_service
        self.document_service = document_service
        self.question_service = question_service
        self.answer_service = answer_service

        self.text_service = TextExtractionService()
        self.chunk_service = ChunkService()
        self.question_generator = QuestionGeneratorService()

    async def upload_file(self, file):



        upload_dir = Path("uploads")
        upload_dir.mkdir(exist_ok=True)

        file_path = upload_dir / file.filename

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())



        extracted_text = self.text_service.extract_text(
            str(file_path)
        )
        print("=" * 50)
        print("Extracted text length:", len(extracted_text))
        print(extracted_text[:300])
        print("=" * 50)


        project = await self.project_service.create_project(
            self.db,
            ProjectCreate(
                name=file.filename,
            ),
        )



        document = await self.document_service.create_document(
            self.db,
            DocumentCreate(
                file_name=file.filename,
                file_type=file.content_type,
                file_size=os.path.getsize(file_path),
                project_id=project.id,
            ),
        )

        print("The Line Befor the chunking.")
        chunks = self.chunk_service.split(extracted_text)
        print(f"Total chunks created: {len(chunks)}")  # Print the number of chunks created

  
        print("BEfor Go to loops of chunkging .")
        for chunk in chunks:
            print(f"Processing chunk: {chunk[:50]}...")  # Print the first 50 characters of the chunk
            generated_questions = await self.question_generator.generate_question(
                text=chunk ,
                difficulty="medium",
                question_type="multiple_choice",
                document_id=document.id,
            )

            # for item in generated_questions:

            #     question = await self.question_service.create_question(
            #         self.db,
            #         QuestionCreate(
            #             question=item["question"],
            #             difficulty=item["difficulty"],
            #             question_type=item["question_type"],
            #             choices=item["choices"],
            #             document_id=document.id,
            #         ),
            #     )

            #     await self.answer_service.create_answer(
            #         self.db,
            #         AnswerCreate(
            #             answer=item["answer"],
            #             question_id=question.id,
            #         ),
            #     )
            result = await self.question_generator.generate_question(
                text=chunk,
                difficulty="Easy",
                question_type="MCQ",
                document_id=document.id,
            )

            question = await self.question_service.create_question(
                self.db,
                QuestionCreate(
                    question=result["question"],
                    difficulty=result["difficulty"],
                    choices=result["choices"],
                    question_type=result["question_type"],
                    document_id=result["document_id"],
                ),
            )

            await self.answer_service.create_answer(
                self.db,
                AnswerCreate(
                    answer=result["answer"],
                    question_id=question.id,
                ),
            )

        return {
            "message": "File uploaded successfully.",
            "project_id": project.id,
            "document_id": document.id,
        }