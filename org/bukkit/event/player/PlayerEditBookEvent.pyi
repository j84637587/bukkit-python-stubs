from org.bukkit.Bukkit import Bukkit
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.meta.BookMeta import BookMeta
from typing import Optional

class PlayerEditBookEvent(PlayerEvent, Cancellable):
    """
    Called when a player edits or signs a book and quill item. If the event is
    cancelled, no changes are made to the BookMeta
    """

    handlers: HandlerList = HandlerList()

    previousBookMeta: BookMeta
    slot: int
    newBookMeta: BookMeta
    isSigning: bool
    cancel: bool

    def __init__(self, who: Player, slot: int, previousBookMeta: BookMeta, newBookMeta: BookMeta, isSigning: bool) -> None:
        """
        Initializes the PlayerEditBookEvent.

        :param who: The player who is editing the book.
        :param slot: The inventory slot number for the book item.
        :param previousBookMeta: The previous book meta.
        :param newBookMeta: The new book meta.
        :param isSigning: Whether the book is being signed.
        :raises IllegalArgumentException: If the slot or book meta arguments are invalid.
        """
        ...

    def getPreviousBookMeta(self) -> BookMeta:
        """
        Gets the book meta currently on the book.
        Note: this is a copy of the book meta. You cannot use this object to
        change the existing book meta.

        :return: the book meta currently on the book
        """
        ...

    def getNewBookMeta(self) -> BookMeta:
        """
        Gets the book meta that the player is attempting to add to the book.
        Note: this is a copy of the proposed new book meta. Use {@link
        #setNewBookMeta(BookMeta)} to change what will actually be added to the
        book.

        :return: the book meta that the player is attempting to add
        """
        ...

    def getSlot(self) -> int:
        """
        Gets the inventory slot number for the book item that triggered this
        event.
        This is a slot number on the player's hotbar in the range 0-8, or -1 for
        off hand.

        :return: the inventory slot number that the book item occupies
        :deprecated: books may be signed from off hand
        """
        ...

    def setNewBookMeta(self, newBookMeta: BookMeta) -> None:
        """
        Sets the book meta that will actually be added to the book.

        :param newBookMeta: new book meta
        :raises IllegalArgumentException: if the new book meta is null
        """
        ...

    def isSigning(self) -> bool:
        """
        Gets whether or not the book is being signed. If a book is signed the
        Material changes from BOOK_AND_QUILL to WRITTEN_BOOK.

        :return: true if the book is being signed
        """
        ...

    def setSigning(self, signing: bool) -> None:
        """
        Sets whether or not the book is being signed. If a book is signed the
        Material changes from BOOK_AND_QUILL to WRITTEN_BOOK.

        :param signing: whether or not the book is being signed.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the handler list for this event.

        :return: the handler list
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: the handler list
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: true if the event is cancelled
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets whether the event is cancelled.

        :param cancel: true to cancel the event
        """
        ...