from typing import Dict, Optional
from org.bukkit.entity import EntitySnapshot
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.loot import LootTable
from org.bukkit.block.spawner import SpawnRule
from google.common.base import Preconditions


class SpawnerEntry:
    """
    Represents a weighted spawn potential that can be added to a monster spawner.
    """

    def __init__(self, snapshot: EntitySnapshot, spawn_weight: int, spawn_rule: Optional[SpawnRule] = None, equipment: Optional['SpawnerEntry.Equipment'] = None) -> None:
        ...

        def get_snapshot(self) -> EntitySnapshot:
        """
        Gets the {@link EntitySnapshot} for this SpawnerEntry.

        @return the snapshot
        """
        ...

    def set_snapshot(self, snapshot: EntitySnapshot) -> None:
        """
        Sets the {@link EntitySnapshot} for this SpawnerEntry.

        @param snapshot the snapshot
        """
        ...

    def get_spawn_weight(self) -> int:
        """
        Gets the weight for this SpawnerEntry, when added to a spawner entries
        with higher weight will spawn more often.

        @return the weight
        """
        ...

    def set_spawn_weight(self, spawn_weight: int) -> None:
        """
        Sets the weight for this SpawnerEntry, when added to a spawner entries
        with higher weight will spawn more often.

        @param spawn_weight the new spawn weight
        """
        ...

        def get_spawn_rule(self) -> Optional[SpawnRule]:
        """
        Gets a copy of the {@link SpawnRule} for this SpawnerEntry, or null if
        none has been set.

        @return a copy of the spawn rule or null
        """
        ...

    def set_spawn_rule(self, spawn_rule: Optional[SpawnRule]) -> None:
        """
        Sets the {@link SpawnRule} for this SpawnerEntry, null may be used to
        clear the current spawn rule.

        @param spawn_rule the new spawn rule to use or null
        """
        ...

        def get_equipment(self) -> Optional['SpawnerEntry.Equipment']:
        """
        Gets the equipment which will be applied to the spawned entity.

        @return the equipment, or null
        """
        ...

    def set_equipment(self, equipment: Optional['SpawnerEntry.Equipment']) -> None:
        """
        Sets the equipment which will be applied to the spawned entity.

        @param equipment new equipment, or null
        """
        ...


    class Equipment:
        """
        Represents the equipment loot table applied to a spawned entity.
        """

        def __init__(self, equipment_loot_table: LootTable, drop_chances: Dict[EquipmentSlot, float]) -> None:
            ...

        def set_equipment_loot_table(self, table: LootTable) -> None:
            """
            Set the loot table for the entity.
            <br>
            To remove a loot table use null.

            @param table this {@link org.bukkit.entity.Mob} will have.
            """
            ...

                def get_equipment_loot_table(self) -> LootTable:
            """
            Gets the loot table for the entity.
            <br>

            If an entity does not have a loot table, this will return null, NOT
            an empty loot table.

            @return the loot table for this entity.
            """
            ...

                def get_drop_chances(self) -> Dict[EquipmentSlot, float]:
            """
            Gets a mutable map of the drop chances for each slot of the entity.
            If non-null, the entity's drop chances will be overridden with the
            given value.

            @return mutable map of drop chances
            """
            ...