from org.bukkit.Material import Material
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.EquipmentSlot import EquipmentSlot
from org.bukkit.inventory.ItemStack import ItemStack
from typing import Optional

class PlayerItemConsumeEvent(PlayerEvent, Cancellable):
    """
    This event will fire when a player is finishing consuming an item (food,
    potion, milk bucket).
    <br>
    If the ItemStack is modified the server will use the effects of the new
    item and not remove the original one from the player's inventory.
    <br>
    If the event is cancelled the effect will not be applied and the item will
    not be removed from the player's inventory.
    """

    handlers: HandlerList

    def __init__(self, player: Player, item: ItemStack, hand: EquipmentSlot) -> None:
        """
        :param player: the player consuming
        :param item: the ItemStack being consumed
        :param hand: the hand that was used
        """
        ...

    def __init__(self, player: Player, item: ItemStack) -> None:
        """
        :param player: the player consuming
        :param item: the ItemStack being consumed
        :deprecated: use {@link #PlayerItemConsumeEvent(Player, ItemStack, EquipmentSlot)}
        """
        ...

    def getItem(self) -> ItemStack:
        """
        Gets the item that is being consumed. Modifying the returned item will
        have no effect, you must use {@link
        #setItem(org.bukkit.inventory.ItemStack)} instead.

        :return: an ItemStack for the item being consumed
        """
        ...

    def setItem(self, item: Optional[ItemStack]) -> None:
        """
        Set the item being consumed

        :param item: the item being consumed
        """
        ...

    def getHand(self) -> EquipmentSlot:
        """
        Get the hand used to consume the item.

        :return: the hand
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...