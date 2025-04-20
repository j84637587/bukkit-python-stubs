from org.bukkit.block import Block
from org.bukkit.entity import LivingEntity
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any
from org.jetbrains.annotations import NotNull

class BlockDispenseArmorEvent(BlockDispenseEvent):
    """
    Called when an equippable item is dispensed from a block and equipped on a
    nearby entity.
    <p>
    If a Block Dispense Armor event is cancelled, the equipment will not be
    equipped on the target entity.
    """

    def __init__(self, block: NotNull[Block], dispensed: NotNull[ItemStack], target: NotNull[LivingEntity]) -> None:
        ...

    """
    Get the living entity on which the armor was dispensed.

    @return: the target entity
    """
        def get_target_entity(self) -> LivingEntity:
        ...