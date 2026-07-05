from docx import Document
from .base_extractor import BaseExtractor


class DOCXExtractor(BaseExtractor):

    def extract_text(self, file_path: str) -> str:
        doc = Document(file_path)

        text = []

        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text)

        return "\n".join(text)