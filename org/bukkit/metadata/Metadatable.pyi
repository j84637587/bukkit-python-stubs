from typing import List
from org.bukkit.plugin import Plugin
from org.bukkit.metadata import MetadataValue

class Metadatable:
    """
    This interface is implemented by all objects that can provide metadata
    about themselves.
    """

    def set_metadata(self, metadata_key: str, new_metadata_value: MetadataValue) -> None:
        """
        Sets a metadata value in the implementing object's metadata store.

        :param metadata_key: A unique key to identify this metadata.
        :param new_metadata_value: The metadata value to apply.
        :raises ValueError: If value is None, or the owning plugin is None.
        """
        ...

    def get_metadata(self, metadata_key: str) -> List[MetadataValue]:
        """
        Returns a list of previously set metadata values from the implementing
        object's metadata store.

        :param metadata_key: the unique metadata key being sought.
        :return: A list of values, one for each plugin that has set the
                 requested value.
        """
        ...

    def has_metadata(self, metadata_key: str) -> bool:
        """
        Tests to see whether the implementing object contains the given
        metadata value in its metadata store.

        :param metadata_key: the unique metadata key being queried.
        :return: the existence of the metadata_key within subject.
        """
        ...

    def remove_metadata(self, metadata_key: str, owning_plugin: Plugin) -> None:
        """
        Removes the given metadata value from the implementing object's
        metadata store.

        :param metadata_key: the unique metadata key identifying the metadata to
                             remove.
        :param owning_plugin: This plugin's metadata value will be removed. All
                             other values will be left untouched.
        :raises ValueError: If plugin is None.
        """
        ...