from org.bukkit import NamespacedKey
from org.jetbrains.annotations import ApiStatus
from org.jetbrains.annotations import Nullable

"""
A ItemFlag can hide some Attributes from ItemStacks
"""
class ItemFlag:
    """
    Setting to show/hide enchants
    """
    HIDE_ENCHANTS: 'ItemFlag'

    """
    Setting to show/hide Attributes like Damage
    """
    HIDE_ATTRIBUTES: 'ItemFlag'

    """
    Setting to show/hide the unbreakable State
    """
    HIDE_UNBREAKABLE: 'ItemFlag'

    """
    Setting to show/hide what the ItemStack can break/destroy
    """
    HIDE_DESTROYS: 'ItemFlag'

    """
    Setting to show/hide where this ItemStack can be build/placed on
    """
    HIDE_PLACED_ON: 'ItemFlag'

    """
    Setting to show/hide potion effects, book and firework information, map
    tooltips, patterns of banners, and enchantments of enchanted books.
    """
    HIDE_ADDITIONAL_TOOLTIP: 'ItemFlag'

    """
    Setting to show/hide dyes from colored leather armor.
    """
    HIDE_DYE: 'ItemFlag'

    """
    Setting to show/hide armor trim from leather armor.
    """
    HIDE_ARMOR_TRIM: 'ItemFlag'

        HIDE_CUSTOM_DATA: 'ItemFlag'

        HIDE_MAX_STACK_SIZE: 'ItemFlag'

        HIDE_MAX_DAMAGE: 'ItemFlag'

        HIDE_DAMAGE: 'ItemFlag'

        HIDE_CUSTOM_NAME: 'ItemFlag'

        HIDE_ITEM_NAME: 'ItemFlag'

        HIDE_ITEM_MODEL: 'ItemFlag'

        HIDE_LORE: 'ItemFlag'

        HIDE_RARITY: 'ItemFlag'

        HIDE_ENCHANTMENTS: 'ItemFlag'

        HIDE_CAN_PLACE_ON: 'ItemFlag'

        HIDE_CAN_BREAK: 'ItemFlag'

        HIDE_ATTRIBUTE_MODIFIERS: 'ItemFlag'

        HIDE_CUSTOM_MODEL_DATA: 'ItemFlag'

        HIDE_TOOLTIP_DISPLAY: 'ItemFlag'

        HIDE_REPAIR_COST: 'ItemFlag'

        HIDE_CREATIVE_SLOT_LOCK: 'ItemFlag'

        HIDE_ENCHANTMENT_GLINT_OVERRIDE: 'ItemFlag'

        HIDE_INTANGIBLE_PROJECTILE: 'ItemFlag'

        HIDE_FOOD: 'ItemFlag'

        HIDE_CONSUMABLE: 'ItemFlag'

        HIDE_USE_REMAINDER: 'ItemFlag'

        HIDE_USE_COOLDOWN: 'ItemFlag'

        HIDE_DAMAGE_RESISTANT: 'ItemFlag'

        HIDE_TOOL: 'ItemFlag'

        HIDE_WEAPON: 'ItemFlag'

        HIDE_ENCHANTABLE: 'ItemFlag'

        HIDE_EQUIPPABLE: 'ItemFlag'

        HIDE_REPAIRABLE: 'ItemFlag'

        HIDE_GLIDER: 'ItemFlag'

        HIDE_TOOLTIP_STYLE: 'ItemFlag'

        HIDE_DEATH_PROTECTION: 'ItemFlag'

        HIDE_BLOCKS_ATTACKS: 'ItemFlag'

        HIDE_STORED_ENCHANTMENTS: 'ItemFlag'

        HIDE_DYED_COLOR: 'ItemFlag'

        HIDE_MAP_COLOR: 'ItemFlag'

        HIDE_MAP_ID: 'ItemFlag'

        HIDE_MAP_DECORATIONS: 'ItemFlag'

        HIDE_MAP_POST_PROCESSING: 'ItemFlag'

        HIDE_CHARGED_PROJECTILES: 'ItemFlag'

        HIDE_BUNDLE_CONTENTS: 'ItemFlag'

        HIDE_POTION_CONTENTS: 'ItemFlag'

        HIDE_POTION_DURATION_SCALE: 'ItemFlag'

        HIDE_SUSPICIOUS_STEW_EFFECTS: 'ItemFlag'

        HIDE_WRITABLE_BOOK_CONTENT: 'ItemFlag'

        HIDE_WRITTEN_BOOK_CONTENT: 'ItemFlag'

        HIDE_TRIM: 'ItemFlag'

        HIDE_DEBUG_STICK_STATE: 'ItemFlag'

        HIDE_ENTITY_DATA: 'ItemFlag'

        HIDE_BUCKET_ENTITY_DATA: 'ItemFlag'

        HIDE_BLOCK_ENTITY_DATA: 'ItemFlag'

        HIDE_INSTRUMENT: 'ItemFlag'

        HIDE_PROVIDES_TRIM_MATERIAL: 'ItemFlag'

        HIDE_OMINOUS_BOTTLE_AMPLIFIER: 'ItemFlag'

        HIDE_JUKEBOX_PLAYABLE: 'ItemFlag'

        HIDE_PROVIDES_BANNER_PATTERNS: 'ItemFlag'

        HIDE_RECIPES: 'ItemFlag'

        HIDE_LODESTONE_TRACKER: 'ItemFlag'

        HIDE_FIREWORK_EXPLOSION: 'ItemFlag'

        HIDE_FIREWORKS: 'ItemFlag'

        HIDE_PROFILE: 'ItemFlag'

        HIDE_NOTE_BLOCK_SOUND: 'ItemFlag'

        HIDE_BANNER_PATTERNS: 'ItemFlag'

        HIDE_BASE_COLOR: 'ItemFlag'

        HIDE_POT_DECORATIONS: 'ItemFlag'

        HIDE_CONTAINER: 'ItemFlag'

        HIDE_BLOCK_STATE: 'ItemFlag'

        HIDE_BEES: 'ItemFlag'

        HIDE_LOCK: 'ItemFlag'

        HIDE_CONTAINER_LOOT: 'ItemFlag'

        HIDE_BREAK_SOUND: 'ItemFlag'

        HIDE_VILLAGER_VARIANT: 'ItemFlag'

        HIDE_WOLF_VARIANT: 'ItemFlag'

        HIDE_WOLF_SOUND_VARIANT: 'ItemFlag'

        HIDE_WOLF_COLLAR: 'ItemFlag'

        HIDE_FOX_VARIANT: 'ItemFlag'

        HIDE_SALMON_SIZE: 'ItemFlag'

        HIDE_PARROT_VARIANT: 'ItemFlag'

        HIDE_TROPICAL_FISH_PATTERN: 'ItemFlag'

        HIDE_TROPICAL_FISH_BASE_COLOR: 'ItemFlag'

        HIDE_TROPICAL_FISH_PATTERN_COLOR: 'ItemFlag'

        HIDE_MOOSHROOM_VARIANT: 'ItemFlag'

        HIDE_RABBIT_VARIANT: 'ItemFlag'

        HIDE_PIG_VARIANT: 'ItemFlag'

        HIDE_COW_VARIANT: 'ItemFlag'

        HIDE_CHICKEN_VARIANT: 'ItemFlag'

        HIDE_FROG_VARIANT: 'ItemFlag'

        HIDE_HORSE_VARIANT: 'ItemFlag'

        HIDE_PAINTING_VARIANT: 'ItemFlag'

        HIDE_LLAMA_VARIANT: 'ItemFlag'

        HIDE_AXOLOTL_VARIANT: 'ItemFlag'

        HIDE_CAT_VARIANT: 'ItemFlag'

        HIDE_CAT_COLLAR: 'ItemFlag'

        HIDE_SHEEP_COLOR: 'ItemFlag'

        HIDE_SHULKER_COLOR: 'ItemFlag'

    def __init__(self: 'ItemFlag', component: str = None) -> None:
        ...

            def get_component(self: 'ItemFlag') -> NamespacedKey:
        ...