from org.bukkit.entity import ExperienceOrb
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Optional

class PlayerItemMendEvent(PlayerEvent, Cancellable):
    """
    Represents when a player has an item repaired via the Mending enchantment.
    <br>
    This event is fired directly before the {@link PlayerExpChangeEvent}, and the
    results of this event directly affect the {@link PlayerExpChangeEvent}.
    """

    handlers: HandlerList

    def __init__(self, who: Player, item: ItemStack, slot: Optional[EquipmentSlot], experienceOrb: ExperienceOrb, repairAmount: int) -> None:
        """
        Initialize the PlayerItemMendEvent.

        :param who: The player involved in the event.
        :param item: The item to be repaired.
        :param slot: The equipment slot of the item.
        :param experienceOrb: The experience orb triggering the event.
        :param repairAmount: The amount to repair the item.
        """
        ...

    @classmethod
    def deprecated_init(cls, who: Player, item: ItemStack, experienceOrb: ExperienceOrb, repairAmount: int) -> None:
        """
        Deprecated constructor for PlayerItemMendEvent.

        :param who: The player involved in the event.
        :param item: The item to be repaired.
        :param experienceOrb: The experience orb triggering the event.
        :param repairAmount: The amount to repair the item.
        """
        ...

    def getItem(self) -> ItemStack:
        """
        Get the {@link ItemStack} to be repaired.

        This is not necessarily the item the player is holding.

        :return: The item to be repaired.
        """
        ...

    def getSlot(self) -> Optional[EquipmentSlot]:
        """
        Get the {@link EquipmentSlot} in which the repaired {@link ItemStack}
        may be found.

        :return: The repaired slot.
        """
        ...

    def getExperienceOrb(self) -> ExperienceOrb:
        """
        Get the experience orb triggering the event.

        :return: The experience orb.
        """
        ...

    def getRepairAmount(self) -> int:
        """
        Get the amount the item is to be repaired.

        The default value is twice the value of the consumed experience orb
        or the remaining damage left on the item, whichever is smaller.

        :return: How much damage will be repaired by the experience orb.
        """
        ...

    def setRepairAmount(self, amount: int) -> None:
        """
        Set the amount the item will be repaired.

        Half of this value will be subtracted from the experience orb which initiated this event.

        :param amount: How much damage will be repaired on the item.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Check if the event is cancelled.

        :return: True if the event is cancelled, otherwise false.
        """
        ...

    def setCancelled(self, cancelled: bool) -> None:
        """
        Set the cancellation state of the event.

        :param cancelled: True to cancel the event, otherwise false.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Get the handler list for this event.

        :return: The handler list.
        """
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        """
        Get the static handler list for this event.

        :return: The static handler list.
        """
        ...