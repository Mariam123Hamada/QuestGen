import json

from google import genai

from utils.config import settings


class QuestionGeneratorService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_KEY
        )

        self.model = settings.GEMINI_MODEL

    async def generate_question(
        self,
        text: str,
        difficulty: str,
        question_type: str,
        document_id: int,
    ) -> dict:
        print("QuestionGeneratorService: Generating question...")
        prompt = f"""
                You are an AI Question Generator.

                Generate exactly ONE question from the following text.

                Text:
                {text}

                Requirements:
                - Difficulty: {difficulty}
                - Question Type: {question_type}
                - Generate exactly one question.
                - Generate its correct answer.
                - Return ONLY valid JSON.

                Example:

                {{
                    "question": "...",
                    "choices": ["...", "...", "...", "..."],
                    "answer": "..."
                }}
                """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        textt = response.text

        try:

            if textt.startswith("```json"):
                textt = textt.replace("```json", "", 1)

            if textt.endswith("```"):
                textt = textt[:-3]

            textt = textt.strip()

            data = json.loads(textt)

            return {
                "question": data["question"],
                "choices": data["choices"],
                "answer": data["answer"],
                "difficulty": difficulty,
                "question_type": question_type,
                "document_id": document_id,
            }

        except Exception as e:
            raise ValueError(
                f"Failed to parse Gemini response.\nResponse:\n{response.text}"
            ) from e