from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from typing import Optional

class PlayerSwapHandItemsEvent(PlayerEvent, Cancellable):
    """
    Called when a player swap items between main hand and off hand using the
    hotkey.
    """

    handlers: HandlerList

    def __init__(self, player: Player, main_hand_item: ItemStack, off_hand_item: ItemStack) -> None:
        """
        Initializes the PlayerSwapHandItemsEvent.

        :param player: The player involved in the event.
        :param main_hand_item: The item in the main hand.
        :param off_hand_item: The item in the off hand.
        """
        ...

    def get_main_hand_item(self) -> Optional[ItemStack]:
        """
        Gets the item switched to the main hand.

        :return: item in the main hand
        """
        ...

    def set_main_hand_item(self, main_hand_item: Optional[ItemStack]) -> None:
        """
        Sets the item in the main hand.

        :param main_hand_item: new item in the main hand
        """
        ...

    def get_off_hand_item(self) -> Optional[ItemStack]:
        """
        Gets the item switched to the off hand.

        :return: item in the off hand
        """
        ...

    def set_off_hand_item(self, off_hand_item: Optional[ItemStack]) -> None:
        """
        Sets the item in the off hand.

        :param off_hand_item: new item in the off hand
        """
        ...

    def is_cancelled(self) -> bool:
        ...
    
    def set_cancelled(self, cancel: bool) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def get_handler_list() -> HandlerList:
        ...