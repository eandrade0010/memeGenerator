"""Provides an IngestorInterface for docx files."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Strategy object for parsing through DOCX file.

    params: string-like path for file
    return: List of QuoteModels
    """

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a boolean flagging whether the file in the path string can be read.

        params: path
        return: boolean
        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.split(" - ")
                quotes.append(QuoteModel(parse[0], parse[1]))

        return quotes
