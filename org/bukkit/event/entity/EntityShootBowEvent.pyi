from org.bukkit.entity import Entity, LivingEntity, Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import EquipmentSlot, ItemStack
from typing import Optional

class EntityShootBowEvent(EntityEvent, Cancellable):
    """
    Called when a LivingEntity shoots a bow firing an arrow
    """

    handlers: HandlerList

    def __init__(self, shooter: LivingEntity, bow: Optional[ItemStack], consumable: Optional[ItemStack], projectile: Entity, hand: EquipmentSlot, force: float, consume_item: bool) -> None:
        ...

    def get_entity(self) -> LivingEntity:
        ...

    def get_bow(self) -> Optional[ItemStack]:
        """
        Gets the bow ItemStack used to fire the arrow.

        :return: the bow involved in this event
        """
        ...

    def get_consumable(self) -> Optional[ItemStack]:
        """
        Get the ItemStack to be consumed in this event (if any).

        For instance, bows will consume an arrow ItemStack in a player's
        inventory.

        :return: the consumable item
        """
        ...

    def get_projectile(self) -> Entity:
        """
        Gets the projectile which will be launched by this event

        :return: the launched projectile
        """
        ...

    def set_projectile(self, projectile: Entity) -> None:
        """
        Replaces the projectile which will be launched

        :param projectile: the new projectile
        """
        ...

    def get_hand(self) -> EquipmentSlot:
        """
        Get the hand from which the bow was shot.

        :return: the hand
        """
        ...

    def get_force(self) -> float:
        """
        Gets the force the arrow was launched with

        :return: bow shooting force, up to 1.0
        """
        ...

    def set_consume_item(self, consume_item: bool) -> None:
        """
        Set whether or not the consumable item should be consumed in this event.

        If set to false, it is recommended that a call to
        {@link Player#updateInventory()} is made as the client may disagree with
        the server's decision to not consume a consumable item.
        <p>
        This value is ignored for entities where items are not required
        (skeletons, pillagers, etc.) or with crossbows (as no item is being
        consumed).

        :param consume_item: whether or not to consume the item
        :deprecated: not currently functional
        """
        ...

    def should_consume_item(self) -> bool:
        """
        Get whether or not the consumable item should be consumed in this event.

        :return: true if consumed, false otherwise
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