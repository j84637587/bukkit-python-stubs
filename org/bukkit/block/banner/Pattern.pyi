from typing import Dict, Any, Optional
from .dye_color import DyeColor
from .pattern_type import PatternType
from .namespaced_key import NamespacedKey
from .registry import Registry
from .configuration_serializable import ConfigurationSerializable
from .serializable_as import SerializableAs

@SerializableAs("Pattern")
class Pattern(ConfigurationSerializable):
    COLOR: str = "color"
    PATTERN: str = "pattern"

    def __init__(self, color: DyeColor, pattern: PatternType) -> None:
        """Creates a new pattern from the specified color and pattern type.

        Args:
            color: The pattern color.
            pattern: The pattern type.
        """
        ...

    def __init__(self, map: Dict[str, Any]) -> None:
        """Constructor for deserialization.

        Args:
            map: The map to deserialize from.
        """
        ...

    @staticmethod
    def get_string(map: Dict[Any, Any], key: Any) -> str:
        """Retrieves a string from the map.

        Args:
            map: The map to retrieve from.
            key: The key to look for.

        Raises:
            NoSuchElementException: If the key is not found in the map.
        """
        ...

    def serialize(self) -> Dict[str, Any]:
        """Serializes the pattern to a map.

        Returns:
            A map representing the serialized pattern.
        """
        ...

    def get_color(self) -> DyeColor:
        """Returns the color of the pattern.

        Returns:
            The color of the pattern.
        """
        ...

    def get_pattern(self) -> PatternType:
        """Returns the type of pattern.

        Returns:
            The pattern type.
        """
        ...

    def __hash__(self) -> int:
        """Returns the hash code for the pattern.

        Returns:
            The hash code.
        """
        ...

    def __eq__(self, obj: Optional[Any]) -> bool:
        """Checks if this pattern is equal to another object.

        Args:
            obj: The object to compare with.

        Returns:
            True if the objects are equal, False otherwise.
        """
        ...