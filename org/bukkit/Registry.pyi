from typing import Any, Iterator, Optional, TypeVar, Union
from abc import ABC, abstractmethod

T = TypeVar('T', bound='Keyed')

class Registry(ABC):
    """
    Represents a registry of Bukkit objects that may be retrieved by
    {@link NamespacedKey}.
    """

    @abstractmethod
    def get(self, key: 'NamespacedKey') -> Optional[T]:
        """
        Get the object by its key.

        @param key non-null key
        @return item or null if does not exist
        """
        pass

    @abstractmethod
    def getOrThrow(self, key: 'NamespacedKey') -> T:
        """
        Get the object by its key.

        If there is no object with the given key, an exception will be thrown.

        @param key to get the object from
        @return object with the given key
        @throws IllegalArgumentException if there is no object with the given key
        """
        pass

    @abstractmethod
    def stream(self) -> 'Stream[T]':
        """
        Returns a new stream, which contains all registry items, which are registered to the registry.

        @return a stream of all registry items
        """
        pass

    def match(self, input: str) -> Optional[T]:
        """
        Attempts to match the registered object with the given key.
        <p>
        This will attempt to find a reasonable match based on the provided input
        and may do so through unspecified means.

        @param input non-null input
        @return registered object or null if does not exist
        """
        pass

class SimpleRegistry(Registry[T]):
    """
    A simple implementation of the Registry interface.
    """

    def __init__(self, type: 'Class[T]', predicate: 'Predicate[T]') -> None:
        pass

    def get(self, key: 'NamespacedKey') -> Optional[T]:
        pass

    def getOrThrow(self, key: 'NamespacedKey') -> T:
        pass

    def stream(self) -> 'Stream[T]':
        pass

    def iterator(self) -> Iterator[T]:
        pass

    def getType(self) -> 'Class[T]':
        pass