from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):

    allowed_extensions = [".pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        tmp_file = f'./tmp/{random.randint(1000, 9999)}.txt'
        call = subprocess.call(['pdftotext', path, tmp_file])

        quotes = []

        with open(tmp_file, 'r') as infile:
            for line in infile:
                if len(line) > 0:
                    parse = line.split(' - ')
                    quotes.append(QuoteModel(parse[0], parse[1]))

        os.remove(tmp_file)
        return quotes





