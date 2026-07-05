from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List

class ChunkService:
    def __init__(self , chunk_size:int=500 , chunk_overlap:int=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
        )
    def split(self , text:str) -> List[str]:
        print("Spliiting Function Called.")
        return self.splitter.split_text(text)
        