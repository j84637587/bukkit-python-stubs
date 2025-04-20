from typing import Dict
from org.bukkit.loot import LootTable
from org.jetbrains.annotations import ApiStatus, NotNull

"""
Represents one of the configurations of a trial spawner.
"""
class TrialSpawnerConfiguration(BaseSpawner):

    def get_base_spawns_before_cooldown(self) -> float:
        """
        Gets the base number of entities the spawner will spawn before going into
        cooldown.

        @return: the number of entities
        """
        ...

    def set_base_spawns_before_cooldown(self, amount: float) -> None:
        """
        Sets the base number of entities the spawner will spawn before going into
        cooldown.

        @param amount: the number of entities
        """
        ...

    def get_base_simultaneous_entities(self) -> float:
        """
        Gets the base number of entities this spawner can track at once. <br>
        If the limit is reached the spawner will not be able to spawn any more
        entities until the existing entities are killed or move too far away.

        @return: the number of entities
        """
        ...

    def set_base_simultaneous_entities(self, amount: float) -> None:
        """
        Sets the base number of entities this spawner can track at once. <br>
        If the limit is reached the spawner will not be able to spawn any more
        entities until the existing entities are killed or move too far away.

        @param amount: the number of entities
        """
        ...

    def get_additional_spawns_before_cooldown(self) -> float:
        """
        Gets the additional number of entities the spawner will spawn per tracked player
        before going into cooldown.

        @return: the number of entities
        """
        ...

    def set_additional_spawns_before_cooldown(self, amount: float) -> None:
        """
        Sets the additional number of entities the spawner will spawn per tracked player
        before going into cooldown.

        @param amount: the number of entities
        """
        ...

    def get_additional_simultaneous_entities(self) -> float:
        """
        Gets the additional number of entities this spawner can track at once per
        tracked player. <br>
        If the limit is reached the spawner will not be able to spawn any more
        entities until the existing entities are killed or move too far away.

        @return: the number of entities
        """
        ...

    def set_additional_simultaneous_entities(self, amount: float) -> None:
        """
        Sets the additional number of entities this spawner can track at once per
        tracked player. <br>
        If the limit is reached the spawner will not be able to spawn any more
        entities until the existing entities are killed or move too far away.

        @param amount: the number of entities
        """
        ...

        def get_possible_rewards(self) -> Dict[LootTable, int]:
        """
        Gets a list of {@link LootTable}s this spawner can pick a reward from as
        well as their associated weight to be chosen.

        @return: a map of loot tables and their associated weight, or an empty
                 map if there are none
        """
        ...

    def add_possible_reward(self, table: LootTable, weight: int) -> None:
        """
        Add a {@link LootTable} to the list of tables this spawner can pick a reward
        from with a given weight.

        @param table: the loot table
        @param weight: the weight, must be at least 1
        """
        ...

    def remove_possible_reward(self, table: LootTable) -> None:
        """
        Removes the provided {@link LootTable} from the list of tables this spawner
        can pick a reward from.

        @param table: the loot table
        """
        ...

    def set_possible_rewards(self, rewards: Dict[LootTable, int]) -> None:
        """
        Sets the list of {@link LootTable}s and their weights this spawner can pick a
        reward from. <br>
        All loot tables in the map must be non-null and all weights must be at least
        1.

        @param rewards: a map of loot tables and their weights, or null to clear all
                        possible tables
        """
        ...