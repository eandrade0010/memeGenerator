"""QuoteModel object for encapsulating a quote with its author."""


class QuoteModel:
    """Class object for encapsulating a quote and its author. To be read from various types of files."""

    def __init__(self, body, author):
        """Initialize QuoteModel object from a parsed line of quotes."""
        self.body = body
        self.author = author
