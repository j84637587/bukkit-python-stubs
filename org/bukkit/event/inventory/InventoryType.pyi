from typing import Optional, Literal
from org.bukkit.inventory import InventoryHolder
from org.bukkit.inventory import MenuType
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

class InventoryType:
    """
    Represents the different kinds of inventories available in Bukkit.
    <br>
    Only InventoryTypes marked {@link #isCreatable()} can be created.
    <br>
    The current list of inventories that cannot be created via
    {@link org.bukkit.Bukkit#createInventory} are:<br>
    <blockquote>
        {@link InventoryType#CREATIVE}, {@link InventoryType#CRAFTING} and
        {@link InventoryType#MERCHANT}
    </blockquote>

    See {@link org.bukkit.Bukkit#createInventory} for more information.

    @see org.bukkit.Bukkit#createInventory(InventoryHolder, InventoryType)
    """

    CHEST: "InventoryType"
    DISPENSER: "InventoryType"
    DROPPER: "InventoryType"
    FURNACE: "InventoryType"
    WORKBENCH: "InventoryType"
    CRAFTING: "InventoryType"
    ENCHANTING: "InventoryType"
    BREWING: "InventoryType"
    PLAYER: "InventoryType"
    CREATIVE: "InventoryType"
    MERCHANT: "InventoryType"
    ENDER_CHEST: "InventoryType"
    ANVIL: "InventoryType"
    SMITHING: "InventoryType"
    BEACON: "InventoryType"
    HOPPER: "InventoryType"
    SHULKER_BOX: "InventoryType"
    BARREL: "InventoryType"
    BLAST_FURNACE: "InventoryType"
    LECTERN: "InventoryType"
    SMOKER: "InventoryType"
    LOOM: "InventoryType"
    CARTOGRAPHY: "InventoryType"
    GRINDSTONE: "InventoryType"
    STONECUTTER: "InventoryType"
    COMPOSTER: "InventoryType"
    CHISELED_BOOKSHELF: "InventoryType"
    JUKEBOX: "InventoryType"
    DECORATED_POT: "InventoryType"
    CRAFTER: "InventoryType"
    SMITHING_NEW: "InventoryType"

    def __init__(self, default_size: int, default_title: str, menu_type: Optional[MenuType], is_creatable: bool = True) -> None:
        ...

    def get_default_size(self) -> int:
        ...

        def get_default_title(self) -> str:
        ...

        def get_menu_type(self) -> Optional[MenuType]:
        ...

    def is_creatable(self) -> bool:
        ...

class SlotType:
    """
    Slot types for inventories.
    """
    RESULT: Literal['RESULT']
    CRAFTING: Literal['CRAFTING']
    ARMOR: Literal['ARMOR']
    CONTAINER: Literal['CONTAINER']
    QUICKBAR: Literal['QUICKBAR']
    OUTSIDE: Literal['OUTSIDE']
    FUEL: Literal['FUEL']