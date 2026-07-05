from .groq_generator import GroqGenerator
from .gemini_generator import GeminiGenerator


class GeneratorFactory:

    _generators = {
        "groq": GroqGenerator,
        "gemini": GeminiGenerator,
    }

    @classmethod
    def get_generator(cls, provider: str):

        generator = cls._generators.get(provider.lower())

        if generator is None:
            raise ValueError(f"Unsupported provider: {provider}")

        return generator()