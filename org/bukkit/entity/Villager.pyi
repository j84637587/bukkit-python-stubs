from typing import Protocol, Optional
from uuid import UUID
from org.bukkit import Bukkit
from org.bukkit.entity import AbstractVillager
from org.bukkit import Location, NamespacedKey, Registry
from org.bukkit.registry import RegistryAware
from org.bukkit.util import OldEnum
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a villager NPC
"""
class Villager(AbstractVillager, Protocol):

        def get_profession(self) -> 'Profession':
        """
        Gets the current profession of this villager.

        @return Current profession.
        """
        ...

    def set_profession(self, profession: 'Profession') -> None:
        """
        Sets the new profession of this villager.

        @param profession New profession.
        """
        ...

        def get_villager_type(self) -> 'Type':
        """
        Gets the current type of this villager.

        @return Current type.
        """
        ...

    def set_villager_type(self, type: 'Type') -> None:
        """
        Sets the new type of this villager.

        @param type New type.
        """
        ...

    def get_villager_level(self) -> int:
        """
        Gets the level of this villager.

        A villager with a level of 1 and no experience is liable to lose its
        profession.

        @return this villager's level
        """
        ...

    def set_villager_level(self, level: int) -> None:
        """
        Sets the level of this villager.

        A villager with a level of 1 and no experience is liable to lose its
        profession.

        @param level the new level
        @raises IllegalArgumentException if level not between [1, 5]
        """
        ...

    def get_villager_experience(self) -> int:
        """
        Gets the trading experience of this villager.

        @return trading experience
        """
        ...

    def set_villager_experience(self, experience: int) -> None:
        """
        Sets the trading experience of this villager.

        @param experience new experience
        @raises IllegalArgumentException if experience < 0
        """
        ...

    def sleep(self, location: Location) -> bool:
        """
        Attempts to make this villager sleep at the given location.
        <br>
        The location must be in the current world and have a bed placed at the
        location. The villager will put its head on the specified block while
        sleeping.

        @param location the location of the bed
        @return whether the sleep was successful
        """
        ...

    def wakeup(self) -> None:
        """
        Causes this villager to wake up if he's currently sleeping.

        @raises IllegalStateException if not sleeping
        """
        ...

    def shake_head(self) -> None:
        """
        Causes this villager to shake his head.
        """
        ...

        def zombify(self) -> Optional['ZombieVillager']:
        """
        Convert this Villager into a ZombieVillager as if it was killed by a
        Zombie.

        <b>Note:</b> this will fire a EntityTransformEvent

        @return the converted entity {@link ZombieVillager} or null if the
        conversion is cancelled
        """
        ...

    def get_reputation(self, uuid: UUID, reputation_type: 'ReputationType') -> int:
        """
        Gets the reputation of an entity for a given type.

        @param uuid the UUID of the entity whose reputation is being checked
        @param reputation_type reputation type to be retrieved
        @return current reputation for the given reputation type
        """
        ...

    def get_weighted_reputation(self, uuid: UUID, reputation_type: 'ReputationType') -> int:
        """
        Gets the weighted reputation of an entity for a given type.

        <p>The total reputation of an entity is a sum of its weighted
        reputations of each type, where the reputation is multiplied by weight
        assigned to its type.

        @param uuid the UUID of the entity whose reputation is being checked
        @param reputation_type reputation type to be retrieved
        @return current reputation for the given reputation type
        @see ReputationType#getWeight()
        """
        ...

    def get_reputation(self, uuid: UUID) -> int:
        """
        Gets the reputation of an entity.

        @param uuid the UUID of the entity whose reputation is being checked
        @return current reputation for the given reputation type
        """
        ...

    def add_reputation(self, uuid: UUID, reputation_type: 'ReputationType', amount: int) -> None:
        """
        Add reputation of a given type towards a given entity.

        <p>The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.

        <p>Note: this will fire a
        {@link org.bukkit.event.entity.VillagerReputationChangeEvent}.

        @param uuid the UUID of the entity for whom the reputation is being
                     added
        @param reputation_type reputation type to be modified
        @param amount amount of reputation to add
        """
        ...

    def add_reputation(self, uuid: UUID, reputation_type: 'ReputationType', amount: int, change_reason: 'ReputationEvent') -> None:
        """
        Add reputation of a given type towards a given entity, with a specific
        change reason.

        <p>The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.

        <p>Note: this will fire a
        {@link org.bukkit.event.entity.VillagerReputationChangeEvent}.

        @param uuid the UUID of the entity for whom the reputation is being
                     added
        @param reputation_type reputation type to be modified
        @param amount amount of reputation to add
        @param change_reason reputation change reason
        """
        ...

    def remove_reputation(self, uuid: UUID, reputation_type: 'ReputationType', amount: int) -> None:
        """
        Remove reputation of a given type towards a given entity.

        <p>The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.

        <p>Note: this will fire a
        {@link org.bukkit.event.entity.VillagerReputationChangeEvent}.

        @param uuid the UUID of the entity for whom the reputation is being
                     removed
        @param reputation_type reputation type to be modified
        @param amount amount of reputation to remove
        """
        ...

    def remove_reputation(self, uuid: UUID, reputation_type: 'ReputationType', amount: int, change_reason: 'ReputationEvent') -> None:
        """
        Remove reputation of a given type towards a given entity, with a
        specific change reason.

        <p>The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.

        <p>Note: this will fire a
        {@link org.bukkit.event.entity.VillagerReputationChangeEvent}.

        @param uuid the UUID of the entity for whom the reputation is being
                     removed
        @param reputation_type reputation type to be modified
        @param amount amount of reputation to remove
        @param change_reason reputation change reason
        """
        ...

    def set_reputation(self, uuid: UUID, reputation_type: 'ReputationType', amount: int) -> None:
        """
        Set reputation of a given type towards a given entity.

        <p>The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.

        <p>Note: this will fire a
        {@link org.bukkit.event.entity.VillagerReputationChangeEvent}.

        @param uuid the UUID of the entity for whom the reputation is being
                     added
        @param reputation_type reputation type to be modified
        @param amount amount of reputation to add
        """
        ...

    def set_reputation(self, uuid: UUID, reputation_type: 'ReputationType', amount: int, change_reason: 'ReputationEvent') -> None:
        """
        Set reputation of a given type towards a given entity, with a specific
        change reason.

        <p>The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.

        <p>Note: this will fire a
        {@link org.bukkit.event.entity.VillagerReputationChangeEvent}.

        @param uuid the UUID of the entity for whom the reputation is being
                     added
        @param reputation_type reputation type to be modified
        @param amount amount of reputation to add
        @param change_reason reputation change reason
        """
        ...

    def set_gossip_decay_time(self, ticks: int) -> None:
        """
        Sets the reputation decay time for this villager.

        <p>Defaults to <b>24000</b> (1 daylight cycle).

        @param ticks amount of ticks until the villager's reputation decays
        """
        ...

    def get_gossip_decay_time(self) -> int:
        """
        Gets the reputation decay time for this villager.

        <p>Defaults to <b>24000</b> (1 daylight cycle).

        @return amount of ticks until the villager's reputation decays
        """
        ...


class Type(OldEnum['Type'], Keyed, RegistryAware, Protocol):
    DESERT: 'Type'
    JUNGLE: 'Type'
    PLAINS: 'Type'
    SAVANNA: 'Type'
    SNOW: 'Type'
    SWAMP: 'Type'
    TAIGA: 'Type'

        @staticmethod
    def get_type(key: str) -> 'Type':
        """
        @param key the key of the villager type
        @return the villager type with the given key
        """
        ...

        def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...

        @staticmethod
    def value_of(name: str) -> 'Type':
        """
        @param name of the villager type.
        @return the villager type with the given name.
        @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
        """
        ...

        @staticmethod
    def values() -> list['Type']:
        """
        @return an array of all known villager types.
        @deprecated use {@link Registry#iterator()}.
        """
        ...


class Profession(OldEnum['Profession'], Keyed, RegistryAware, Protocol):
    NONE: 'Profession'
    ARMORER: 'Profession'
    BUTCHER: 'Profession'
    CARTOGRAPHER: 'Profession'
    CLERIC: 'Profession'
    FARMER: 'Profession'
    FISHERMAN: 'Profession'
    FLETCHER: 'Profession'
    LEATHERWORKER: 'Profession'
    LIBRARIAN: 'Profession'
    MASON: 'Profession'
    NITWIT: 'Profession'
    SHEPHERD: 'Profession'
    TOOLSMITH: 'Profession'
    WEAPONSMITH: 'Profession'

        @staticmethod
    def get_profession(key: str) -> 'Profession':
        """
        @param key the key of the villager profession
        @return the villager profession with the given key
        """
        ...

        def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...

        @staticmethod
    def value_of(name: str) -> 'Profession':
        """
        @param name of the villager profession.
        @return the villager profession with the given name.
        @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
        """
        ...

        @staticmethod
    def values() -> list['Profession']:
        """
        @return an array of all known villager professions.
        @deprecated use {@link Registry#iterator()}.
        """
        ...


class ReputationType(Protocol):
    MAJOR_NEGATIVE: 'ReputationType'
    MINOR_NEGATIVE: 'ReputationType'
    MINOR_POSITIVE: 'ReputationType'
    MAJOR_POSITIVE: 'ReputationType'
    TRADING: 'ReputationType'

    def get_max_value(self) -> int:
        """
        Get maximum reputation value of this type.
        @return maximum value of this reputation type
        """
        ...

    def get_weight(self) -> int:
        """
        Get weight of this reputation type.

        <p>When calculating total reputation of an entity, reputation of
        each type is multiplied by its weight.

        @return weight assigned to this reputation type
        """
        ...

    @staticmethod
    def get_reputation_type(key: str) -> 'ReputationType':
        """
        @param key the key of the reputation type
        @return the reputation type with the given key
        """
        ...


class ReputationEvent(Protocol):
    ZOMBIE_VILLAGER_CURED: 'ReputationEvent'
    TRADE: 'ReputationEvent'
    VILLAGER_HURT: 'ReputationEvent'
    VILLAGER_KILLED: 'ReputationEvent'
    GOSSIP: 'ReputationEvent'
    DECAY: 'ReputationEvent'
    GOLEM_KILLED: 'ReputationEvent'
    UNSPECIFIED: 'ReputationEvent'

    @staticmethod
    def get_reputation_event(key: str) -> 'ReputationEvent':
        """
        @param key the key of the reputation event
        @return the reputation event with the given key
        """
        ...