from typing import Optional
from uuid import UUID
from java.net import InetAddress
from org.bukkit import Warning
from org.bukkit.event import Event, HandlerList

"""
Stores details for players attempting to log in

@deprecated This event causes synchronization from the login thread; {@link
    AsyncPlayerPreLoginEvent} is preferred to keep the secondary threads
    asynchronous.
"""
class PlayerPreLoginEvent(Event):
    handlers: HandlerList

    def __init__(self, name: str, ip_address: InetAddress, unique_id: Optional[UUID] = None) -> None:
        """
        @deprecated since = "1.7.5"
        """
        ...

        def getResult(self) -> 'Result':
        """
        Gets the current result of the login, as an enum

        @return Current Result of the login
        """
        ...

    def setResult(self, result: 'Result') -> None:
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

    def allow(self) -> None:
        """
        Allows the player to log in
        """
        ...

    def disallow(self, result: 'Result', message: str) -> None:
        """
        Disallows the player from logging in, with the given reason

        @param result New result for disallowing the player
        @param message Kick message to display to the user
        """
        ...

        def getName(self) -> str:
        """
        Gets the player's name.

        @return the player's name
        """
        ...

        def getAddress(self) -> InetAddress:
        """
        Gets the player IP address.

        @return The IP address
        """
        ...

        def getHandlers(self) -> HandlerList:
        ...

        def getUniqueId(self) -> UUID:
        """
        Gets the player's unique ID.

        @return The unique ID
        """
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