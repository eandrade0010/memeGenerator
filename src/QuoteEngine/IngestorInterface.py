"""Base abstract class with parsing method."""

from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Base abstract class with methods for determining whether a file can be parsed and a method for parsing file."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Return a boolean flagging whether the file in the path string can be read.

        params: path
        return: boolean
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file in path for a quote and an author, creating a list of QuoteModels.

        params: path
        return: list of QuoteModels
        """
        pass
