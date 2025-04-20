from org.bukkit.entity import Entity
from org.bukkit.entity import Explosive
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class ExplosionPrimeEvent(EntityEvent, Cancellable):
    """
    Called when an entity has made a decision to explode.
    """
    
    handlers: HandlerList = HandlerList()
    cancel: bool
    radius: float
    fire: bool

    def __init__(self, what: Entity, radius: float, fire: bool) -> None:
        ...
    
    def __init__(self, explosive: Explosive) -> None:
        ...
    
    def isCancelled(self) -> bool:
        ...
    
    def setCancelled(self, cancel: bool) -> None:
        ...
    
    """
    Gets the radius of the explosion

    @return returns the radius of the explosion
    """
    def getRadius(self) -> float:
        ...
    
    """
    Sets the radius of the explosion

    @param radius the radius of the explosion
    """
    def setRadius(self, radius: float) -> None:
        ...
    
    """
    Gets whether this explosion will create fire or not

    @return true if this explosion will create fire
    """
    def getFire(self) -> bool:
        ...
    
    """
    Sets whether this explosion will create fire or not

    @param fire true if you want this explosion to create fire
    """
    def setFire(self, fire: bool) -> None:
        ...
    
    def getHandlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def getHandlerList() -> HandlerList:
        ...