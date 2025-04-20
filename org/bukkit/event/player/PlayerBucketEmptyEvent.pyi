from org.bukkit.Material import Material
from org.bukkit.block.Block import Block
from org.bukkit.block.BlockFace import BlockFace
from org.bukkit.entity.Player import Player
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.EquipmentSlot import EquipmentSlot
from org.bukkit.inventory.ItemStack import ItemStack
from typing import Any

class PlayerBucketEmptyEvent(PlayerBucketEvent):
    """
    Called when a player empties a bucket
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, who: Player, block_clicked: Block, block_face: BlockFace, bucket: Material, item_in_hand: ItemStack) -> None:
        super().__init__(who, block_clicked, block_face, bucket, item_in_hand)

    def __init__(self, who: Player, block: Block, block_clicked: Block, block_face: BlockFace, bucket: Material, item_in_hand: ItemStack) -> None:
        super().__init__(who, block, block_clicked, block_face, bucket, item_in_hand)

    def __init__(self, who: Player, block: Block, block_clicked: Block, block_face: BlockFace, bucket: Material, item_in_hand: ItemStack, hand: EquipmentSlot) -> None:
        super().__init__(who, block, block_clicked, block_face, bucket, item_in_hand, hand)

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        return PlayerBucketEmptyEvent.handlers