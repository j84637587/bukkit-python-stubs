from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.util import Vector
from typing import Any

class PlayerInteractAtEntityEvent(PlayerInteractEntityEvent):
    """
    Represents an event that is called when a player right clicks an entity that
    also contains the location where the entity was clicked.
    <br>
    Note that the client may sometimes spuriously send this packet in addition to 
    {@link PlayerInteractEntityEvent}. Users are advised to listen to this (parent) 
    class unless specifically required.
    """

    handlers: HandlerList = HandlerList()
    position: Vector

    def __init__(self, who: Player, clicked_entity: Entity, position: Vector) -> None:
        """
        :param who: The player who interacted with the entity.
        :param clicked_entity: The entity that was clicked.
        :param position: The position where the entity was clicked.
        """
        ...

    def __init__(self, who: Player, clicked_entity: Entity, position: Vector, hand: EquipmentSlot) -> None:
        """
        :param who: The player who interacted with the entity.
        :param clicked_entity: The entity that was clicked.
        :param position: The position where the entity was clicked.
        :param hand: The equipment slot used for the interaction.
        """
        ...

    def get_clicked_position(self) -> Vector:
        """
        :return: The position where the entity was clicked.
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        :return: The handler list for this event.
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        :return: The static handler list for this event.
        """
        ...