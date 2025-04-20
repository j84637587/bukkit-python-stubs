from org.bukkit.event import HandlerList
from org.bukkit.plugin import RegisteredServiceProvider
from typing import TypeVar

T = TypeVar('T')

class ServiceUnregisterEvent(ServiceEvent):
    """
    This event is called when a service is unregistered.
    <p>
    Warning: The order in which register and unregister events are called
    should not be relied upon.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, service_provider: RegisteredServiceProvider[T]) -> None:
        super().__init__(service_provider)

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @classmethod
    def get_handler_list(cls) -> HandlerList:
        return cls.handlers