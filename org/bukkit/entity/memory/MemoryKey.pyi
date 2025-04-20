from typing import TypeVar, Generic, Dict, Set, Optional
from org.bukkit import Keyed, Location, NamespacedKey, RegistryAware
import uuid

T = TypeVar('T')

class MemoryKey(Generic[T], Keyed, RegistryAware):
    """
    Represents a key used for accessing memory values of a
    {@link org.bukkit.entity.LivingEntity}.

    @param <T> the class type of the memory value
    """

    def __init__(self, namespaced_key: NamespacedKey, t_class: type):
        """
        Initializes a MemoryKey instance.

        :param namespaced_key: The NamespacedKey for this MemoryKey.
        :param t_class: The class type of the memory value.
        """
        ...

    def get_key_or_throw(self) -> NamespacedKey:
        """
        @throws IllegalStateException if this MemoryKey is not registered.
        :return: The NamespacedKey associated with this MemoryKey.
        """
        ...

    def get_key_or_null(self) -> Optional[NamespacedKey]:
        """
        :return: The NamespacedKey associated with this MemoryKey, or None if not registered.
        """
        ...

    def is_registered(self) -> bool:
        """
        :return: True if this MemoryKey is registered, False otherwise.
        """
        ...

    @Deprecated(since="1.21.4")
    def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        :return: The NamespacedKey associated with this MemoryKey.
        """
        ...

    def get_memory_class(self) -> type:
        """
        Gets the class of values associated with this memory.

        :return: The class of value objects.
        """
        ...

    MEMORY_KEYS: Dict[NamespacedKey, 'MemoryKey'] = {}

    HOME: 'MemoryKey[Location]' = ...
    POTENTIAL_JOB_SITE: 'MemoryKey[Location]' = ...
    JOB_SITE: 'MemoryKey[Location]' = ...
    MEETING_POINT: 'MemoryKey[Location]' = ...
    GOLEM_DETECTED_RECENTLY: 'MemoryKey[bool]' = ...
    LAST_SLEPT: 'MemoryKey[int]' = ...
    LAST_WOKEN: 'MemoryKey[int]' = ...
    LAST_WORKED_AT_POI: 'MemoryKey[int]' = ...
    UNIVERSAL_ANGER: 'MemoryKey[bool]' = ...
    ANGRY_AT: 'MemoryKey[uuid.UUID]' = ...
    ADMIRING_ITEM: 'MemoryKey[bool]' = ...
    ADMIRING_DISABLED: 'MemoryKey[bool]' = ...
    HUNTED_RECENTLY: 'MemoryKey[bool]' = ...
    PLAY_DEAD_TICKS: 'MemoryKey[int]' = ...
    TEMPTATION_COOLDOWN_TICKS: 'MemoryKey[int]' = ...
    IS_TEMPTED: 'MemoryKey[bool]' = ...
    LONG_JUMP_COOLING_DOWN: 'MemoryKey[int]' = ...
    HAS_HUNTING_COOLDOWN: 'MemoryKey[bool]' = ...
    RAM_COOLDOWN_TICKS: 'MemoryKey[int]' = ...
    LIKED_PLAYER: 'MemoryKey[uuid.UUID]' = ...
    LIKED_NOTEBLOCK_POSITION: 'MemoryKey[Location]' = ...
    LIKED_NOTEBLOCK_COOLDOWN_TICKS: 'MemoryKey[int]' = ...
    ITEM_PICKUP_COOLDOWN_TICKS: 'MemoryKey[int]' = ...
    SNIFFER_EXPLORED_POSITIONS: 'MemoryKey[Location]' = ...

    @staticmethod
    def get_by_key(namespaced_key: NamespacedKey) -> Optional['MemoryKey']:
        """
        Returns a {@link MemoryKey} by a {@link NamespacedKey}.

        :param namespaced_key: The {@link NamespacedKey} referencing a
        {@link MemoryKey}
        :return: The {@link MemoryKey} or None when no {@link MemoryKey} is
        available under that key.
        """
        ...

    @staticmethod
    def values() -> Set['MemoryKey']:
        """
        Returns the set of all MemoryKeys.

        :return: The memoryKeys.
        """
        ...