from typing import Optional
from java.net import InetAddress
from java.util import UUID
from org.bukkit.event import Event, HandlerList
from org.jetbrains.annotations import NotNull

"""
Stores details for players attempting to log in.
This event is asynchronous, and not run using main thread.
"""
class AsyncPlayerPreLoginEvent(Event):
    handlers: HandlerList = HandlerList()
    result: 'Result'
    message: str
    name: str
    ipAddress: InetAddress
    uniqueId: UUID
    transferred: bool

    @Deprecated(since="1.7.5")
    def __init__(self, name: str, ipAddress: InetAddress) -> None:
        ...

    @Deprecated(since="1.20.5")
    def __init__(self, name: str, ipAddress: InetAddress, uniqueId: UUID) -> None:
        ...

    def __init__(self, name: str, ipAddress: InetAddress, uniqueId: UUID, transferred: bool) -> None:
        ...

    """
    Gets the current result of the login, as an enum

    @return Current Result of the login
    """
        def getLoginResult(self) -> 'Result':
        ...

    """
    Gets the current result of the login, as an enum

    @return Current Result of the login
    @see #getLoginResult()
    @deprecated This method uses a deprecated enum from {@link PlayerPreLoginEvent}
    """
    @Deprecated(since="1.3.2")
        def getResult(self) -> Optional['PlayerPreLoginEvent.Result']:
        ...

    """
    Sets the new result of the login, as an enum

    @param result New result to set
    """
    def setLoginResult(self, result: 'Result') -> None:
        ...

    """
    Sets the new result of the login, as an enum

    @param result New result to set
    @see #setLoginResult(Result)
    @deprecated This method uses a deprecated enum from {@link PlayerPreLoginEvent}
    """
    @Deprecated(since="1.3.2")
    def setResult(self, result: 'PlayerPreLoginEvent.Result') -> None:
        ...

    """
    Gets the current kick message that will be used if getResult() != Result.ALLOWED

    @return Current kick message
    """
        def getKickMessage(self) -> str:
        ...

    """
    Sets the kick message to display if getResult() != Result.ALLOWED

    @param message New kick message
    """
    def setKickMessage(self, message: str) -> None:
        ...

    """
    Allows the player to log in
    """
    def allow(self) -> None:
        ...

    """
    Disallows the player from logging in, with the given reason

    @param result New result for disallowing the player
    @param message Kick message to display to the user
    """
    def disallow(self, result: 'Result', message: str) -> None:
        ...

    """
    Disallows the player from logging in, with the given reason

    @param result New result for disallowing the player
    @param message Kick message to display to the user
    @see #disallow(Result, String)
    @deprecated This method uses a deprecated enum from {@link PlayerPreLoginEvent}
    """
    @Deprecated(since="1.3.2")
    def disallow(self, result: 'PlayerPreLoginEvent.Result', message: str) -> None:
        ...

    """
    Gets the player's name.

    @return the player's name
    """
        def getName(self) -> str:
        ...

    """
    Gets the player IP address.

    @return The IP address
    """
        def getAddress(self) -> InetAddress:
        ...

    """
    Gets the player's unique ID.

    @return The unique ID
    """
        def getUniqueId(self) -> UUID:
        ...

    """
    Gets if this connection has been transferred from another server.

    @return true if the connection has been transferred
    """
    def isTransferred(self) -> bool:
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
        ALLOWED: 'Result'
        """
        The player is not allowed to log in, due to the server being full
        """
        KICK_FULL: 'Result'
        """
        The player is not allowed to log in, due to them being banned
        """
        KICK_BANNED: 'Result'
        """
        The player is not allowed to log in, due to them not being on the white list
        """
        KICK_WHITELIST: 'Result'
        """
        The player is not allowed to log in, for reasons undefined
        """
        KICK_OTHER: 'Result'

        @Deprecated(since="1.3.2")
                def old(self) -> 'PlayerPreLoginEvent.Result':
            ...