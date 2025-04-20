from enum import Enum

class CreativeCategory(Enum):
    """
    Represents a category in the creative inventory.
    """
    BUILDING_BLOCKS = ...
    """
    An assortment of building blocks including dirt, bricks, planks, ores
    slabs, etc.
    """
    
    DECORATIONS = ...
    """
    Blocks and items typically used for decorative purposes including
    candles, saplings, flora, fauna, fences, walls, carpets, etc.
    """
    
    REDSTONE = ...
    """
    Blocks used and associated with redstone contraptions including buttons,
    levers, pressure plates, redstone components, pistons, etc.
    """
    
    TRANSPORTATION = ...
    """
    Items pertaining to transportation including minecarts, rails, boats,
    elytra, etc.
    """
    
    MISC = ...
    """
    Miscellaneous items and blocks that do not fit into other categories
    including gems, dyes, spawn eggs, discs, banner patterns, etc.
    """
    
    FOOD = ...
    """
    Food items consumable by the player including meats, berries, edible
    drops from creatures, etc.
    """
    
    TOOLS = ...
    """
    Equipment items meant for general utility including pickaxes, axes, hoes,
    flint and steel, and useful enchantment books for said tools.
    """
    
    COMBAT = ...
    """
    Equipment items meant for combat including armor, swords, bows, tipped
    arrows, and useful enchantment books for said equipment.
    """
    
    BREWING = ...
    """
    All items related to brewing and potions including all types of potions,
    their variants, and ingredients to brew them.
    """