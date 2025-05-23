from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.jetbrains.annotations import ApiStatus, NotNull

"""
Called when an {@link Entity} is removed.
<p>
This event should only be used for monitoring. The result
of modifying the entity during or after this event is unspecified.
This event is not called for a {@link org.bukkit.entity.Player}.
"""
class EntityRemoveEvent(EntityEvent):
    handlers: HandlerList = HandlerList()
    cause: 'EntityRemoveEvent.Cause'

    def __init__(self, what: Entity, cause: 'EntityRemoveEvent.Cause') -> None:
        super().__init__(what)
        self.cause = cause

    """
    Gets the cause why the entity got removed.

    @return: the cause why the entity got removed
    """
        def getCause(self) -> 'EntityRemoveEvent.Cause':
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    """
    Represents various ways an entity gets removed.
    """
    class Cause:
        """
        When an entity dies.
        """
        DEATH = ...

        """
        When an entity does despawn. This includes mobs which are too far away,
        items or arrows which lay too long on the ground or area effect cloud.
        """
        DESPAWN = ...

        """
        When an entity gets removed because it drops as an item.
        For example, trident or falling sand.
        <p>
        <b>Note:</b> Depending on other factors, such as gamerules, no item will actually drop,
        the cause, however, will still be drop.
        """
        DROP = ...

        """
        When an entity gets removed because it enters a block.
        For example, bees or silverfish.
        """
        ENTER_BLOCK = ...

        """
        When an entity gets removed because it exploded.
        For example, creepers, tnt or firework.
        """
        EXPLODE = ...

        """
        When an entity gets removed because it hit something. This mainly applies to projectiles.
        """
        HIT = ...

        """
        When an entity gets removed because it merges with another one.
        For example, items or xp.
        """
        MERGE = ...

        """
        When an entity gets removed because it is too far below the world.
        This only applies to entities which get removed immediately,
        some entities get damage instead.
        """
        OUT_OF_WORLD = ...

        """
        When an entity gets removed because it got pickup.
        For example, items, arrows, xp or parrots which get on a player shoulder.
        """
        PICKUP = ...

        """
        When an entity gets removed with a player because the player quits the game.
        For example, a boat which gets removed with the player when he quits.
        """
        PLAYER_QUIT = ...

        """
        When a plugin manually removes an entity.
        """
        PLUGIN = ...

        """
        When an entity gets removed because it transforms into another one.
        """
        TRANSFORMATION = ...

        """
        When the chunk an entity is in gets unloaded.
        """
        UNLOAD = ...