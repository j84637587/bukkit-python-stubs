from typing import Optional

from org.bukkit.Location import Location
from org.bukkit.entity.Entity import Entity
from org.bukkit.entity.HumanEntity import HumanEntity

class LootContext:
    """
    Represents additional information a {@link LootTable} can use to modify its
    generated loot.
    """
    
    DEFAULT_LOOT_MODIFIER: int = -1

    def __init__(self, location: Location, luck: float, looting_modifier: int, looted_entity: Optional[Entity], killer: Optional[HumanEntity]) -> None:
        """
        Initializes a LootContext instance.

        :param location: The location where the loot will be generated.
        :param luck: The luck value affecting loot generation.
        :param looting_modifier: The looting modifier.
        :param looted_entity: The entity that was looted.
        :param killer: The entity that killed the looted entity.
        """
        ...

    def get_location(self) -> Location:
        """
        The {@link Location} to store where the loot will be generated.

        :return: the Location of where the loot will be generated
        """
        ...

    def get_luck(self) -> float:
        """
        Represents the {@link org.bukkit.potion.PotionEffectType#LUCK} that an
        entity can have. The higher the value the better chance of receiving more
        loot.

        :return: luck
        """
        ...

    def get_looting_modifier(self) -> int:
        """
        Represents the {@link org.bukkit.enchantments.Enchantment#LOOTING} the
        {@link #getKiller()} entity has on their equipped item.

        This value is only set via
        {@link LootContext.Builder#lootingModifier(int)}. If not set, the
        {@link #getKiller()} entity's looting level will be used instead.

        :return: the looting level
        :deprecated: no longer functional
        """
        ...

    def get_looted_entity(self) -> Optional[Entity]:
        """
        Get the {@link Entity} that was killed. Can be null.

        :return: the looted entity or null
        """
        ...

    def get_killer(self) -> Optional[HumanEntity]:
        """
        Get the {@link HumanEntity} who killed the {@link #getLootedEntity()}.
        Can be null.

        :return: the killer entity, or null.
        """
        ...

class Builder:
    """
    Utility class to make building {@link LootContext} easier. The only
    required argument is {@link Location} with a valid (non-null)
    {@link org.bukkit.World}.
    """

    def __init__(self, location: Location) -> None:
        """
        Creates a new LootContext.Builder instance to facilitate easy
        creation of {@link LootContext}s.

        :param location: the location the LootContext should use
        """
        ...

    def luck(self, luck: float) -> 'Builder':
        """
        Set how much luck to have when generating loot.

        :param luck: the luck level
        :return: the Builder
        """
        ...

    def looting_modifier(self, modifier: int) -> 'Builder':
        """
        Set the {@link org.bukkit.enchantments.Enchantment#LOOTING}
        level equivalent to use when generating loot. Values less than or
        equal to 0 will force the {@link LootTable} to only return a single
        {@link org.bukkit.inventory.ItemStack} per pool.

        :param modifier: the looting level modifier
        :return: the Builder
        :deprecated: no longer functional
        """
        ...

    def looted_entity(self, looted_entity: Optional[Entity]) -> 'Builder':
        """
        The entity that was killed.

        :param looted_entity: the looted entity
        :return: the Builder
        """
        ...

    def killer(self, killer: Optional[HumanEntity]) -> 'Builder':
        """
        Set the {@link org.bukkit.entity.HumanEntity} that killed
        {@link #getLootedEntity()}. This entity will be used to get the
        looting level if {@link #lootingModifier(int)} is not set.

        :param killer: the killer entity
        :return: the Builder
        """
        ...

    def build(self) -> LootContext:
        """
        Create a new {@link LootContext} instance using the supplied
        parameters.

        :return: a new {@link LootContext} instance
        """
        ...