from org.bukkit.block import Block
from org.bukkit.entity import Entity, Player
from org.bukkit.event import Cancellable, HandlerList
from typing import Optional

class BlockIgniteEvent(BlockEvent, Cancellable):
    """
    Called when a block is ignited. If you want to catch when a Player places
    fire, you need to use {@link BlockPlaceEvent}.
    <p>
    If a Block Ignite event is cancelled, the block will not be ignited.
    """

    handlers: HandlerList

    def __init__(self, theBlock: Block, cause: 'IgniteCause', ignitingEntity: Optional[Entity] = None) -> None:
        ...

    def __init__(self, theBlock: Block, cause: 'IgniteCause', ignitingBlock: Block) -> None:
        ...

    def __init__(self, theBlock: Block, cause: 'IgniteCause', ignitingEntity: Optional[Entity], ignitingBlock: Optional[Block] = None) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getCause(self) -> 'IgniteCause':
        """
        Gets the cause of block ignite.

        @return An IgniteCause value detailing the cause of block ignition
        """
        ...

    def getPlayer(self) -> Optional[Player]:
        """
        Gets the player who ignited this block

        @return The Player that placed/ignited the fire block, or null if not ignited by a Player.
        """
        ...

    def getIgnitingEntity(self) -> Optional[Entity]:
        """
        Gets the entity who ignited this block

        @return The Entity that placed/ignited the fire block, or null if not ignited by a Entity.
        """
        ...

    def getIgnitingBlock(self) -> Optional[Block]:
        """
        Gets the block which ignited this block

        @return The Block that placed/ignited the fire block, or null if not ignited by a Block.
        """
        ...

    class IgniteCause:
        """
        An enum to specify the cause of the ignite
        """
        LAVA = ...
        FLINT_AND_STEEL = ...
        SPREAD = ...
        LIGHTNING = ...
        FIREBALL = ...
        ENDER_CRYSTAL = ...
        EXPLOSION = ...
        ARROW = ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...