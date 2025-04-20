from collections import defaultdict
from typing import TypeVar, Generic, List, Dict, Set, Optional, Iterator
from org.bukkit import Bukkit
from org.bukkit.event.server import ServiceRegisterEvent, ServiceUnregisterEvent
from org.jetbrains.annotations import NotNull, Nullable

T = TypeVar('T')
K = TypeVar('K')

class RegisteredServiceProvider(Generic[T]):
    def __init__(self, service: Type[T], provider: T, priority: 'ServicePriority', plugin: 'Plugin') -> None:
        ...

class SimpleServicesManager:
    """
    A simple services manager.
    """

    def __init__(self) -> None:
        self.providers: Dict[Type[K], List[RegisteredServiceProvider[K]]] = defaultdict(list)

    def register(self, service: Type[T], provider: T, plugin: 'Plugin', priority: 'ServicePriority') -> None:
        """
        Register a provider of a service.

        :param service: service class
        :param provider: provider to register
        :param plugin: plugin with the provider
        :param priority: priority of the provider
        """
        ...

    def unregisterAll(self, plugin: 'Plugin') -> None:
        """
        Unregister all the providers registered by a particular plugin.

        :param plugin: The plugin
        """
        ...

    def unregister(self, service: Type[K], provider: object) -> None:
        """
        Unregister a particular provider for a particular service.

        :param service: The service interface
        :param provider: The service provider implementation
        """
        ...

    def unregister(self, provider: object) -> None:
        """
        Unregister a particular provider.

        :param provider: The service provider implementation
        """
        ...

    def load(self, service: Type[T]) -> Optional[T]:
        """
        Queries for a provider. This may return if no provider has been
        registered for a service. The highest priority provider is returned.

        :param service: The service interface
        :return: provider or None
        """
        ...

    def getRegistration(self, service: Type[T]) -> Optional[RegisteredServiceProvider[T]]:
        """
        Queries for a provider registration. This may return if no provider
        has been registered for a service.

        :param service: The service interface
        :return: provider registration or None
        """
        ...

    def getRegistrations(self, plugin: 'Plugin') -> List[RegisteredServiceProvider]:
        """
        Get registrations of providers for a plugin.

        :param plugin: The plugin
        :return: provider registrations
        """
        ...

    def getRegistrations(self, service: Type[T]) -> List[RegisteredServiceProvider[T]]:
        """
        Get registrations of providers for a service. The returned list is
        an unmodifiable copy.

        :param service: The service interface
        :return: a copy of the list of registrations
        """
        ...

    def getKnownServices(self) -> Set[Type[K]]:
        """
        Get a list of known services. A service is known if it has registered
        providers for it.

        :return: a copy of the set of known services
        """
        ...

    def isProvidedFor(self, service: Type[T]) -> bool:
        """
        Returns whether a provider has been registered for a service.

        :param service: service to check
        :return: true if and only if there are registered providers
        """
        ...