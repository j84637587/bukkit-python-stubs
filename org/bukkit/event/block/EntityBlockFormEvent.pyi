from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.entity import Entity
from org.bukkit.event.block import BlockFormEvent
from typing import Any

class EntityBlockFormEvent(BlockFormEvent):
    """
    Called when a block is formed by entities.
    <p>
    Examples:
    <ul>
    <li>Snow formed by a {@link org.bukkit.entity.Snowman}.
    <li>Frosted Ice formed by the Frost Walker enchantment.
    </ul>
    """

    def __init__(self, entity: Entity, block: Block, blockstate: BlockState) -> None:
        """
        Initialize the event with the entity, block, and block state.

        :param entity: The entity that formed the block.
        :param block: The block that is formed.
        :param blockstate: The state of the block.
        """
        ...

    """
    Get the entity that formed the block.

    :return: Entity involved in event
    """
    def get_entity(self) -> Entity:
        ...