from org.bukkit.plugin import Plugin
from typing import Optional, Any

class FixedMetadataValue:
    """
    A FixedMetadataValue is a special case metadata item that contains the same
    value forever after initialization. Invalidating a FixedMetadataValue has
    no effect.
    <p>
    This class extends LazyMetadataValue for historical reasons, even though it
    overrides all the implementation methods. it is possible that in the future
    the inheritance hierarchy may change.
    """

    def __init__(self, owning_plugin: Plugin, value: Optional[Any]) -> None:
        """
        Initializes a FixedMetadataValue with an Object

        @param owning_plugin the {@link Plugin} that created this metadata value
        @param value the value assigned to this metadata value
        """
        ...

    def invalidate(self) -> None:
        """Invalidates this metadata value."""
        ...

    def value(self) -> Optional[Any]:
        """Returns the internal value."""
        ...