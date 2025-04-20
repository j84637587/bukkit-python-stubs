from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Any

class PlayerShowEntityEvent(PlayerEvent):
    """
    Called when a hidden entity is shown to a player.
    <br>
    This event is only called when the entity's visibility status is actually
    changed.
    <br>
    This event is called regardless of whether the entity was within tracking
    range.
    
    @see Player#showEntity(org.bukkit.plugin.Plugin, org.bukkit.entity.Entity)
    """

    handlers: HandlerList = HandlerList()
    entity: Entity

    def __init__(self, who: Player, entity: Entity) -> None:
        """
        Initializes the PlayerShowEntityEvent.

        :param who: The player to whom the entity is shown.
        :param entity: The entity that is shown to the player.
        """
        super().__init__(who)
        self.entity = entity

    def getEntity(self) -> Entity:
        """
        Gets the entity which has been shown to the player.

        :return: The shown entity.
        """
        return self.entity

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: The handler list.
        """
        return self.handlers

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list.
        """
        return PlayerShowEntityEvent.handlers