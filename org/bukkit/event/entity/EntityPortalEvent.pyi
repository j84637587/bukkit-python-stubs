from org.bukkit.Location import Location
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.entity.EntityTeleportEvent import EntityTeleportEvent
from typing import Optional

class EntityPortalEvent(EntityTeleportEvent):
    """
    Called when a non-player entity is about to teleport because it is in
    contact with a portal.
    <p>
    For players see {@link org.bukkit.event.player.PlayerPortalEvent}
    """

    handlers: HandlerList = HandlerList()
    search_radius: int = 128
    can_create_portal: bool = True
    creation_radius: int = 16

    def __init__(self, entity: Entity, from_location: Location, to_location: Optional[Location] = None) -> None:
        super().__init__(entity, from_location, to_location)

    def __init__(self, entity: Entity, from_location: Location, to_location: Optional[Location] = None, search_radius: int = 128) -> None:
        super().__init__(entity, from_location, to_location)
        self.search_radius = search_radius

    def __init__(self, entity: Entity, from_location: Location, to_location: Optional[Location] = None, search_radius: int = 128, can_create_portal: bool = True, creation_radius: int = 16) -> None:
        super().__init__(entity, from_location, to_location)
        self.search_radius = search_radius
        self.can_create_portal = can_create_portal
        self.creation_radius = creation_radius

    def set_search_radius(self, search_radius: int) -> None:
        """
        Set the Block radius to search in for available portals.

        :param search_radius: the radius in which to search for a portal from the location
        """
        ...

    def get_search_radius(self) -> int:
        """
        Gets the search radius value for finding an available portal.

        :return: the currently set search radius
        """
        ...

    def get_can_create_portal(self) -> bool:
        """
        Returns whether the server will attempt to create a destination portal or not.

        :return: whether there should create be a destination portal created
        """
        ...

    def set_can_create_portal(self, can_create_portal: bool) -> None:
        """
        Sets whether the server should attempt to create a destination portal or not.

        :param can_create_portal: Sets whether there should be a destination portal created
        """
        ...

    def set_creation_radius(self, creation_radius: int) -> None:
        """
        Sets the maximum radius the world is searched for a free space from the given location.

        If enough free space is found then the portal will be created there, if
        not it will force create with air-space at the target location.

        Does not apply to end portal target platforms which will always appear at
        the target location.

        :param creation_radius: the radius in which to create a portal from the location
        """
        ...

    def get_creation_radius(self) -> int:
        """
        Gets the maximum radius the world is searched for a free space from the given location.

        If enough free space is found then the portal will be created there, if
        not it will force create with air-space at the target location.

        Does not apply to end portal target platforms which will always appear at
        the target location.

        :return: the currently set creation radius
        """
        ...

    @staticmethod
    def get_handlers() -> HandlerList:
        ...
    
    @staticmethod
    def get_handler_list() -> HandlerList:
        ...