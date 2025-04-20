from typing import Optional
from uuid import UUID
from org.bukkit.Material import Material
from org.bukkit.inventory.ItemStack import ItemStack

"""
Represents an Animal.
"""
class Animals(Breedable):

    """
    Get the UUID of the entity that caused this entity to enter the
    {@link #canBreed()} state.

    @return uuid if set, or None
    """
    def get_breed_cause(self) -> Optional[UUID]: ...

    """
    Set the UUID of the entity that caused this entity to enter the
    {@link #canBreed()} state.

    @param uuid new uuid, or None
    """
    def set_breed_cause(self, uuid: Optional[UUID]) -> None: ...

    """
    Get whether or not this entity is in love mode and will produce
    offspring with another entity in love mode. Will return True if
    and only if {@link #getLoveModeTicks()} is greater than 0.

    @return True if in love mode, False otherwise
    """
    def is_love_mode(self) -> bool: ...

    """
    Get the amount of ticks remaining for this entity in love mode.
    If the entity is not in love mode, 0 will be returned.

    @return the remaining love mode ticks
    """
    def get_love_mode_ticks(self) -> int: ...

    """
    Set the amount of ticks for which this entity should be in love mode.
    Setting the love mode ticks to 600 is the equivalent of a player
    feeding the entity their breeding item of choice.

    @param ticks the love mode ticks. Must be positive
    """
    def set_love_mode_ticks(self, ticks: int) -> None: ...

    """
    Check if the provided ItemStack is the correct item used for breeding
    this entity.

    @param stack ItemStack to check.
    @return if the provided ItemStack is the correct food item for this
    entity.
    """
    def is_breed_item(self, stack: ItemStack) -> bool: ...

    """
    Check if the provided ItemStack is the correct item used for breeding
    this entity.

    @param material Material to check.
    @return if the provided ItemStack is the correct food item for this
    entity.
    """
    def is_breed_item(self, material: Material) -> bool: ...