from typing import Dict, Any
from google.common.base import Preconditions
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from org.jetbrains.annotations import NotNull

"""
Represents a spawn rule that controls what conditions an entity from a
monster spawner can spawn.
"""
@SerializableAs("SpawnRule")
class SpawnRule(ConfigurationSerializable):

    def __init__(self, min_block_light: int, max_block_light: int, min_sky_light: int, max_sky_light: int) -> None:
        """
        Constructs a new SpawnRule.

        :param min_block_light: The minimum (inclusive) block light required for
        spawning to succeed.
        :param max_block_light: The maximum (inclusive) block light required for
        spawning to succeed.
        :param min_sky_light: The minimum (inclusive) sky light required for
        spawning to succeed.
        :param max_sky_light: The maximum (inclusive) sky light required for
        spawning to succeed.
        """
        ...

    def get_min_block_light(self) -> int:
        """
        Gets the minimum (inclusive) block light required for spawning to
        succeed.

        :return: minimum block light
        """
        ...

    def set_min_block_light(self, min_block_light: int) -> None:
        """
        Sets the minimum (inclusive) block light required for spawning to
        succeed.

        :param min_block_light: minimum block light
        """
        ...

    def get_max_block_light(self) -> int:
        """
        Gets the maximum (inclusive) block light required for spawning to
        succeed.

        :return: maximum block light
        """
        ...

    def set_max_block_light(self, max_block_light: int) -> None:
        """
        Sets the maximum (inclusive) block light required for spawning to
        succeed.

        :param max_block_light: maximum block light
        """
        ...

    def get_min_sky_light(self) -> int:
        """
        Gets the minimum (inclusive) sky light required for spawning to succeed.

        :return: minimum sky light
        """
        ...

    def set_min_sky_light(self, min_sky_light: int) -> None:
        """
        Sets the minimum (inclusive) sky light required for spawning to succeed.

        :param min_sky_light: minimum sky light
        """
        ...

    def get_max_sky_light(self) -> int:
        """
        Gets the maximum (inclusive) sky light required for spawning to succeed.

        :return: maximum sky light
        """
        ...

    def set_max_sky_light(self, max_sky_light: int) -> None:
        """
        Sets the maximum (inclusive) sky light required for spawning to succeed.

        :param max_sky_light: maximum sky light
        """
        ...

    def __eq__(self, obj: Any) -> bool:
        ...

    def __hash__(self) -> int:
        ...

        def clone(self) -> 'SpawnRule':
        ...

        def serialize(self) -> Dict[str, Any]:
        ...

        @staticmethod
    def deserialize(args: Dict[str, Any]) -> 'SpawnRule':
        ...