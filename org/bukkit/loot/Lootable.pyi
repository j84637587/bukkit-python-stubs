from typing import Optional
from org.bukkit.loot import LootTable

class Lootable:
    """
    Represents a {@link org.bukkit.block.Container} or a
    {@link org.bukkit.entity.Mob} that can have a loot table.
    <br>
    Container loot will only generate upon opening, and only when the container
    is <i>first</i> opened.
    <br>
    Entities will only generate loot upon death.
    """

    def setLootTable(self, table: Optional[LootTable]) -> None:
        """
        Set the loot table for a container or entity.
        <br>
        To remove a loot table use null.

        @param table the Loot Table this {@link org.bukkit.block.Container} or
        {@link org.bukkit.entity.Mob} will have.
        """
        ...

    def getLootTable(self) -> Optional[LootTable]:
        """
        Gets the Loot Table attached to this block or entity.
        <br>

        If an block/entity does not have a loot table, this will return null, NOT
        an empty loot table.

        @return the Loot Table attached to this block or entity.
        """
        ...

    def setSeed(self, seed: int) -> None:
        """
        Set the seed used when this Loot Table generates loot.

        @param seed the seed to used to generate loot. Default is 0.
        """
        ...

    def getSeed(self) -> int:
        """
        Get the Loot Table's seed.
        <br>
        The seed is used when generating loot.

        @return the seed
        """
        ...