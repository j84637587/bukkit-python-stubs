from typing import Optional
from java.net import InetAddress
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.jetbrains.annotations import NotNull

"""
Stores details for players attempting to log in.
<br>
Note that this event is called <i>early</i> in the player initialization
process. It is recommended that most options involving the Player
<i>entity</i> be postponed to the {@link PlayerJoinEvent} instead.
"""
class PlayerLoginEvent(PlayerEvent):
    handlers: HandlerList = HandlerList()
    address: InetAddress
    realAddress: InetAddress
    hostname: str
    result: 'PlayerLoginEvent.Result'
    message: str

    def __init__(self, player: Player, hostname: str, address: InetAddress, realAddress: InetAddress) -> None:
        """
        This constructor defaults message to an empty string, and result to
        ALLOWED

        @param player The {@link Player} for this event
        @param hostname The hostname that was used to connect to the server
        @param address The address the player used to connect, provided for
            timing issues
        @param realAddress the actual, unspoofed connecting address
        """
        ...

    def __init__(self, player: Player, hostname: str, address: InetAddress) -> None:
        """
        This constructor defaults message to an empty string, and result to
        ALLOWED

        @param player The {@link Player} for this event
        @param hostname The hostname that was used to connect to the server
        @param address The address the player used to connect, provided for
            timing issues
        """
        ...

    def __init__(self, player: Player, hostname: str, address: InetAddress, result: 'PlayerLoginEvent.Result', message: str, realAddress: InetAddress) -> None:
        """
        This constructor pre-configures the event with a result and message

        @param player The {@link Player} for this event
        @param hostname The hostname that was used to connect to the server
        @param address The address the player used to connect, provided for
            timing issues
        @param result The result status for this event
        @param message The message to be displayed if result denies login
        @param realAddress the actual, unspoofed connecting address
        """
        ...

        def getResult(self) -> 'PlayerLoginEvent.Result':
        """
        Gets the current result of the login, as an enum

        @return Current Result of the login
        """
        ...

    def setResult(self, result: 'PlayerLoginEvent.Result') -> None:
        """
        Sets the new result of the login, as an enum

        @param result New result to set
        """
        ...

        def getKickMessage(self) -> str:
        """
        Gets the current kick message that will be used if getResult() !=
        Result.ALLOWED

        @return Current kick message
        """
        ...

    def setKickMessage(self, message: str) -> None:
        """
        Sets the kick message to display if getResult() != Result.ALLOWED

        @param message New kick message
        """
        ...

        def getHostname(self) -> str:
        """
        Gets the hostname that the player used to connect to the server, or
        blank if unknown

        @return The hostname
        """
        ...

    def allow(self) -> None:
        """
        Allows the player to log in
        """
        ...

    def disallow(self, result: 'PlayerLoginEvent.Result', message: str) -> None:
        """
        Disallows the player from logging in, with the given reason

        @param result New result for disallowing the player
        @param message Kick message to display to the user
        """
        ...

        def getAddress(self) -> InetAddress:
        """
        Gets the {@link InetAddress} for the Player associated with this event.
        This method is provided as a workaround for player.getAddress()
        returning null during PlayerLoginEvent.

        @return The address for this player. For legacy compatibility, this may
            be null.
        """
        ...

        def getRealAddress(self) -> InetAddress:
        """
        Gets the connection address of this player, regardless of whether it has
        been spoofed or not.

        @return the player's connection address
        @see #getAddress()
        """
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    """
    Basic kick reasons for communicating to plugins
    """
    class Result:
        """
        The player is allowed to log in
        """
        ALLOWED = ...
        """
        The player is not allowed to log in, due to the server being full
        """
        KICK_FULL = ...
        """
        The player is not allowed to log in, due to them being banned
        """
        KICK_BANNED = ...
        """
        The player is not allowed to log in, due to them not being on the
        white list
        """
        KICK_WHITELIST = ...
        """
        The player is not allowed to log in, for reasons undefined
        """
        KICK_OTHER = ...