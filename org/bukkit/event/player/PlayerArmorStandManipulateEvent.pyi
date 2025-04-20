from org.bukkit.entity import ArmorStand
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any

class PlayerArmorStandManipulateEvent(PlayerInteractEntityEvent):
    """
    Called when a player interacts with an armor stand and will either swap, retrieve or
    place an item.
    """

    handlers: HandlerList

    def __init__(self, who: Player, clicked_entity: ArmorStand, player_item: ItemStack, armor_stand_item: ItemStack, slot: EquipmentSlot, hand: EquipmentSlot) -> None:
        ...

    @classmethod
    def deprecated_init(cls, who: Player, clicked_entity: ArmorStand, player_item: ItemStack, armor_stand_item: ItemStack, slot: EquipmentSlot) -> None:
        ...

    def get_player_item(self) -> ItemStack:
        """
        Returns the item held by the player.
        <p>
        If this item is empty and the armor stand item is also empty, there will be no
        transaction between the player and the armor stand. If the player's item is empty
        but the armor stand item is not, the player's item will be placed on the armor
        stand. If both items are not empty, the items will be swapped.
        <p>
        In the case that this event is cancelled, the original items will remain the same.
        @return: the item held by the player.
        """
        ...

    def get_armor_stand_item(self) -> ItemStack:
        """
        Returns the item held by the armor stand.
        <p>
        If this item is empty and the player's item is also empty, there will be no
        transaction between the player and the armor stand. If the player's item is empty
        but the armor stand item is not, then the player will obtain the armor stand item.
        In the case that the player's item is not empty but the armor stand item is empty,
        the player's item will be placed on the armor stand. If both items are not empty,
        the items will be swapped.
        <p>
        In the case that the event is cancelled the original items will remain the same.
        @return: the item held by the armor stand.
        """
        ...

    def get_slot(self) -> EquipmentSlot:
        """
        Returns the raw item slot of the armor stand in this event.
        
        @return: the index of the item obtained or placed of the armor stand.
        """
        ...

    def get_hand(self) -> EquipmentSlot:
        """
        {@inheritDoc}
        <p>
        Note that this is not the hand of the armor stand that was changed, but rather
        the hand used by the player to swap items with the armor stand.
        """
        ...

    def get_right_clicked(self) -> ArmorStand:
        ...
    
    def get_handlers(self) -> HandlerList:
        ...

    @classmethod
    def get_handler_list(cls) -> HandlerList:
        ...