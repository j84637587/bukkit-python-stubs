from typing import Dict
from org.bukkit.block import Block
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.inventory import InventoryEvent
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull

"""
Called when an ItemStack is successfully enchanted (currently at
enchantment table)
"""
class EnchantItemEvent(InventoryEvent, Cancellable):
    handlers: HandlerList

    def __init__(self, enchanter: Player, view: InventoryView, table: Block, item: ItemStack, level: int, enchants: Dict[Enchantment, int], enchantment_hint: Enchantment, level_hint: int, i: int) -> None:
        ...

    """
    Gets the player enchanting the item

    @return enchanting player
    """
        def get_enchanter(self) -> Player:
        ...

    """
    Gets the block being used to enchant the item

    @return the block used for enchanting
    """
        def get_enchant_block(self) -> Block:
        ...

    """
    Gets the item to be enchanted (can be modified)

    @return ItemStack of item
    """
        def get_item(self) -> ItemStack:
        ...

    """
    Gets the cost (minimum level) which is displayed as a number on the right
    hand side of the enchantment offer.

    @return experience level cost
    """
    def get_exp_level_cost(self) -> int:
        ...

    """
    Sets the cost (minimum level) which is displayed as a number on the right
    hand side of the enchantment offer.

    @param level - cost in levels
    """
    def set_exp_level_cost(self, level: int) -> None:
        ...

    """
    Get map of enchantment (levels, keyed by type) to be added to item
    (modify map returned to change values). Note: Any enchantments not
    allowed for the item will be ignored

    @return map of enchantment levels, keyed by enchantment
    """
        def get_enchants_to_add(self) -> Dict[Enchantment, int]:
        ...

    """
    Get the {@link Enchantment} that was displayed as a hint to the player
    on the selected enchantment offer.

    @return the hinted enchantment
    """
        def get_enchantment_hint(self) -> Enchantment:
        ...

    """
    Get the level of the enchantment that was displayed as a hint to the
    player on the selected enchantment offer.

    @return the level of the hinted enchantment
    """
    def get_level_hint(self) -> int:
        ...

    """
    Which button was pressed to initiate the enchanting.

    @return The button index (0, 1, or 2).
    """
    def which_button(self) -> int:
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...