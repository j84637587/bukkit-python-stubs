from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.entity import Projectile
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Optional

class ProjectileHitEvent(EntityEvent, Cancellable):
    """
    Called when a projectile hits an object
    """
    
    handlers: HandlerList

    def __init__(self, projectile: Projectile) -> None:
        ...

    def __init__(self, projectile: Projectile, hit_entity: Optional[Entity]) -> None:
        ...

    def __init__(self, projectile: Projectile, hit_block: Optional[Block]) -> None:
        ...

    def __init__(self, projectile: Projectile, hit_entity: Optional[Entity], hit_block: Optional[Block]) -> None:
        ...

    def __init__(self, projectile: Projectile, hit_entity: Optional[Entity], hit_block: Optional[Block], hit_face: Optional[BlockFace]) -> None:
        ...

    def getEntity(self) -> Projectile:
        """
        :return: the projectile that caused this event
        """
        ...

    def getHitBlock(self) -> Optional[Block]:
        """
        Gets the block that was hit, if it was a block that was hit.

        :return: hit block or else null
        """
        ...

    def getHitBlockFace(self) -> Optional[BlockFace]:
        """
        Gets the block face that was hit, if it was a block that was hit and the
        face was provided in the event.

        :return: hit face or else null
        """
        ...

    def getHitEntity(self) -> Optional[Entity]:
        """
        Gets the entity that was hit, if it was an entity that was hit.

        :return: hit entity or else null
        """
        ...

    def isCancelled(self) -> bool:
        ...
    
    def setCancelled(self, cancel: bool) -> None:
        """
        Whether to cancel the action that occurs when the projectile hits.

        In the case of an entity, it will not collide (unless it's a firework,
        then use {@link FireworkExplodeEvent}).
        <br>
        In the case of a block, some blocks (eg target block, bell) will not
        perform the action associated.
        <br>
        This does NOT prevent block collisions, and explosions will still occur
        unless their respective events are cancelled.

        :param cancel: true if you wish to cancel this event
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def getHandlerList() -> HandlerList:
        ...