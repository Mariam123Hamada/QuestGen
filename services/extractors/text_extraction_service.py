from pathlib import Path
from .TypesFactory.extractor_factory import ExtractorFactory


class TextExtractionService:

    def extract_text(
        self,
        file_path: str,
    ) -> str:

        extension = Path(file_path).suffix.lower().replace(".", "")

        extractor = ExtractorFactory.get_extractor(
            extension
        )

        return extractor.extract_text(file_path)