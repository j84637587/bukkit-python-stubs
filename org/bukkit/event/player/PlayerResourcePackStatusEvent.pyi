from uuid import UUID
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Literal

class PlayerResourcePackStatusEvent(PlayerEvent):
    """
    Called when a player takes action on a resource pack request sent via
    {@link Player#setResourcePack(java.lang.String)}.
    """

    handlers: HandlerList = HandlerList()
    id: UUID
    status: 'PlayerResourcePackStatusEvent.Status'

    def __init__(self, who: Player, id: UUID, resource_pack_status: 'PlayerResourcePackStatusEvent.Status') -> None:
        super().__init__(who)
        self.id = id
        self.status = resource_pack_status

    """
    Gets the unique ID of this pack.

    @return unique resource pack ID.
    """
    def get_id(self) -> UUID:
        ...

    """
    Gets the status of this pack.

    @return the current status
    """
    def get_status(self) -> 'PlayerResourcePackStatusEvent.Status':
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...

    class Status:
        """
        Status of the resource pack.
        """
        SUCCESSFULLY_LOADED: Literal['SUCCESSFULLY_LOADED']
        DECLINED: Literal['DECLINED']
        FAILED_DOWNLOAD: Literal['FAILED_DOWNLOAD']
        ACCEPTED: Literal['ACCEPTED']
        DOWNLOADED: Literal['DOWNLOADED']
        INVALID_URL: Literal['INVALID_URL']
        FAILED_RELOAD: Literal['FAILED_RELOAD']
        DISCARDED: Literal['DISCARDED']