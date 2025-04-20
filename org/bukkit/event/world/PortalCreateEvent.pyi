from typing import List, Optional
from org.bukkit import World
from org.bukkit.block import BlockState
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.world import WorldEvent
from org.jetbrains.annotations import NotNull, Nullable

"""
Called when a portal is created
"""
class PortalCreateEvent(WorldEvent, Cancellable):
    handlers: HandlerList = HandlerList()
    cancel: bool
    blocks: List[BlockState]
    entity: Optional[Entity]
    reason: 'CreateReason'

    @Deprecated(since="1.14.1")
    def __init__(self, blocks: List[BlockState], world: World, reason: 'CreateReason') -> None:
        ...

    def __init__(self, blocks: List[BlockState], world: World, entity: Optional[Entity], reason: 'CreateReason') -> None:
        ...

    """
    Gets an array list of all the blocks associated with the created portal

    @return array list of all the blocks associated with the created portal
    """
        def getBlocks(self) -> List[BlockState]:
        ...

    """
    Returns the Entity that triggered this portal creation (if available)

    @return Entity involved in this event
    """
        def getEntity(self) -> Optional[Entity]:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Gets the reason for the portal's creation

    @return CreateReason for the portal's creation
    """
        def getReason(self) -> 'CreateReason':
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    """
    An enum to specify the various reasons for a portal's creation
    """
    class CreateReason:
        """
        When the blocks inside a portal are created due to a portal frame
        being set on fire.
        """
        FIRE = ...

        """
        When a nether portal frame and portal is created at the exit of an
        entered nether portal.
        """
        NETHER_PAIR = ...

        """
        When the target end platform is created as a result of a player
        entering an end portal.
        """
        END_PLATFORM = ...