from org.jetbrains.annotations import NotNull
from org.bukkit.persistence import PersistentDataContainer

"""
The {@link PersistentDataHolder} interface defines an object that can store
custom persistent meta data on it.
"""
class PersistentDataHolder:
    """
    Returns a custom tag container capable of storing tags on the object.

    Note that the tags stored on this container are all stored under their
    own custom namespace therefore modifying default tags using this
    {@link PersistentDataHolder} is impossible.

    @return the persistent metadata container
    """
        def get_persistent_data_container(self) -> PersistentDataContainer:
        ...