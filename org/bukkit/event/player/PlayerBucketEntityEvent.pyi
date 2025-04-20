from org.bukkit.Material import Material
from org.bukkit.entity.Entity import Entity
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.EquipmentSlot import EquipmentSlot
from org.bukkit.inventory.ItemStack import ItemStack
from org.jetbrains.annotations import NotNull

class PlayerBucketEntityEvent(PlayerEvent, Cancellable):
    """
    This event is called whenever a player captures an entity in a bucket.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    entity: Entity
    original_bucket: ItemStack
    entity_bucket: ItemStack
    hand: EquipmentSlot

    def __init__(self, player: Player, entity: Entity, original_bucket: ItemStack, entity_bucket: ItemStack, hand: EquipmentSlot) -> None:
        ...

        def getEntity(self) -> Entity:
        """
        Gets the {@link Entity} being put into the bucket.

        @return The {@link Entity} being put into the bucket
        """
        ...

        def getOriginalBucket(self) -> ItemStack:
        """
        Gets the bucket used to capture the {@link Entity}.

        This refers to the bucket clicked with, eg {@link Material#WATER_BUCKET}.

        @return The used bucket
        """
        ...

        def getEntityBucket(self) -> ItemStack:
        """
        Gets the bucket that the {@link Entity} will be put into.

        This refers to the bucket with the entity, eg
        {@link Material#PUFFERFISH_BUCKET}.

        @return The bucket that the {@link Entity} will be put into
        """
        ...

        def getHand(self) -> EquipmentSlot:
        """
        Get the hand that was used to bucket the entity.

        @return the hand
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