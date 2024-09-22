from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TXTIngestor(IngestorInterface):

    allowed_extensions = [".txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("cannot read exception")

        quotes = []

        with open(path, "r") as infile:
            for line in infile:
                parse = line.split(' - ')
                quotes.append(QuoteModel(parse[0], parse[1]))

        return quotes
