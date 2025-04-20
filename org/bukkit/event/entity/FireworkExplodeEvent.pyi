from org.bukkit.entity import Firework
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class FireworkExplodeEvent(EntityEvent, Cancellable):
    """
    Called when a firework explodes.
    """

    handlers: HandlerList = HandlerList()
    cancel: bool

    def __init__(self, what: Firework) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    """
    Set the cancelled state of this event. If the firework explosion is
    cancelled, the firework will still be removed, but no particles will be
    displayed.

    :param cancel: whether to cancel or not.
    """
    def setCancelled(self, cancel: bool) -> None:
        ...

    def getEntity(self) -> Firework:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...