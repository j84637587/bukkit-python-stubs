from org.bukkit.event import HandlerList
from org.bukkit.plugin import RegisteredServiceProvider
from typing import TypeVar

T = TypeVar('T')

class ServiceRegisterEvent(ServiceEvent):
    """
    This event is called when a service is registered.
    <p>
    Warning: The order in which register and unregister events are called
    should not be relied upon.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, registered_provider: RegisteredServiceProvider[T]) -> None:
        super().__init__(registered_provider)

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        return ServiceRegisterEvent.handlers