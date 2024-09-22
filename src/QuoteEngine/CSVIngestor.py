"""Provides an IngestorInterface for CSV files."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Strategy object for parsing through CSV file."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a boolean flagging whether the file in the path string can be read.

        params: path
        return: boolean
        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            quotes.append(QuoteModel(row["body"], row["author"]))

        return quotes
