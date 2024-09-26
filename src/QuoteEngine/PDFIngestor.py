"""Provides an IngestorInterface for pdf files."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Strategy object for parsing through PDF file.

    Create temporary .txt file which is subsequently read.
    """

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a boolean flagging whether the file in the path string can be read.

        params: path
        return: boolean
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        # Create temp directory
        temp_path = "./tmp/"
        if not os.path.exists(temp_path):
            os.mkdir(temp_path)

        tmp_file = f'{temp_path}/{random.randint(1000, 9999)}.txt'
        call = subprocess.call(['pdftotext', '-layout',  path, tmp_file])

        quotes = []
        infile = open(tmp_file, "r")

        for line in infile.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                print(parse)
                quotes.append(QuoteModel(parse[0], parse[1]))

        os.remove(tmp_file)
        return quotes
