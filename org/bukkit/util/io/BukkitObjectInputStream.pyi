from io import IOBase
from typing import Any, TypeVar

T = TypeVar('T')
Wrapper = TypeVar('Wrapper', bound=Any)
ConfigurationSerializable = TypeVar('ConfigurationSerializable')

class BukkitObjectInputStream(IOBase):
    """
    This class is designed to be used in conjunction with the {@link
    ConfigurationSerializable} API. It translates objects back to their
    original implementation after being serialized by {@link
    BukkitObjectInputStream}.
    <p>
    Behavior of implementations extending this class is not guaranteed across
    future versions.
    """

    def __init__(self) -> None:
        """
        Constructor provided to mirror super functionality.

        Raises:
            IOError: if an I/O error occurs while creating this stream
            SecurityError: if a security manager exists and denies
            enabling subclassing
        """
        ...

    def __init__(self, in_stream: IOBase) -> None:
        """
        Object input stream decoration constructor.

        Args:
            in_stream: the input stream to wrap

        Raises:
            IOError: if an I/O error occurs while reading stream header
        """
        ...

    def resolve_object(self, obj: Any) -> Any:
        """
        Resolves the specified object.

        Args:
            obj: the object to resolve

        Raises:
            IOError: if an error occurs during object resolution
        """
        ...

    @staticmethod
    def new_io_exception(string: str, cause: Exception) -> IOError:
        """
        Creates a new IOException with the specified message and cause.

        Args:
            string: the error message
            cause: the cause of the exception

        Returns:
            An instance of IOError.
        """
        ...