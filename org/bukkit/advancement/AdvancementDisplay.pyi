from typing import Protocol
from org.bukkit.inventory import ItemStack

class AdvancementDisplay(Protocol):
    """
    Holds information about how the advancement is displayed by the game.
    """

    def get_title(self) -> str:
        """
        Gets the title of the advancement.

        Returns:
            The advancement title without colour codes.
        """
        ...

    def get_description(self) -> str:
        """
        Gets the visible description of the advancement.

        Returns:
            The advancement description without colour codes.
        """
        ...

    def get_icon(self) -> ItemStack:
        """
        The icon that is used for this advancement.

        Returns:
            an ItemStack that represents the advancement.
        """
        ...

    def should_show_toast(self) -> bool:
        """
        Whether to show a toast to the player when this advancement has been
        completed.

        Returns:
            true if a toast is shown.
        """
        ...

    def should_announce_chat(self) -> bool:
        """
        Whether to announce in the chat when this advancement has been completed.

        Returns:
            true if announced in chat.
        """
        ...

    def is_hidden(self) -> bool:
        """
        Whether to hide this advancement and all its children from the
        advancement screen until this advancement have been completed.

        Has no effect on root advancements themselves, but still affects all
        their children.

        Returns:
            true if hidden.
        """
        ...

    def get_x(self) -> float:
        """
        The X position of the advancement in the advancement screen.

        Returns:
            the X coordinate as float
        """
        ...

    def get_y(self) -> float:
        """
        The Y position of the advancement in the advancement screen.

        Returns:
            the Y coordinate as float
        """
        ...

    def get_type(self) -> 'AdvancementDisplayType':
        """
        The display type of this advancement.

        Returns:
            an enum representing the type.
        """
        ...