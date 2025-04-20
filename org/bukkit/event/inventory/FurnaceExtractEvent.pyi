from org.bukkit import Bukkit
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event.block import BlockExpEvent
from org.bukkit.material import MaterialData
from typing import Optional

class FurnaceExtractEvent(BlockExpEvent):
    """
    This event is called when a player takes items out of the furnace
    """

    def __init__(self, player: Player, block: Block, item_type: Material, item_amount: int, exp: int) -> None:
        ...

    """
    Get the player that triggered the event

    @return: the relevant player
    """
    def get_player(self) -> Player:
        ...

    """
    Get the Material of the item being retrieved

    @return: the material of the item
    """
    def get_item_type(self) -> Material:
        ...

    """
    Get the item count being retrieved

    @return: the amount of the item
    """
    def get_item_amount(self) -> int:
        ...