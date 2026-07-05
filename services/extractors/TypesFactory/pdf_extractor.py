# from pypdf import PdfReader
# from .base_extractor import BaseExtractor


# class PDFExtractor(BaseExtractor):

#     def extract_text(self, file_path: str) -> str:

#         reader = PdfReader(file_path)

#         text = ""

#         for page in reader.pages:
#             extracted = page.extract_text()

#             if extracted:
#                 text += extracted + "\n"

#         return text
from pypdf import PdfReader
from .base_extractor import BaseExtractor


class PDFExtractor(BaseExtractor):

    def extract_text(self, file_path: str) -> str:
        reader = PdfReader(file_path)

        text = ""

        print("Pages:", len(reader.pages))

        for i, page in enumerate(reader.pages):
            extracted = page.extract_text()

            print(f"Page {i + 1}: {repr(extracted)}")

            if extracted:
                text += extracted + "\n"

        return text