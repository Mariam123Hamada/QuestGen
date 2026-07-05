import json

from google import genai

from utils.config import settings
from .base_generator import BaseGenerator


class GeminiGenerator(BaseGenerator):

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

        prompt = f"""
        You are an AI Question Generator.

        Generate exactly ONE question.

        Text:
        {text}

        Difficulty: {difficulty}
        Question Type: {question_type}

        Return ONLY valid JSON.

        {{
            "question":"...",
            "choices":["...","...","...","..."],
            "answer":"..."
        }}
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        textt = response.text.strip()

        if textt.startswith("```json"):
            textt = textt.replace("```json", "", 1)

        if textt.endswith("```"):
            textt = textt[:-3]

        data = json.loads(textt.strip())

        return {
            "question": data["question"],
            "choices": data["choices"],
            "answer": data["answer"],
            "difficulty": difficulty,
            "question_type": question_type,
            "document_id": document_id,
        }