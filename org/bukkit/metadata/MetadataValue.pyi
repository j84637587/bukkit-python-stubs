from typing import Optional, Any
from org.bukkit.plugin import Plugin

class MetadataValue:
    """
    Interface for metadata values.
    """

    def value(self) -> Optional[Any]:
        """Fetches the value of this metadata item.

        Returns:
            The metadata value.
        """
        ...

    def as_int(self) -> int:
        """Attempts to convert the value of this metadata item into an int.

        Returns:
            The value as an int.
        """
        ...

    def as_float(self) -> float:
        """Attempts to convert the value of this metadata item into a float.

        Returns:
            The value as a float.
        """
        ...

    def as_double(self) -> float:
        """Attempts to convert the value of this metadata item into a double.

        Returns:
            The value as a double.
        """
        ...

    def as_long(self) -> int:
        """Attempts to convert the value of this metadata item into a long.

        Returns:
            The value as a long.
        """
        ...

    def as_short(self) -> int:
        """Attempts to convert the value of this metadata item into a short.

        Returns:
            The value as a short.
        """
        ...

    def as_byte(self) -> int:
        """Attempts to convert the value of this metadata item into a byte.

        Returns:
            The value as a byte.
        """
        ...

    def as_boolean(self) -> bool:
        """Attempts to convert the value of this metadata item into a boolean.

        Returns:
            The value as a boolean.
        """
        ...

    def as_string(self) -> str:
        """Attempts to convert the value of this metadata item into a string.

        Returns:
            The value as a string.
        """
        ...

    def get_owning_plugin(self) -> Optional[Plugin]:
        """Returns the Plugin that created this metadata item.

        Returns:
            The plugin that owns this metadata value. Could be null if the plugin was already unloaded.
        """
        ...

    def invalidate(self) -> None:
        """Invalidates this metadata item, forcing it to recompute when next accessed."""
        ...