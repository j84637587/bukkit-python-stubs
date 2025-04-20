from typing import List

class WritableBookMeta:
    """
    Represents a book (Material.WRITABLE_BOOK or Material.WRITTEN_BOOK) that can have pages.
    """

    def has_pages(self) -> bool:
        """
        Checks for the existence of pages in the book.

        :return: true if the book has pages
        """
        ...

    def get_page(self, page: int) -> str:
        """
        Gets the specified page in the book. The given page must exist.
        
        Pages are 1-indexed.

        :param page: the page number to get, in range [1, get_page_count()]
        :return: the page from the book
        """
        ...

    def set_page(self, page: int, data: str) -> None:
        """
        Sets the specified page in the book. Pages of the book must be contiguous.
        
        The data can be up to 1024 characters in length, additional characters are truncated.
        
        Pages are 1-indexed.

        :param page: the page number to set, in range [1, get_page_count()]
        :param data: the data to set for that page
        """
        ...

    def get_pages(self) -> List[str]:
        """
        Gets all the pages in the book.

        :return: list of all the pages in the book
        """
        ...

    def set_pages(self, pages: List[str]) -> None:
        """
        Clears the existing book pages, and sets the book to use the provided pages.
        Maximum 100 pages with 1024 characters per page.

        :param pages: A list of pages to set the book to use
        """
        ...

    def set_pages_varargs(self, *pages: str) -> None:
        """
        Clears the existing book pages, and sets the book to use the provided pages.
        Maximum 100 pages with 1024 characters per page.

        :param pages: A list of strings, each being a page
        """
        ...

    def add_page(self, *pages: str) -> None:
        """
        Adds new pages to the end of the book. Up to a maximum of 100 pages with
        1024 characters per page.

        :param pages: A list of strings, each being a page
        """
        ...

    def get_page_count(self) -> int:
        """
        Gets the number of pages in the book.

        :return: the number of pages in the book
        """
        ...

    def clone(self) -> 'WritableBookMeta':
        ...