from org.bukkit.plugin import RegisteredServiceProvider
from org.bukkit.event.server import ServerEvent
from typing import TypeVar

T = TypeVar('T')

class ServiceEvent(ServerEvent):
    """
    An event relating to a registered service. This is called in a {@link
    org.bukkit.plugin.ServicesManager}
    """

    def __init__(self, provider: RegisteredServiceProvider[T]) -> None:
        ...
    
    def get_provider(self) -> RegisteredServiceProvider[T]:
        ...