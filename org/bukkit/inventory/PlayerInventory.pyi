from org.bukkit.entity import HumanEntity
from typing import List, Optional
from org.jetbrains.annotations import NotNull, Nullable

"""
Interface to the inventory of a Player, including the four armor slots and any extra slots.
"""
class PlayerInventory(Inventory):

    """
    Gets all ItemStacks from the armor slots.

    @return all the ItemStacks from the armor slots. Individual items can be
    null and are returned in a fixed order starting from the boots and going
    up to the helmet
    """
        def getArmorContents(self) -> List[Optional[ItemStack]]:
        ...

    """
    Get all additional ItemStacks stored in this inventory.
    <br>
    NB: What defines an extra slot is up to the implementation, however it
    will not be contained within {@link #getStorageContents()} or
    {@link #getArmorContents()}

    @return All additional ItemStacks. Individual items can be null.
    """
        def getExtraContents(self) -> List[Optional[ItemStack]]:
        ...

    """
    Return the ItemStack from the helmet slot

    @return The ItemStack in the helmet slot
    """
        def getHelmet(self) -> Optional[ItemStack]:
        ...

    """
    Return the ItemStack from the chestplate slot

    @return The ItemStack in the chestplate slot
    """
        def getChestplate(self) -> Optional[ItemStack]:
        ...

    """
    Return the ItemStack from the leg slot

    @return The ItemStack in the leg slot
    """
        def getLeggings(self) -> Optional[ItemStack]:
        ...

    """
    Return the ItemStack from the boots slot

    @return The ItemStack in the boots slot
    """
        def getBoots(self) -> Optional[ItemStack]:
        ...

    """
    Stores the ItemStack at the given index of the inventory.
    <p>
    Indexes 0 through 8 refer to the hotbar. 9 through 35 refer to the main inventory, counting up from 9 at the top
    left corner of the inventory, moving to the right, and moving to the row below it back on the left side when it
    reaches the end of the row. It follows the same path in the inventory like you would read a book.
    <p>
    Indexes 36 through 39 refer to the armor slots. Though you can set armor with this method using these indexes,
    you are encouraged to use the provided methods for those slots.
    <p>
    Index 40 refers to the off hand (shield) item slot. Though you can set off hand with this method using this index,
    you are encouraged to use the provided method for this slot.
    <p>
    If you attempt to use this method with an index less than 0 or greater than 40, an ArrayIndexOutOfBounds
    exception will be thrown.

    @param index The index where to put the ItemStack
    @param item The ItemStack to set
    @throws ArrayIndexOutOfBoundsException when index < 0 || index > 40
    @see #setBoots(ItemStack)
    @see #setChestplate(ItemStack)
    @see #setHelmet(ItemStack)
    @see #setLeggings(ItemStack)
    @see #setItemInOffHand(ItemStack)
    """
    @Override
    def setItem(self, index: int, item: Optional[ItemStack]) -> None:
        ...

    """
    Stores the ItemStack at the given equipment slot in the inventory.

    @param slot the slot to put the ItemStack
    @param item the ItemStack to set

    @see #setItem(int, ItemStack)
    """
    def setItem(self, slot: NotNull EquipmentSlot, item: Optional[ItemStack]) -> None:
        ...

    """
    Gets the ItemStack at the given equipment slot in the inventory.

    @param slot the slot to get the ItemStack

    @return the ItemStack in the given slot or null if there is not one
    """
        def getItem(self, slot: NotNull EquipmentSlot) -> Optional[ItemStack]:
        ...

    """
    Put the given ItemStacks into the armor slots

    @param items The ItemStacks to use as armour
    """
    def setArmorContents(self, items: Optional[List[ItemStack]]) -> None:
        ...

    """
    Put the given ItemStacks into the extra slots
    <br>
    See {@link #getExtraContents()} for an explanation of extra slots.

    @param items The ItemStacks to use as extra
    """
    def setExtraContents(self, items: Optional[List[ItemStack]]) -> None:
        ...

    """
    Put the given ItemStack into the helmet slot. This does not check if
    the ItemStack is a helmet

    @param helmet The ItemStack to use as helmet
    """
    def setHelmet(self, helmet: Optional[ItemStack]) -> None:
        ...

    """
    Put the given ItemStack into the chestplate slot. This does not check
    if the ItemStack is a chestplate

    @param chestplate The ItemStack to use as chestplate
    """
    def setChestplate(self, chestplate: Optional[ItemStack]) -> None:
        ...

    """
    Put the given ItemStack into the leg slot. This does not check if the
    ItemStack is a pair of leggings

    @param leggings The ItemStack to use as leggings
    """
    def setLeggings(self, leggings: Optional[ItemStack]) -> None:
        ...

    """
    Put the given ItemStack into the boots slot. This does not check if the
    ItemStack is a boots

    @param boots The ItemStack to use as boots
    """
    def setBoots(self, boots: Optional[ItemStack]) -> None:
        ...

    """
    Gets a copy of the item the player is currently holding
    in their main hand.

    @return the currently held item
    """
        def getItemInMainHand(self) -> ItemStack:
        ...

    """
    Sets the item the player is holding in their main hand.

    @param item The item to put into the player's hand
    """
    def setItemInMainHand(self, item: Optional[ItemStack]) -> None:
        ...

    """
    Gets a copy of the item the player is currently holding
    in their off hand.

    @return the currently held item
    """
        def getItemInOffHand(self) -> ItemStack:
        ...

    """
    Sets the item the player is holding in their off hand.

    @param item The item to put into the player's hand
    """
    def setItemInOffHand(self, item: Optional[ItemStack]) -> None:
        ...

    """
    Gets a copy of the item the player is currently holding

    @return the currently held item
    @see #getItemInMainHand()
    @see #getItemInOffHand()
    @deprecated players can duel wield now use the methods for the
        specific hand instead
    """
    @Deprecated(since="1.9")
        def getItemInHand(self) -> ItemStack:
        ...

    """
    Sets the item the player is holding

    @param stack The item to put into the player's hand
    @see #setItemInMainHand(ItemStack)
    @see #setItemInOffHand(ItemStack)
    @deprecated players can duel wield now use the methods for the
        specific hand instead
    """
    @Deprecated(since="1.9")
    def setItemInHand(self, stack: Optional[ItemStack]) -> None:
        ...

    """
    Get the slot number of the currently held item

    @return Held item slot number
    """
    def getHeldItemSlot(self) -> int:
        ...

    """
    Set the slot number of the currently held item.
    <p>
    This validates whether the slot is between 0 and 8 inclusive.

    @param slot The new slot number
    @throws IllegalArgumentException Thrown if slot is not between 0 and 8
        inclusive
    """
    def setHeldItemSlot(self, slot: int) -> None:
        ...

    @Override
        def getHolder(self) -> Optional[HumanEntity]:
        ...