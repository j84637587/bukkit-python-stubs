from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockGrowEvent
from typing import Any

class BlockFormEvent(BlockGrowEvent):
    """
    Called when a block is formed or spreads based on world conditions.
    <p>
    Use {@link BlockSpreadEvent} to catch blocks that actually spread and don't
    just "randomly" form.
    <p>
    Examples:
    <ul>
    <li>Snow forming due to a snow storm.
    <li>Ice forming in a snowy Biome like Taiga or Tundra.
    <li> Obsidian / Cobblestone forming due to contact with water.
    <li> Concrete forming due to mixing of concrete powder and water.
    </ul>
    <p>
    If a Block Form event is cancelled, the block will not be formed.
    
    @see BlockSpreadEvent
    """

    handlers: HandlerList

    def __init__(self, block: Block, new_state: BlockState) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...