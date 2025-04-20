from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Any

class PlayerHideEntityEvent(PlayerEvent):
    """
    Called when a visible entity is hidden from a player.
    <br>
    This event is only called when the entity's visibility status is actually
    changed.
    <br>
    This event is called regardless of if the entity was within tracking range.
    
    @see Player#hideEntity(org.bukkit.plugin.Plugin, org.bukkit.entity.Entity)
    """

    handlers: HandlerList = HandlerList()
    entity: Entity

    def __init__(self, who: Player, entity: Entity) -> None:
        """
        Initializes the PlayerHideEntityEvent.

        :param who: The player who has hidden the entity.
        :param entity: The entity that has been hidden from the player.
        """
        ...

    def getEntity(self) -> Entity:
        """
        Gets the entity which has been hidden from the player.

        :return: the hidden entity
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: the handler list
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: the static handler list
        """
        ...