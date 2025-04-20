from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit.registry import RegistryAware
from org.jetbrains.annotations import ApiStatus
from org.jetbrains.annotations import NotNull
from typing import Protocol

class DamageType(Protocol, Keyed, Translatable, RegistryAware):
    """
    Represent a type of damage that an entity can receive.
    <p>
    Constants in this class include the base types provided by the vanilla
    server. Data packs are capable of registering more types of damage which may
    be obtained through the {@link Registry#DAMAGE_TYPE}.

    @see <a href="https://minecraft.wiki/w/Damage_type">Minecraft Wiki</a>
    """

    IN_FIRE: "DamageType"
    CAMPFIRE: "DamageType"
    LIGHTNING_BOLT: "DamageType"
    ON_FIRE: "DamageType"
    LAVA: "DamageType"
    HOT_FLOOR: "DamageType"
    IN_WALL: "DamageType"
    CRAMMING: "DamageType"
    DROWN: "DamageType"
    STARVE: "DamageType"
    CACTUS: "DamageType"
    FALL: "DamageType"
    ENDER_PEARL: "DamageType"
    FLY_INTO_WALL: "DamageType"
    OUT_OF_WORLD: "DamageType"
    GENERIC: "DamageType"
    MAGIC: "DamageType"
    WITHER: "DamageType"
    DRAGON_BREATH: "DamageType"
    DRY_OUT: "DamageType"
    SWEET_BERRY_BUSH: "DamageType"
    FREEZE: "DamageType"
    STALAGMITE: "DamageType"
    FALLING_BLOCK: "DamageType"
    FALLING_ANVIL: "DamageType"
    FALLING_STALACTITE: "DamageType"
    STING: "DamageType"
    MOB_ATTACK: "DamageType"
    MOB_ATTACK_NO_AGGRO: "DamageType"
    PLAYER_ATTACK: "DamageType"
    ARROW: "DamageType"
    TRIDENT: "DamageType"
    MOB_PROJECTILE: "DamageType"
    SPIT: "DamageType"
    FIREWORKS: "DamageType"
    FIREBALL: "DamageType"
    UNATTRIBUTED_FIREBALL: "DamageType"
    WITHER_SKULL: "DamageType"
    THROWN: "DamageType"
    INDIRECT_MAGIC: "DamageType"
    THORNS: "DamageType"
    EXPLOSION: "DamageType"
    PLAYER_EXPLOSION: "DamageType"
    SONIC_BOOM: "DamageType"
    BAD_RESPAWN_POINT: "DamageType"
    OUTSIDE_BORDER: "DamageType"
    GENERIC_KILL: "DamageType"
    WIND_CHARGE: "DamageType"
    MACE_SMASH: "DamageType"

    @staticmethod
        def getDamageType(key: str) -> "DamageType":
        """
        Get the DamageType associated with the given key.
        """
        ...

        def getTranslationKey(self) -> str:
        """
        {@inheritDoc}
        <p>
        The returned key is that of the death message sent when this damage type
        is responsible for the death of an entity.
        <p>
        <strong>Note</strong> This translation key is only used if
        {@link #getDeathMessageType()} is {@link DeathMessageType#DEFAULT}
        """
        ...

        def getDamageScaling(self) -> "DamageScaling":
        """
        Get the {@link DamageScaling} for this damage type.

        @return the damage scaling
        """
        ...

        def getDamageEffect(self) -> "DamageEffect":
        """
        Get the {@link DamageEffect} for this damage type.

        @return the damage effect
        """
        ...

        def getDeathMessageType(self) -> "DeathMessageType":
        """
        Get the {@link DeathMessageType} for this damage type.

        @return the death message type
        """
        ...

    def getExhaustion(self) -> float:
        """
        Get the amount of hunger exhaustion caused by this damage type.

        @return the exhaustion
        """
        ...

        @Deprecated(since="1.21.4")
    def getKey(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...