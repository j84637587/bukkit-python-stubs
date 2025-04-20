from typing import Optional, Protocol
from org.bukkit import Material

"""
Represents a Material.WRITTEN_BOOK that can have a title, an author,
and pages.
"""
class BookMeta(Protocol):

    class Generation:
        """
        Represents the generation (or level of copying) of a written book
        """
        ORIGINAL = ...
        COPY_OF_ORIGINAL = ...
        COPY_OF_COPY = ...
        TATTERED = ...

    """
    Checks for the existence of a title in the book.

    @return true if the book has a title
    """
    def has_title(self) -> bool: ...

    """
    Gets the title of the book.
    <p>
    Plugins should check that hasTitle() returns true before calling this
    method.

    @return the title of the book
    """
    def get_title(self) -> Optional[str]: ...

    """
    Sets the title of the book.
    <p>
    Limited to 32 characters. Removes title when given null.

    @param title the title to set
    @return true if the title was successfully set
    """
    def set_title(self, title: Optional[str]) -> bool: ...

    """
    Checks for the existence of an author in the book.

    @return true if the book has an author
    """
    def has_author(self) -> bool: ...

    """
    Gets the author of the book.
    <p>
    Plugins should check that hasAuthor() returns true before calling this
    method.

    @return the author of the book
    """
    def get_author(self) -> Optional[str]: ...

    """
    Sets the author of the book. Removes author when given null.

    @param author the author to set
    """
    def set_author(self, author: Optional[str]) -> None: ...

    """
    Checks for the existence of generation level in the book.

    @return true if the book has a generation level
    """
    def has_generation(self) -> bool: ...

    """
    Gets the generation of the book.
    <p>
    Plugins should check that hasGeneration() returns true before calling
    this method.

    @return the generation of the book
    """
    def get_generation(self) -> Optional[Generation]: ...

    """
    Sets the generation of the book. Removes generation when given null.

    @param generation the generation to set
    """
    def set_generation(self, generation: Optional[Generation]) -> None: ...

    def clone(self) -> BookMeta: ...