from org.bukkit import Bukkit
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from org.bukkit.material import MaterialData
from typing import Optional

"""
Called when a player interacts with a Bucket
"""
class PlayerBucketEvent(PlayerEvent, Cancellable):
    def __init__(self, who: Player, block: Optional[Block], block_clicked: Block, block_face: BlockFace, bucket: Material, item_in_hand: ItemStack, hand: EquipmentSlot) -> None: ...
    
    @classmethod
    def deprecated_constructor_1(cls, who: Player, block_clicked: Block, block_face: BlockFace, bucket: Material, item_in_hand: ItemStack) -> None: ...
    
    @classmethod
    def deprecated_constructor_2(cls, who: Player, block: Block, block_clicked: Block, block_face: BlockFace, bucket: Material, item_in_hand: ItemStack) -> None: ...

    """
    Returns the bucket used in this event

    @return: the used bucket
    """
    def get_bucket(self) -> Material: ...

    """
    Get the resulting item in hand after the bucket event

    @return: ItemStack hold in hand after the event.
    """
    def get_item_stack(self) -> Optional[ItemStack]: ...

    """
    Set the item in hand after the event

    @param item_stack: the new held ItemStack after the bucket event.
    """
    def set_item_stack(self, item_stack: Optional[ItemStack]) -> None: ...

    """
    Gets the block involved in this event.

    @return: The Block which block is involved in this event
    """
    def get_block(self) -> Block: ...

    """
    Return the block clicked

    @return: the clicked block
    """
    def get_block_clicked(self) -> Block: ...

    """
    Get the face on the clicked block

    @return: the clicked face
    """
    def get_block_face(self) -> BlockFace: ...

    """
    Get the hand that was used in this event.

    @return: the hand
    """
    def get_hand(self) -> EquipmentSlot: ...

    def is_cancelled(self) -> bool: ...

    def set_cancelled(self, cancel: bool) -> None: ...