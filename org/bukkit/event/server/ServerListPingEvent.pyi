from typing import Iterator, Optional
from org.bukkit import Bukkit
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList, ServerEvent
from org.bukkit.util import CachedServerIcon
from java.net import InetAddress
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull, UndefinedNullability

"""
Called when a server list ping is coming in. Displayed players can be
checked and removed by {@link #iterator() iterating} over this event.
<br>
<b>Note:</b> The players in {@link #iterator()} will not be shown in the
server info if {@link Bukkit#getHideOnlinePlayers()} is true.
"""
class ServerListPingEvent(ServerEvent, Iterable[Player]):
    MAGIC_PLAYER_COUNT: int = -2147483648
    handlers: HandlerList = HandlerList()
    hostname: str
    address: InetAddress
    motd: str
    numPlayers: int
    maxPlayers: int

    def __init__(self, hostname: str, address: InetAddress, motd: str, numPlayers: int, maxPlayers: int) -> None:
        """
        Initializes a new ServerListPingEvent.

        :param hostname: The hostname that was used to connect to the server
        :param address: the address of the pinger
        :param motd: the message of the day
        :param numPlayers: the number of players
        :param maxPlayers: the max number of players
        """
        super().__init__(True)
        Preconditions.checkArgument(numPlayers >= 0, "Cannot have negative number of players online", numPlayers)
        self.hostname = hostname
        self.address = address
        self.motd = motd
        self.numPlayers = numPlayers
        self.maxPlayers = maxPlayers

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        return cls.handlers

        def getHostname(self) -> str:
        """
        Gets the hostname that the player used to connect to the server, or
        blank if unknown

        :return: The hostname
        """
        return self.hostname

        def getAddress(self) -> InetAddress:
        """
        Get the address the ping is coming from.

        :return: the address
        """
        return self.address

        def getMotd(self) -> str:
        """
        Get the message of the day message.

        :return: the message of the day
        """
        return self.motd

    def setMotd(self, motd: str) -> None:
        """
        Change the message of the day message.

        :param motd: the message of the day
        """
        self.motd = motd

    def getNumPlayers(self) -> int:
        """
        Get the number of players sent.

        :return: the number of players
        """
        numPlayers = self.numPlayers
        if numPlayers == self.MAGIC_PLAYER_COUNT:
            numPlayers = 0
            for player in self:
                numPlayers += 1
        return numPlayers

    def getMaxPlayers(self) -> int:
        """
        Get the maximum number of players sent.

        :return: the maximum number of players
        """
        return self.maxPlayers

    @Deprecated(since="1.19.3")
    def shouldSendChatPreviews(self) -> bool:
        """
        Gets whether the server needs to send a preview of the chat to the
        client.

        :return: true if chat preview is enabled, false otherwise
        """
        return False

    def setMaxPlayers(self, maxPlayers: int) -> None:
        """
        Set the maximum number of players sent.

        :param maxPlayers: the maximum number of player
        """
        self.maxPlayers = maxPlayers

    def setServerIcon(self, icon: Optional[CachedServerIcon]) -> None:
        """
        Sets the server-icon sent to the client.

        :param icon: the icon to send to the client
        :raises IllegalArgumentException: if the {@link CachedServerIcon} is not
            created by the caller of this event; null may be accepted for some
            implementations
        :raises UnsupportedOperationException: if the caller of this event does
            not support setting the server icon
        """
        raise UnsupportedOperationException()

        def getHandlers(self) -> HandlerList:
        return self.handlers

        def iterator(self) -> Iterator[Player]:
        """
        {@inheritDoc}
        <p>
        Calling the {@link Iterator#remove()} method will force that particular
        player to not be displayed on the player list, decrease the size
        returned by {@link #getNumPlayers()}, and will not be returned again by
        any new iterator.
        <br>
        <b>Note:</b> The players here will not be shown in the server info if
        {@link Bukkit#getHideOnlinePlayers()} is true.

        :raises UnsupportedOperationException: if the caller of this event does
            not support removing players
        """
        raise UnsupportedOperationException()