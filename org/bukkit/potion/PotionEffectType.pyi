from typing import Optional, List
from org.bukkit import Color, Keyed, NamespacedKey, Registry, Translatable, RegistryAware
from org.jetbrains.annotations import NotNull, Nullable, Contract

"""
Represents a type of potion and its effect on an entity.
"""
class PotionEffectType(Keyed, Translatable, RegistryAware):
    ID_MAP: 'BiMap[int, PotionEffectType]' = HashBiMap.create()

    """
    Increases movement speed.
    """
    SPEED: 'PotionEffectType' = getPotionEffectType(1, "speed")

    """
    Decreases movement speed.
    """
    SLOWNESS: 'PotionEffectType' = getPotionEffectType(2, "slowness")

    """
    Increases dig speed.
    """
    HASTE: 'PotionEffectType' = getPotionEffectType(3, "haste")

    """
    Decreases dig speed.
    """
    MINING_FATIGUE: 'PotionEffectType' = getPotionEffectType(4, "mining_fatigue")

    """
    Increases damage dealt.
    """
    STRENGTH: 'PotionEffectType' = getPotionEffectType(5, "strength")

    """
    Heals an entity.
    """
    INSTANT_HEALTH: 'PotionEffectType' = getPotionEffectType(6, "instant_health")

    """
    Hurts an entity.
    """
    INSTANT_DAMAGE: 'PotionEffectType' = getPotionEffectType(7, "instant_damage")

    """
    Increases jump height.
    """
    JUMP_BOOST: 'PotionEffectType' = getPotionEffectType(8, "jump_boost")

    """
    Warps vision on the client.
    """
    NAUSEA: 'PotionEffectType' = getPotionEffectType(9, "nausea")

    """
    Regenerates health.
    """
    REGENERATION: 'PotionEffectType' = getPotionEffectType(10, "regeneration")

    """
    Decreases damage dealt to an entity.
    """
    RESISTANCE: 'PotionEffectType' = getPotionEffectType(11, "resistance")

    """
    Stops fire damage.
    """
    FIRE_RESISTANCE: 'PotionEffectType' = getPotionEffectType(12, "fire_resistance")

    """
    Allows breathing underwater.
    """
    WATER_BREATHING: 'PotionEffectType' = getPotionEffectType(13, "water_breathing")

    """
    Grants invisibility.
    """
    INVISIBILITY: 'PotionEffectType' = getPotionEffectType(14, "invisibility")

    """
    Blinds an entity.
    """
    BLINDNESS: 'PotionEffectType' = getPotionEffectType(15, "blindness")

    """
    Allows an entity to see in the dark.
    """
    NIGHT_VISION: 'PotionEffectType' = getPotionEffectType(16, "night_vision")

    """
    Increases hunger.
    """
    HUNGER: 'PotionEffectType' = getPotionEffectType(17, "hunger")

    """
    Decreases damage dealt by an entity.
    """
    WEAKNESS: 'PotionEffectType' = getPotionEffectType(18, "weakness")

    """
    Deals damage to an entity over time.
    """
    POISON: 'PotionEffectType' = getPotionEffectType(19, "poison")

    """
    Deals damage to an entity over time and gives the health to the
    shooter.
    """
    WITHER: 'PotionEffectType' = getPotionEffectType(20, "wither")

    """
    Increases the maximum health of an entity.
    """
    HEALTH_BOOST: 'PotionEffectType' = getPotionEffectType(21, "health_boost")

    """
    Increases the maximum health of an entity with health that cannot be
    regenerated, but is refilled every 30 seconds.
    """
    ABSORPTION: 'PotionEffectType' = getPotionEffectType(22, "absorption")

    """
    Increases the food level of an entity each tick.
    """
    SATURATION: 'PotionEffectType' = getPotionEffectType(23, "saturation")

    """
    Outlines the entity so that it can be seen from afar.
    """
    GLOWING: 'PotionEffectType' = getPotionEffectType(24, "glowing")

    """
    Causes the entity to float into the air.
    """
    LEVITATION: 'PotionEffectType' = getPotionEffectType(25, "levitation")

    """
    Loot table luck.
    """
    LUCK: 'PotionEffectType' = getPotionEffectType(26, "luck")

    """
    Loot table unluck.
    """
    UNLUCK: 'PotionEffectType' = getPotionEffectType(27, "unluck")

    """
    Slows entity fall rate.
    """
    SLOW_FALLING: 'PotionEffectType' = getPotionEffectType(28, "slow_falling")

    """
    Effects granted by a nearby conduit. Includes enhanced underwater abilities.
    """
    CONDUIT_POWER: 'PotionEffectType' = getPotionEffectType(29, "conduit_power")

    """
    Increses underwater movement speed.<br>
    Squee'ek uh'k kk'kkkk squeek eee'eek.
    """
    DOLPHINS_GRACE: 'PotionEffectType' = getPotionEffectType(30, "dolphins_grace")

    """
    Triggers an ominous event when the player enters a village or trial chambers.<br>
    oof.
    """
    BAD_OMEN: 'PotionEffectType' = getPotionEffectType(31, "bad_omen")

    """
    Reduces the cost of villager trades.<br>
    \o/.
    """
    HERO_OF_THE_VILLAGE: 'PotionEffectType' = getPotionEffectType(32, "hero_of_the_village")

    """
    Causes the player's vision to dim occasionally.
    """
    DARKNESS: 'PotionEffectType' = getPotionEffectType(33, "darkness")

    """
    Causes trial spawners to become ominous.
    """
    TRIAL_OMEN: 'PotionEffectType' = getPotionEffectType(34, "trial_omen")

    """
    Triggers a raid when a player enters a village.
    """
    RAID_OMEN: 'PotionEffectType' = getPotionEffectType(35, "raid_omen")

    """
    Emits a wind burst upon death.
    """
    WIND_CHARGED: 'PotionEffectType' = getPotionEffectType(36, "wind_charged")

    """
    Creates cobwebs upon death.
    """
    WEAVING: 'PotionEffectType' = getPotionEffectType(37, "weaving")

    """
    Causes slimes to spawn upon death.
    """
    OOZING: 'PotionEffectType' = getPotionEffectType(38, "oozing")

    """
    Chance of spawning silverfish when hurt.
    """
    INFESTED: 'PotionEffectType' = getPotionEffectType(39, "infested")

        @staticmethod
    def getPotionEffectType(typeId: int, key: str) -> 'PotionEffectType':
        potionEffectType: 'PotionEffectType' = Registry.EFFECT.getOrThrow(NamespacedKey.minecraft(key))

        if typeId > 0:
            PotionEffectType.ID_MAP.put(typeId, potionEffectType)
        return potionEffectType

    """
    Creates a PotionEffect from this PotionEffectType, applying duration
    modifiers and checks.

    @param duration time in ticks
    @param amplifier the effect's amplifier
    @return a resulting potion effect
    @see PotionBrewer#createEffect(PotionEffectType, int, int)
    """
        def createEffect(self, duration: int, amplifier: int) -> 'PotionEffect':
        ...

    """
    Returns whether the effect of this type happens once, immediately.

    @return whether this type is normally instant
    """
    def isInstant(self) -> bool:
        ...

    """
    Returns the {@link PotionEffectTypeCategory category} of this effect type.

    @return the category
    """
        def getCategory(self) -> 'PotionEffectTypeCategory':
        ...

    """
    Returns the color of this effect type.

    @return the color
    """
        def getColor(self) -> Color:
        ...

    """
    {@inheritDoc}

    @see #getKeyOrThrow()
    @see #isRegistered()
    @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
    """
        @Deprecated(since="1.21.4")
    def getKey(self) -> NamespacedKey:
        ...

    """
    Returns the duration modifier applied to effects of this type.

    @return duration modifier
    @deprecated unused, always 1.0
    """
    @Deprecated(since="1.14")
    def getDurationModifier(self) -> float:
        ...

    """
    Returns the unique ID of this type.

    @return Unique ID
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def getId(self) -> int:
        ...

    """
    Returns the name of this effect type.

    @return The name of this effect type
    @deprecated only for backwards compatibility, use {@link #getKey()} instead.
    """
        @Deprecated(since="1.20.3")
    def getName(self) -> str:
        ...

    """
    Gets the PotionEffectType at the specified key

    @param key key to fetch
    @return Resulting PotionEffectType, or null if not found
    @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
    """
    @Contract("null -> null")
        @Deprecated(since="1.20.3")
    @staticmethod
    def getByKey(key: Optional[NamespacedKey]) -> Optional['PotionEffectType']:
        ...

    """
    Gets the effect type specified by the unique id.

    @param id Unique ID to fetch
    @return Resulting type, or null if not found.
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
        @staticmethod
    def getById(id: int) -> Optional['PotionEffectType']:
        ...

    """
    Gets the effect type specified by the given name.

    @param name Name of PotionEffectType to fetch
    @return Resulting PotionEffectType, or null if not found.
    @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
    """
        @Deprecated(since="1.20.3")
    @staticmethod
    def getByName(name: str) -> Optional['PotionEffectType']:
        ...

    """
    @return an array of all known PotionEffectTypes.
    @deprecated use {@link Registry#iterator()}.
    """
        @Deprecated(since="1.20.3")
    @staticmethod
    def values() -> List['PotionEffectType']:
        ...