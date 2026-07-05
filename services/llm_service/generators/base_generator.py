from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    @abstractmethod
    async def generate_question(
        self,
        text: str,
        difficulty: str,
        question_type: str,
        document_id: int,
    ) -> dict:
        pass