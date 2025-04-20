from org.bukkit.event import HandlerList
from typing import Literal, Final

class ServerLoadEvent(ServerEvent):
    """
    This event is called when either the server startup or reload has completed.
    """

    class LoadType:
        """
        Represents the context in which the enclosing event has been completed.
        """
        STARTUP: Final[Literal['STARTUP']] = 'STARTUP'
        RELOAD: Final[Literal['RELOAD']] = 'RELOAD'

    handlers: Final[HandlerList] = HandlerList()
    type: LoadType

    def __init__(self, type: LoadType) -> None:
        """
        Creates a {@code ServerLoadEvent} with a given loading type.

        :param type: the context in which the server was loaded
        """
        ...

    def getType(self) -> LoadType:
        """
        Gets the context in which the server was loaded.

        :return: the context in which the server was loaded
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        :return: the handler list for this event
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        :return: the static handler list for this event
        """
        ...