from typing import TypeVar, Generic, Collection, List, Optional
from org.bukkit.plugin import Plugin, RegisteredServiceProvider, ServicePriority

T = TypeVar('T')

class ServicesManager(Generic[T]):
    """
    Manages services and service providers. Services are an interface
    specifying a list of methods that a provider must implement. Providers are
    implementations of these services. A provider can be queried from the
    services manager in order to use a service (if one is available). If
    multiple plugins register a service, then the service with the highest
    priority takes precedence.
    """

    def register(self, service: type[T], provider: T, plugin: Plugin, priority: ServicePriority) -> None:
        """
        Register a provider of a service.

        :param service: service class
        :param provider: provider to register
        :param plugin: plugin with the provider
        :param priority: priority of the provider
        """
        ...

    def unregisterAll(self, plugin: Plugin) -> None:
        """
        Unregister all the providers registered by a particular plugin.

        :param plugin: The plugin
        """
        ...

    def unregister(self, service: type, provider: object) -> None:
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

    def load(self, service: type[T]) -> Optional[T]:
        """
        Queries for a provider. This may return None if no provider has been
        registered for a service. The highest priority provider is returned.

        :param service: The service interface
        :return: provider or None
        """
        ...

    def getRegistration(self, service: type[T]) -> Optional[RegisteredServiceProvider[T]]:
        """
        Queries for a provider registration. This may return None if no provider
        has been registered for a service.

        :param service: The service interface
        :return: provider registration or None
        """
        ...

    def getRegistrations(self, plugin: Plugin) -> List[RegisteredServiceProvider]:
        """
        Get registrations of providers for a plugin.

        :param plugin: The plugin
        :return: provider registrations
        """
        ...

    def getRegistrations(self, service: type[T]) -> Collection[RegisteredServiceProvider[T]]:
        """
        Get registrations of providers for a service. The returned list is
        unmodifiable.

        :param service: The service interface
        :return: list of registrations
        """
        ...

    def getKnownServices(self) -> Collection[type]:
        """
        Get a list of known services. A service is known if it has registered
        providers for it.

        :return: list of known services
        """
        ...

    def isProvidedFor(self, service: type[T]) -> bool:
        """
        Returns whether a provider has been registered for a service. Do not
        check this first only to call load(service) later, as that
        would be a non-thread safe situation.

        :param service: service to check
        :return: whether there has been a registered provider
        """
        ...