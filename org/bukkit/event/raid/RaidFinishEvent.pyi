from typing import List
from org.bukkit import Raid, World
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.jetbrains.annotations import NotNull

class RaidFinishEvent(RaidEvent):
    """
    This event is called when a {@link Raid} was complete with a clear result.
    """

    handlers: HandlerList = HandlerList()
    winners: List[Player]

    def __init__(self, raid: NotNull[Raid], world: NotNull[World], winners: NotNull[List[Player]]) -> None:
        ...

    """
    Returns an immutable list contains all winners.
    <br>
    <b>Note: Players who are considered as heroes but were not online at the
    end would not be included in this list.</b>

    @return winners
    """
        def get_winners(self) -> List[Player]:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...