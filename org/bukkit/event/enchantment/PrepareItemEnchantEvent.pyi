from org.bukkit.block import Block
from org.bukkit.enchantments import EnchantmentOffer
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.inventory import InventoryEvent
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory.view import EnchantmentView
from typing import List

class PrepareItemEnchantEvent(InventoryEvent, Cancellable):
    """
    Called when an ItemStack is inserted in an enchantment table - can be
    called multiple times
    """
    
    handlers: HandlerList

    def __init__(self, enchanter: Player, view: EnchantmentView, table: Block, item: ItemStack, offers: List[EnchantmentOffer], bonus: int) -> None:
        ...

    def get_enchanter(self) -> Player:
        """
        Gets the player enchanting the item

        :return: enchanting player
        """
        ...

    def get_enchant_block(self) -> Block:
        """
        Gets the block being used to enchant the item

        :return: the block used for enchanting
        """
        ...

    def get_item(self) -> ItemStack:
        """
        Gets the item to be enchanted.

        :return: ItemStack of item
        """
        ...

    def get_exp_level_costs_offered(self) -> List[int]:
        """
        Get a list of offered experience level costs of the enchantment.

        :return: experience level costs offered
        :deprecated: Use get_offers() instead of this method
        """
        ...

    def get_offers(self) -> List[EnchantmentOffer]:
        """
        Get a list of available EnchantmentOffer for the player. You can
        modify the values to change the available offers for the player. An offer
        may be null, if there isn't a enchantment offer at a specific slot. There
        are 3 slots in the enchantment table available to modify.

        :return: list of available enchantment offers
        """
        ...

    def get_enchantment_bonus(self) -> int:
        """
        Get enchantment bonus in effect - corresponds to number of bookshelves

        :return: enchantment bonus
        """
        ...

    def get_view(self) -> EnchantmentView:
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