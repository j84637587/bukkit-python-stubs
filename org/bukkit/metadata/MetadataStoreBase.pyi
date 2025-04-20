from collections import UserDict
from typing import TypeVar, Generic, List, Dict, Collection
from org.bukkit.plugin import Plugin
from org.bukkit.metadata import MetadataValue
from google.common.base import Preconditions
from typing import Optional

T = TypeVar('T')

class MetadataStoreBase(Generic[T]):
    """
    Abstract base class for a metadata store.
    """

    def __init__(self) -> None:
        self.metadataMap: Dict[str, Dict[Plugin, MetadataValue]] = {}

    def set_metadata(self, subject: T, metadata_key: str, new_metadata_value: MetadataValue) -> None:
        """
        Adds a metadata value to an object. Each metadata value is owned by a
        specific {@link Plugin}. If a plugin has already added a metadata value
        to an object, that value will be replaced with the value of {@code
        newMetadataValue}. Multiple plugins can set independent values for the
        same {@code metadataKey} without conflict.
        <p>
        Implementation note: I considered using a {@link
        java.util.concurrent.locks.ReadWriteLock} for controlling access to
        {@code metadataMap}, but decided that the added overhead wasn't worth
        the finer grained access control.
        <p>
        Bukkit is almost entirely single threaded so locking overhead shouldn't
        pose a problem.
        
        @param subject The object receiving the metadata.
        @param metadata_key A unique key to identify this metadata.
        @param new_metadata_value The metadata value to apply.
        @raises ValueError If value is null, or the owning plugin is null
        @see MetadataStore#setMetadata(Object, String, MetadataValue)
        """
        pass

    def get_metadata(self, subject: T, metadata_key: str) -> List[MetadataValue]:
        """
        Returns all metadata values attached to an object. If multiple
        have attached metadata, each will value will be included.
        
        @param subject the object being interrogated.
        @param metadata_key the unique metadata key being sought.
        @return A list of values, one for each plugin that has set the
            requested value.
        @see MetadataStore#getMetadata(Object, String)
        """
        pass

    def has_metadata(self, subject: T, metadata_key: str) -> bool:
        """
        Tests to see if a metadata attribute has been set on an object.
        
        @param subject the object upon which the has-metadata test is
            performed.
        @param metadata_key the unique metadata key being queried.
        @return the existence of the metadataKey within subject.
        """
        pass

    def remove_metadata(self, subject: T, metadata_key: str, owning_plugin: Plugin) -> None:
        """
        Removes a metadata item owned by a plugin from a subject.
        
        @param subject the object to remove the metadata from.
        @param metadata_key the unique metadata key identifying the metadata to
            remove.
        @param owning_plugin the plugin attempting to remove a metadata item.
        @raises ValueError If plugin is null
        @see MetadataStore#removeMetadata(Object, String,
            org.bukkit.plugin.Plugin)
        """
        pass

    def invalidate_all(self, owning_plugin: Plugin) -> None:
        """
        Invalidates all metadata in the metadata store that originates from the
        given plugin. Doing this will force each invalidated metadata item to
        be recalculated the next time it is accessed.
        
        @param owning_plugin the plugin requesting the invalidation.
        @raises ValueError If plugin is null
        @see MetadataStore#invalidateAll(org.bukkit.plugin.Plugin)
        """
        pass

    def disambiguate(self, subject: T, metadata_key: str) -> str:
        """
        Creates a unique name for the object receiving metadata by combining
        unique data from the subject with a metadataKey.
        <p>
        The name created must be globally unique for the given object and any
        two equivalent objects must generate the same unique name. For example,
        two Player objects must generate the same string if they represent the
        same player, even if the objects would fail a reference equality test.
        
        @param subject The object for which this key is being generated.
        @param metadata_key The name identifying the metadata value.
        @return a unique metadata key for the given subject.
        """
        pass