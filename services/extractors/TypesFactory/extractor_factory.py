from .docs_extractor import DOCXExtractor
from .pdf_extractor import PDFExtractor
from .text_extractor import TXTExtractor

class ExtractorFactory:
    _extractors = {
        "pdf": PDFExtractor,
        "docx": DOCXExtractor,
        "txt": TXTExtractor, 
    }
    
    @classmethod
    def get_extractor(cls , file_type: str):
        extractor_class = cls._extractors.get(file_type.lower())
        if not extractor_class:
            raise ValueError(f"Unsupported file type: {file_type}")
        return extractor_class()