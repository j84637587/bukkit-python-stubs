from typing import List, TypeVar
from org.bukkit.plugin import Plugin
from org.bukkit.metadata import MetadataValue
from org.jetbrains.annotations import NotNull

T = TypeVar('T')

class MetadataStore:
    """
    Interface for managing metadata associated with objects.
    """

    def set_metadata(self, subject: NotNull[T], metadata_key: NotNull[str], new_metadata_value: NotNull[MetadataValue]) -> None:
        """
        Adds a metadata value to an object.

        :param subject: The object receiving the metadata.
        :param metadata_key: A unique key to identify this metadata.
        :param new_metadata_value: The metadata value to apply.
        :raises IllegalArgumentException: If value is null, or the owning plugin is null.
        """
        ...

    def get_metadata(self, subject: NotNull[T], metadata_key: NotNull[str]) -> NotNull[List[MetadataValue]]:
        """
        Returns all metadata values attached to an object. If multiple plugins
        have attached metadata, each will value will be included.

        :param subject: the object being interrogated.
        :param metadata_key: the unique metadata key being sought.
        :return: A list of values, one for each plugin that has set the requested value.
        """
        ...

    def has_metadata(self, subject: NotNull[T], metadata_key: NotNull[str]) -> bool:
        """
        Tests to see if a metadata attribute has been set on an object.

        :param subject: the object upon which the has-metadata test is performed.
        :param metadata_key: the unique metadata key being queried.
        :return: the existence of the metadataKey within subject.
        """
        ...

    def remove_metadata(self, subject: NotNull[T], metadata_key: NotNull[str], owning_plugin: NotNull[Plugin]) -> None:
        """
        Removes a metadata item owned by a plugin from a subject.

        :param subject: the object to remove the metadata from.
        :param metadata_key: the unique metadata key identifying the metadata to remove.
        :param owning_plugin: the plugin attempting to remove a metadata item.
        :raises IllegalArgumentException: If plugin is null.
        """
        ...

    def invalidate_all(self, owning_plugin: NotNull[Plugin]) -> None:
        """
        Invalidates all metadata in the metadata store that originates from the
        given plugin. Doing this will force each invalidated metadata item to
        be recalculated the next time it is accessed.

        :param owning_plugin: the plugin requesting the invalidation.
        :raises IllegalArgumentException: If plugin is null.
        """
        ...