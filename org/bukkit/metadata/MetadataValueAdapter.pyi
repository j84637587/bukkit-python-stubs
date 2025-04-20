from weakref import WeakReference
from org.bukkit.plugin import Plugin
from org.bukkit.util import NumberConversions
from org.jetbrains.annotations import NotNull, Nullable

"""
Optional base class for facilitating MetadataValue implementations.
This provides all the conversion functions for MetadataValue so that
writing an implementation of MetadataValue is as simple as implementing
value() and invalidate().
"""
class MetadataValueAdapter:
    owning_plugin: WeakReference[Plugin]

    def __init__(self, owning_plugin: NotNull[Plugin]) -> None:
        """
        :param owning_plugin: The owning plugin.
        """
        ...

        def get_owning_plugin(self) -> Plugin:
        ...

    def as_int(self) -> int:
        ...

    def as_float(self) -> float:
        ...

    def as_double(self) -> float:
        ...

    def as_long(self) -> int:
        ...

    def as_short(self) -> int:
        ...

    def as_byte(self) -> int:
        ...

    def as_boolean(self) -> bool:
        ...

        def as_string(self) -> str:
        ...