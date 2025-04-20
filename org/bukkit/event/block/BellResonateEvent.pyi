from typing import List
from org.bukkit.block import Block
from org.bukkit.entity import LivingEntity
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Any

class BellResonateEvent(BlockEvent):
    """
    Called when a bell resonated after being rung and highlights nearby raiders.
    A bell will only resonate if raiders are in the vicinity of the bell.
    """

    handlers: HandlerList = HandlerList()
    resonatedEntities: List[LivingEntity]

    def __init__(self, theBlock: Block, resonatedEntities: List[LivingEntity]) -> None:
        super().__init__(theBlock)
        self.resonatedEntities = resonatedEntities

    """
    Get a mutable list of all {@link LivingEntity LivingEntities} to be
    highlighted by the bell's resonating. This list can be added to or
    removed from to change which entities are highlighted, and may be empty
    if no entities were resonated as a result of this event.
    <p>
    While the highlighted entities will change, the particles that display
    over a resonated entity and their colors will not. This is handled by the
    client and cannot be controlled by the server.

    @return a list of resonated entities
    """
    def get_resonated_entities(self) -> List[LivingEntity]:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...