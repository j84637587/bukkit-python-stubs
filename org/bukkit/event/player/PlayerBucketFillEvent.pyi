from org.bukkit.Material import Material
from org.bukkit.block.Block import Block
from org.bukkit.block.BlockFace import BlockFace
from org.bukkit.entity.Player import Player
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.EquipmentSlot import EquipmentSlot
from org.bukkit.inventory.ItemStack import ItemStack
from org.jetbrains.annotations import NotNull

class PlayerBucketFillEvent(PlayerBucketEvent):
    """
    Called when a player fills a bucket
    """

    handlers: HandlerList = ...

    def __init__(self,
                 who: NotNull[Player],
                 blockClicked: NotNull[Block],
                 blockFace: NotNull[BlockFace],
                 bucket: NotNull[Material],
                 itemInHand: NotNull[ItemStack]) -> None:
        ...

    def __init__(self,
                 who: NotNull[Player],
                 block: NotNull[Block],
                 blockClicked: NotNull[Block],
                 blockFace: NotNull[BlockFace],
                 bucket: NotNull[Material],
                 itemInHand: NotNull[ItemStack]) -> None:
        ...

    def __init__(self,
                 who: NotNull[Player],
                 block: NotNull[Block],
                 blockClicked: NotNull[Block],
                 blockFace: NotNull[BlockFace],
                 bucket: NotNull[Material],
                 itemInHand: NotNull[ItemStack],
                 hand: NotNull[EquipmentSlot]) -> None:
        ...

        def getHandlers(self) -> NotNull[HandlerList]:
        ...

        @staticmethod
    def getHandlerList() -> NotNull[HandlerList]:
        ...