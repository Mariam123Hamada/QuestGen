import json

from groq import Groq

from utils.config import settings
from .base_generator import BaseGenerator


class GroqGenerator(BaseGenerator):

    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )
        self.model = settings.GROQ_MODEL

    async def generate_question(
        self,
        text: str,
        difficulty: str,
        question_type: str,
        document_id: int,
    ) -> dict:

        print("GroqGenerator: Generating question...")

        prompt = f"""
        You are an AI Question Generator.

        Generate exactly ONE question.

        Text:
        {text}

        Requirements:
        - Difficulty: {difficulty}
        - Question Type: {question_type}
        - Return ONLY valid JSON.

        {{
            "question":"...",
            "choices":["...","...","...","..."],
            "answer":"..."
        }}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Return only valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
        )

        textt = response.choices[0].message.content.strip()

        if textt.startswith("```json"):
            textt = textt.replace("```json", "", 1)

        if textt.startswith("```"):
            textt = textt.replace("```", "", 1)

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