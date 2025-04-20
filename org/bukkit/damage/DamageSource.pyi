from org.bukkit import Bukkit
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.damage import DamageType
from typing import Optional, Protocol

"""
Represents a source of damage.
"""
class DamageSource(Protocol):

    def get_damage_type(self) -> DamageType:
        """
        Get the DamageType.

        @return: the damage type
        """
        ...

    def get_causing_entity(self) -> Optional[Entity]:
        """
        Get the Entity that caused the damage to occur.
        Not to be confused with get_direct_entity(), the causing entity is
        the entity to which the damage is ultimately attributed if the receiver
        is killed. If, for example, the receiver was damaged by a projectile, the
        shooter/thrower would be returned.

        @return: an Entity or null
        """
        ...

    def get_direct_entity(self) -> Optional[Entity]:
        """
        Get the Entity that directly caused the damage.
        Not to be confused with get_causing_entity(), the direct entity is
        the entity that actually inflicted the damage. If, for example, the
        receiver was damaged by a projectile, the projectile would be returned.

        @return: an Entity or null
        """
        ...

    def get_damage_location(self) -> Optional[Location]:
        """
        Get the Location from where the damage originated. This will only
        be present if an entity did not cause the damage.

        @return: the location, or null if none
        """
        ...

    def get_source_location(self) -> Optional[Location]:
        """
        Get the Location from where the damage originated.
        This is a convenience method to get the final location of the damage.
        This method will attempt to return
        get_damage_location() the damage location. If this is null, the
        get_causing_entity() causing entity location will be returned.
        Finally if there is no damage location nor a causing entity, null will be
        returned.

        @return: the source of the location or null.
        """
        ...

    def is_indirect(self) -> bool:
        """
        Get if this damage is indirect.
        Damage is considered indirect if get_causing_entity() is not equal
        to get_direct_entity(). This will be the case, for example, if a
        skeleton shot an arrow or a player threw a potion.

        @return: true if is indirect, false otherwise.
        """
        ...

    def get_food_exhaustion(self) -> float:
        """
        Get the amount of hunger exhaustion caused by this damage.

        @return: the amount of hunger exhaustion caused.
        """
        ...

    def scales_with_difficulty(self) -> bool:
        """
        Gets if this source of damage scales with difficulty.

        @return: True if scales.
        """
        ...

    @staticmethod
    def builder(damage_type: DamageType) -> 'DamageSource.Builder':
        """
        Create a new DamageSource.Builder.

        @param damage_type: the DamageType to use
        @return: a DamageSource.Builder
        """
        ...

    class Builder(Protocol):

        def with_causing_entity(self, entity: Entity) -> 'DamageSource.Builder':
            """
            Set the Entity that caused the damage.

            @param entity: the entity
            @return: this instance. Allows for chained method calls
            @see DamageSource#get_causing_entity()
            """
            ...

        def with_direct_entity(self, entity: Entity) -> 'DamageSource.Builder':
            """
            Set the Entity that directly inflicted the damage.

            @param entity: the entity
            @return: this instance. Allows for chained method calls
            @see DamageSource#get_direct_entity()
            """
            ...

        def with_damage_location(self, location: Location) -> 'DamageSource.Builder':
            """
            Set the Location of the source of damage.

            @param location: the location where the damage occurred
            @return: this instance. Allows for chained method calls
            @see DamageSource#get_source_location()
            """
            ...

        def build(self) -> DamageSource:
            """
            Create a new DamageSource instance using the supplied parameters.

            @return: the damage source instance
            """
            ...