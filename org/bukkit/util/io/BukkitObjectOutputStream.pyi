from io import IOBase
from typing import Any
from org.bukkit.configuration.serialization import ConfigurationSerializable

class BukkitObjectOutputStream(IOBase):
    """
    This class is designed to be used in conjunction with the {@link
    ConfigurationSerializable} API. It translates objects to an internal
    implementation for later deserialization using {@link
    BukkitObjectInputStream}.
    <p>
    Behavior of implementations extending this class is not guaranteed across
    future versions.
    """

    def __init__(self, out: IOBase) -> None:
        """
        Object output stream decoration constructor.

        :param out: the stream to wrap
        :raises IOError: if an I/O error occurs while writing stream header
        """
        ...

    def __init__(self) -> None:
        """
        Constructor provided to mirror super functionality.

        :raises IOError: if an I/O error occurs while creating this stream
        :raises SecurityError: if a security manager exists and denies
        enabling subclassing
        """
        ...

    def replace_object(self, obj: Any) -> Any:
        """
        :param obj: the object to replace
        :raises IOError: if an I/O error occurs
        :return: the replaced object
        """
        ...