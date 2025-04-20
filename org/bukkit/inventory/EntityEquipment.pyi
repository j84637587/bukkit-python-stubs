from typing import Optional, List

from org.bukkit.entity import Entity
from org.bukkit.entity import Mob
from org.jetbrains.annotations import NotNull, Nullable

class EquipmentSlot:
    pass

class ItemStack:
    pass

class EntityEquipment:
    """
    An interface to a creatures inventory
    """

    def set_item(self, slot: EquipmentSlot, item: Optional[ItemStack]) -> None:
        """
        Stores the ItemStack at the given equipment slot in the inventory.

        :param slot: the slot to put the ItemStack
        :param item: the ItemStack to set
        """
        ...

    def set_item(self, slot: EquipmentSlot, item: Optional[ItemStack], silent: bool) -> None:
        """
        Stores the ItemStack at the given equipment slot in the inventory.

        :param slot: the slot to put the ItemStack
        :param item: the ItemStack to set
        :param silent: whether or not the equip sound should be silenced
        """
        ...

        def get_item(self, slot: EquipmentSlot) -> ItemStack:
        """
        Gets the ItemStack at the given equipment slot in the inventory.

        :param slot: the slot to get the ItemStack
        :return: the ItemStack in the given slot
        """
        ...

        def get_item_in_main_hand(self) -> ItemStack:
        """
        Gets a copy of the item the entity is currently holding
        in their main hand.

        :return: the currently held item
        """
        ...

    def set_item_in_main_hand(self, item: Optional[ItemStack]) -> None:
        """
        Sets the item the entity is holding in their main hand.

        :param item: The item to put into the entities hand
        """
        ...

    def set_item_in_main_hand(self, item: Optional[ItemStack], silent: bool) -> None:
        """
        Sets the item the entity is holding in their main hand.

        :param item: The item to put into the entities hand
        :param silent: whether or not the equip sound should be silenced
        """
        ...

        def get_item_in_off_hand(self) -> ItemStack:
        """
        Gets a copy of the item the entity is currently holding
        in their off hand.

        :return: the currently held item
        """
        ...

    def set_item_in_off_hand(self, item: Optional[ItemStack]) -> None:
        """
        Sets the item the entity is holding in their off hand.

        :param item: The item to put into the entities hand
        """
        ...

    def set_item_in_off_hand(self, item: Optional[ItemStack], silent: bool) -> None:
        """
        Sets the item the entity is holding in their off hand.

        :param item: The item to put into the entities hand
        :param silent: whether or not the equip sound should be silenced
        """
        ...

    @Deprecated(since="1.9")
        def get_item_in_hand(self) -> ItemStack:
        """
        Gets a copy of the item the entity is currently holding

        :return: the currently held item
        :see: #get_item_in_main_hand()
        :see: #get_item_in_off_hand()
        :deprecated: entities can duel wield now use the methods for the
                      specific hand instead
        """
        ...

    @Deprecated(since="1.9")
    def set_item_in_hand(self, stack: Optional[ItemStack]) -> None:
        """
        Sets the item the entity is holding

        :param stack: The item to put into the entities hand
        :see: #set_item_in_main_hand(ItemStack)
        :see: #set_item_in_off_hand(ItemStack)
        :deprecated: entities can duel wield now use the methods for the
                      specific hand instead
        """
        ...

        def get_helmet(self) -> Optional[ItemStack]:
        """
        Gets a copy of the helmet currently being worn by the entity

        :return: The helmet being worn
        """
        ...

    def set_helmet(self, helmet: Optional[ItemStack]) -> None:
        """
        Sets the helmet worn by the entity

        :param helmet: The helmet to put on the entity
        """
        ...

    def set_helmet(self, helmet: Optional[ItemStack], silent: bool) -> None:
        """
        Sets the helmet worn by the entity

        :param helmet: The helmet to put on the entity
        :param silent: whether or not the equip sound should be silenced
        """
        ...

        def get_chestplate(self) -> Optional[ItemStack]:
        """
        Gets a copy of the chest plate currently being worn by the entity

        :return: The chest plate being worn
        """
        ...

    def set_chestplate(self, chestplate: Optional[ItemStack]) -> None:
        """
        Sets the chest plate worn by the entity

        :param chestplate: The chest plate to put on the entity
        """
        ...

    def set_chestplate(self, chestplate: Optional[ItemStack], silent: bool) -> None:
        """
        Sets the chest plate worn by the entity

        :param chestplate: The chest plate to put on the entity
        :param silent: whether or not the equip sound should be silenced
        """
        ...

        def get_leggings(self) -> Optional[ItemStack]:
        """
        Gets a copy of the leggings currently being worn by the entity

        :return: The leggings being worn
        """
        ...

    def set_leggings(self, leggings: Optional[ItemStack]) -> None:
        """
        Sets the leggings worn by the entity

        :param leggings: The leggings to put on the entity
        """
        ...

    def set_leggings(self, leggings: Optional[ItemStack], silent: bool) -> None:
        """
        Sets the leggings worn by the entity

        :param leggings: The leggings to put on the entity
        :param silent: whether or not the equip sound should be silenced
        """
        ...

        def get_boots(self) -> Optional[ItemStack]:
        """
        Gets a copy of the boots currently being worn by the entity

        :return: The boots being worn
        """
        ...

    def set_boots(self, boots: Optional[ItemStack]) -> None:
        """
        Sets the boots worn by the entity

        :param boots: The boots to put on the entity
        """
        ...

    def set_boots(self, boots: Optional[ItemStack], silent: bool) -> None:
        """
        Sets the boots worn by the entity

        :param boots: The boots to put on the entity
        :param silent: whether or not the equip sound should be silenced
        """
        ...

        def get_armor_contents(self) -> List[ItemStack]:
        """
        Gets all ItemStacks from the armor slots.

        :return: all the ItemStacks from the armor slots. Individual items can be
                 null and are returned in a fixed order starting from the boots and going
                 up to the helmet
        """
        ...

    def set_armor_contents(self, items: List[ItemStack]) -> None:
        """
        Sets the entities armor to the provided array of ItemStacks

        :param items: The items to set the armor as. Individual items may be null.
        """
        ...

    def clear(self) -> None:
        """
        Clears the entity of all armor and held items
        """
        ...

    @Deprecated(since="1.9")
    def get_item_in_hand_drop_chance(self) -> float:
        """
        @return: drop chance
        @see: #get_item_in_main_hand_drop_chance()
        @see: #get_item_in_off_hand_drop_chance()
        @deprecated: entities can duel wield now use the methods for the specific
                      hand instead
        """
        ...

    @Deprecated(since="1.9")
    def set_item_in_hand_drop_chance(self, chance: float) -> None:
        """
        @param chance: drop chance
        @see: #set_item_in_main_hand_drop_chance(float)
        @see: #set_item_in_off_hand_drop_chance(float)
        @deprecated: entities can duel wield now use the methods for the specific
                      hand instead
        """
        ...

    def get_item_in_main_hand_drop_chance(self) -> float:
        """
        Gets the chance of the main hand item being dropped upon this creature's
        death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @return: chance of the currently held item being dropped (1 for non-{@link Mob})
        """
        ...

    def set_item_in_main_hand_drop_chance(self, chance: float) -> None:
        """
        Sets the chance of the item this creature is currently holding in their
        main hand being dropped upon this creature's death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @param chance: the chance of the main hand item being dropped
        @raises: UnsupportedOperationException when called on non-{@link Mob}
        """
        ...

    def get_item_in_off_hand_drop_chance(self) -> float:
        """
        Gets the chance of the off hand item being dropped upon this creature's
        death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @return: chance of the off hand item being dropped (1 for non-{@link Mob})
        """
        ...

    def set_item_in_off_hand_drop_chance(self, chance: float) -> None:
        """
        Sets the chance of the off hand item being dropped upon this creature's
        death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @param chance: the chance of off hand item being dropped
        @raises: UnsupportedOperationException when called on non-{@link Mob}
        """
        ...

    def get_helmet_drop_chance(self) -> float:
        """
        Gets the chance of the helmet being dropped upon this creature's death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @return: the chance of the helmet being dropped (1 for non-{@link Mob})
        """
        ...

    def set_helmet_drop_chance(self, chance: float) -> None:
        """
        Sets the chance of the helmet being dropped upon this creature's death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @param chance: of the helmet being dropped
        @raises: UnsupportedOperationException when called on non-{@link Mob}
        """
        ...

    def get_chestplate_drop_chance(self) -> float:
        """
        Gets the chance of the chest plate being dropped upon this creature's
        death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @return: the chance of the chest plate being dropped (1 for non-{@link Mob})
        """
        ...

    def set_chestplate_drop_chance(self, chance: float) -> None:
        """
        Sets the chance of the chest plate being dropped upon this creature's
        death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @param chance: of the chest plate being dropped
        @raises: UnsupportedOperationException when called on non-{@link Mob}
        """
        ...

    def get_leggings_drop_chance(self) -> float:
        """
        Gets the chance of the leggings being dropped upon this creature's
        death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @return: the chance of the leggings being dropped (1 for non-{@link Mob})
        """
        ...

    def set_leggings_drop_chance(self, chance: float) -> None:
        """
        Sets the chance of the leggings being dropped upon this creature's
        death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @param chance: chance of the leggings being dropped
        @raises: UnsupportedOperationException when called on non-{@link Mob}
        """
        ...

    def get_boots_drop_chance(self) -> float:
        """
        Gets the chance of the boots being dropped upon this creature's death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @return: the chance of the boots being dropped (1 for non-{@link Mob})
        """
        ...

    def set_boots_drop_chance(self, chance: float) -> None:
        """
        Sets the chance of the boots being dropped upon this creature's death.

        <ul>
        <li>A drop chance of 0.0F will never drop
        <li>A drop chance of 1.0F will always drop
        </ul>

        @param chance: of the boots being dropped
        @raises: UnsupportedOperationException when called on non-{@link Mob}
        """
        ...

        def get_holder(self) -> Optional[Entity]:
        """
        Get the entity this EntityEquipment belongs to

        :return: the entity this EntityEquipment belongs to
        """
        ...