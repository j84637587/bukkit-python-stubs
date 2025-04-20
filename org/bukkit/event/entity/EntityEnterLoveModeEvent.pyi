from org.bukkit.entity import Animals
from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Optional

class EntityEnterLoveModeEvent(EntityEvent, Cancellable):
    """
    Called when an entity enters love mode.
    <br>
    This can be cancelled but the item will still be consumed that was used to
    make the entity enter into love mode.
    """

    handlers: HandlerList

    def __init__(self, animal_in_love: Animals, human_entity: Optional[HumanEntity], ticks_in_love: int) -> None:
        ...

    """
    Gets the animal that is entering love mode.

    @return The animal that is entering love mode
    """
    def get_entity(self) -> Animals:
        ...

    """
    Gets the Human Entity that caused the animal to enter love mode.

    @return The Human entity that caused the animal to enter love mode, or
    null if there wasn't one.
    """
    def get_human_entity(self) -> Optional[HumanEntity]:
        ...

    """
    Gets the amount of ticks that the animal will fall in love for.

    @return The amount of ticks that the animal will fall in love for
    """
    def get_ticks_in_love(self) -> int:
        ...

    """
    Sets the amount of ticks that the animal will fall in love for.

    @param ticks_in_love The amount of ticks that the animal will fall in love
    for
    """
    def set_ticks_in_love(self, ticks_in_love: int) -> None:
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