from org.bukkit import Bukkit
from org.bukkit import NamespacedKey
from org.bukkit import Tag
from org.bukkit.damage import DamageType
from org.jetbrains.annotations import ApiStatus
from org.jetbrains.annotations import Nullable

"""
Vanilla {@link DamageType} {@link Tag tags}.
"""
class DamageTypeTags:
    """
    Vanilla tag representing damage types which damage helmets.
    """
    DAMAGES_HELMET: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which bypass armor.
    """
    BYPASSES_ARMOR: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which bypass shields.
    """
    BYPASSES_SHIELD: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which bypass invulnerability.
    """
    BYPASSES_INVULNERABILITY: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which bypass cooldowns.
    <br>
    <b>Note:</b> this can be null unless a datapack add values to this tag because vanilla not has any values for this.
    """
    BYPASSES_COOLDOWN: Nullable[Tag[DamageType]] = ...

    """
    Vanilla tag representing damage types which bypass effects.
    """
    BYPASSES_EFFECTS: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which bypass resistance.
    """
    BYPASSES_RESISTANCE: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which bypass enchantments.
    """
    BYPASSES_ENCHANTMENTS: Tag[DamageType] = ...

    """
    Vanilla tag representing all fire damage types.
    """
    IS_FIRE: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which originate from projectiles.
    """
    IS_PROJECTILE: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which witches are resistant to.
    """
    WITCH_RESISTANT_TO: Tag[DamageType] = ...

    """
    Vanilla tag representing all explosion damage types.
    """
    IS_EXPLOSION: Tag[DamageType] = ...

    """
    Vanilla tag representing all fall damage types.
    """
    IS_FALL: Tag[DamageType] = ...

    """
    Vanilla tag representing all drowning damage types.
    """
    IS_DROWNING: Tag[DamageType] = ...

    """
    Vanilla tag representing all freezing damage types.
    """
    IS_FREEZING: Tag[DamageType] = ...

    """
    Vanilla tag representing all lightning damage types.
    """
    IS_LIGHTNING: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which do not cause entities to anger.
    """
    NO_ANGER: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which do not cause an impact.
    """
    NO_IMPACT: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which cause maximum fall damage.
    """
    ALWAYS_MOST_SIGNIFICANT_FALL: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which withers are immune to.
    """
    WITHER_IMMUNE_TO: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which ignite armor stands.
    """
    IGNITES_ARMOR_STANDS: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which burn armor stands.
    """
    BURNS_ARMOR_STANDS: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which avoid guardian thorn damage.
    """
    AVOIDS_GUARDIAN_THORNS: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which always trigger silverfish.
    """
    ALWAYS_TRIGGERS_SILVERFISH: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which always hurt enderdragons.
    """
    ALWAYS_HURTS_ENDER_DRAGONS: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which do not cause knockback.
    """
    NO_KNOCKBACK: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which always kill armor stands.
    """
    ALWAYS_KILLS_ARMOR_STANDS: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which can break armor stands.
    """
    CAN_BREAK_ARMOR_STAND: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which bypass wolf armor.
    """
    BYPASSES_WOLF_ARMOR: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which are from player attacks.
    """
    IS_PLAYER_ATTACK: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which originate from hot blocks.
    """
    BURN_FROM_STEPPING: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which cause entities to panic.
    """
    PANIC_CAUSES: Tag[DamageType] = ...

    """
    Vanilla tag representing environmental damage types which cause entities to panic.
    """
    PANIC_ENVIRONMENTAL_CAUSES: Tag[DamageType] = ...

    """
    Vanilla tag representing damage types which originate from mace smashes.
    """
    IS_MACE_SMASH: Tag[DamageType] = ...

    """
    Internal use only.
    """
    REGISTRY_DAMAGE_TYPES: str = "damage_types"

    @staticmethod
        def getTag(key: str) -> Nullable[Tag[DamageType]]:
        ...

    def __init__(self) -> None:
        ...