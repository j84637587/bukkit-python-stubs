from typing import Protocol

class Lidded(Protocol):
    """
    Interface representing a lidded block.
    """

    def open(self) -> None:
        """
        Sets the block's animated state to open and prevents it from being closed
        until close() is called.
        """
        ...

    def close(self) -> None:
        """
        Sets the block's animated state to closed even if a player is currently
        viewing this block.
        """
        ...