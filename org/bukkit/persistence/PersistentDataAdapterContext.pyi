from org.bukkit.persistence import PersistentDataContainer
from typing import Protocol

class PersistentDataAdapterContext(Protocol):
    """
    This interface represents the context in which the {@link PersistentDataType} can
    serialize and deserialize the passed values.
    """

    def new_persistent_data_container(self) -> PersistentDataContainer:
        """
        Creates a new and empty meta container instance.

        Returns:
            PersistentDataContainer: the fresh container instance
        """
        ...