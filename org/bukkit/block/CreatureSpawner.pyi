from typing import Optional
from org.bukkit.spawner import Spawner
from org.jetbrains.annotations import Nullable

class CreatureSpawner(TileState, Spawner):
    """
    Represents a captured state of a creature spawner.
    """

    @Deprecated(since="1.11.2")
    def set_creature_type_by_name(self, creature_type: Optional[str]) -> None:
        """
        Set the spawner mob type.

        :param creature_type: The creature type's name or None to clear.
        :deprecated: magic value, use
        {@link #setSpawnedType(org.bukkit.entity.EntityType)}.
        """
        ...

    @Deprecated(since="1.11.2")
    def get_creature_type_name(self) -> Optional[str]:
        """
        Get the spawner's creature type.

        :return: The creature type's name if is set.
        :deprecated: magic value, use {@link #getSpawnedType()}.
        """
        ...