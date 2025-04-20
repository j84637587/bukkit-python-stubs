from org.bukkit.entity import Entity
from org.bukkit.attribute import Attribute
from org.bukkit.damage import DamageSource
from typing import Optional
from typing_extensions import Deprecated

"""
Represents an Entity that has health and can take damage.
"""
class Damageable(Entity):
    """
    Deals the given amount of damage to this entity.

    @param amount Amount of damage to deal
    """
    def damage(self, amount: float) -> None: ...

    """
    Deals the given amount of damage to this entity from a specified Entity.

    @param amount amount of damage to deal
    @param source entity to which the damage should be attributed
    """
    def damage(self, amount: float, source: Optional[Entity]) -> None: ...

    """
    Deals the given amount of damage to this entity from a specified DamageSource.

    @param amount amount of damage to deal
    @param damageSource source to which the damage should be attributed
    """
    def damage(self, amount: float, damageSource: DamageSource) -> None: ...

    """
    Gets the entity's health from 0 to getMaxHealth(), where 0 is dead.

    @return Health represented from 0 to max
    """
    def getHealth(self) -> float: ...

    """
    Sets the entity's health from 0 to getMaxHealth(), where 0 is dead.

    @param health New health represented from 0 to max
    @throws IllegalArgumentException Thrown if the health is < 0 or >
        getMaxHealth()
    """
    def setHealth(self, health: float) -> None: ...

    """
    Gets the entity's absorption amount.

    @return absorption amount from 0
    """
    def getAbsorptionAmount(self) -> float: ...

    """
    Sets the entity's absorption amount.
    Note: The amount is capped to the value of Attribute.MAX_ABSORPTION. The effect of this method on
    that attribute is currently unspecified and subject to change.

    @param amount new absorption amount from 0
    @throws IllegalArgumentException thrown if health is < 0 or non-finite.
    """
    def setAbsorptionAmount(self, amount: float) -> None: ...

    """
    Gets the maximum health this entity has.

    @return Maximum health
    @deprecated use Attribute.MAX_HEALTH.
    """
    @Deprecated(since="1.11")
    def getMaxHealth(self) -> float: ...

    """
    Sets the maximum health this entity can have.
    If the health of the entity is above the value provided it will be set
    to that value.
    Note: An entity with a health bar (Player, EnderDragon,
    Wither, etc...) will have their bar scaled accordingly.

    @param health amount of health to set the maximum to
    @deprecated use Attribute.MAX_HEALTH.
    """
    @Deprecated(since="1.11")
    def setMaxHealth(self, health: float) -> None: ...

    """
    Resets the max health to the original amount.
    @deprecated use Attribute.MAX_HEALTH.
    """
    @Deprecated(since="1.11")
    def resetMaxHealth(self) -> None: ...