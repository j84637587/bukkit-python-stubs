from typing import TypeVar, Generic, Any
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import ServicePriority

T = TypeVar('T')

class RegisteredServiceProvider(Generic[T]):
    """
    A registered service provider.

    @param T: Service
    """

    def __init__(self, service: type[T], provider: T, priority: ServicePriority, plugin: Plugin) -> None:
        ...

    def get_service(self) -> type[T]:
        """
        :return: The service class.
        """
        ...

    def get_plugin(self) -> Plugin:
        """
        :return: The plugin associated with this service provider.
        """
        ...

    def get_provider(self) -> T:
        """
        :return: The provider instance.
        """
        ...

    def get_priority(self) -> ServicePriority:
        """
        :return: The priority of the service provider.
        """
        ...

    def compare_to(self, other: RegisteredServiceProvider[Any]) -> int:
        """
        Compares this service provider with another.

        :param other: The other service provider to compare with.
        :return: A negative integer, zero, or a positive integer as this service provider
                 is less than, equal to, or greater than the specified object.
        """
        ...