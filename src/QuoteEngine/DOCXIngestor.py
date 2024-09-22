from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.split(" - ")
                quotes.append(QuoteModel(parse[0], parse[1]))

        return quotes
