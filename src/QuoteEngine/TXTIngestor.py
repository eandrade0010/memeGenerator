"""Provides an IngestorInterface for text files."""

from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TXTIngestor(IngestorInterface):
    """Strategy object for parsing through text file.

    params: string-like path for file
    return: List of QuoteModels
    """

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a boolean flagging whether the file in the path string can be read.

        params: path
        return: boolean
        """
        if not cls.can_ingest(path):
            raise Exception("cannot read exception")

        quotes = []

        with open(path, "r") as infile:
            for line in infile:
                parse = line.split(' - ')
                quotes.append(QuoteModel(parse[0], parse[1]))

        return quotes
