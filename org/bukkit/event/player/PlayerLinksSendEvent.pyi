from org.bukkit import ServerLinks
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.jetbrains.annotations import ApiStatus, NotNull

"""
This event is called when the list of links is sent to the player.
"""
class PlayerLinksSendEvent(PlayerEvent):
    handlers: HandlerList = HandlerList()
    links: ServerLinks

    def __init__(self, player: Player, links: ServerLinks) -> None:
        super().__init__(player)
        self.links = links

    """
    Gets the links to be sent, for modification.

    @return: the links
    """
        def getLinks(self) -> ServerLinks:
        return self.links

        def getHandlers(self) -> HandlerList:
        return self.handlers

        @staticmethod
    def getHandlerList() -> HandlerList:
        return PlayerLinksSendEvent.handlers