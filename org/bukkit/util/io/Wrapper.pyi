from typing import TypeVar, Generic, Dict, Any
from google.common.collect import ImmutableMap
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import ConfigurationSerialization
from org.jetbrains.annotations import NotNull

T = TypeVar('T', bound=Dict[str, Any])

class Wrapper(Generic[T]):
    """
    Wrapper class for a map that is also Serializable.
    """
    
    serialVersionUID: int = -986209235411767547

    map: T

    @staticmethod
    def new_wrapper(obj: ConfigurationSerializable) -> 'Wrapper[ImmutableMap[str, Any]]':
        """
        Creates a new Wrapper instance for the given ConfigurationSerializable object.
        """
        ...

    def __init__(self, map: T) -> None:
        """
        Initializes the Wrapper with the provided map.
        """
        ...