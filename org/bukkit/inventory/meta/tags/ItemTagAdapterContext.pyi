from org.bukkit.persistence import PersistentDataAdapterContext
from org.bukkit.persistence import PersistentDataHolder
from typing import Protocol

class ItemTagAdapterContext(Protocol):
    """
    This interface represents the context in which the {@link ItemTagType} can
    serialize and deserialize the passed values.

    @deprecated this API part has been replaced by {@link PersistentDataHolder}.
    Please use {@link PersistentDataAdapterContext} instead of this.
    """

    def new_tag_container(self) -> CustomItemTagContainer:
        """
        Creates a new and empty tag container instance.

        @return: the fresh container instance
        """
        ...