from typing import Optional
from uuid import UUID
from org.bukkit.inventory import ItemStack
from org.bukkit.entity import Entity

"""
Represents a dropped item.
"""
class Item(Entity):

    """
    Gets the item stack associated with this item drop.

    @return An item stack.
    """
    def get_item_stack(self) -> ItemStack: ...

    """
    Sets the item stack associated with this item drop.

    @param stack An item stack.
    """
    def set_item_stack(self, stack: ItemStack) -> None: ...

    """
    Gets the delay before this Item is available to be picked up by players.

    @return Remaining delay
    """
    def get_pickup_delay(self) -> int: ...

    """
    Sets the delay before this Item is available to be picked up by players.

    @param delay New delay
    """
    def set_pickup_delay(self, delay: int) -> None: ...

    """
    Sets if this Item should live forever.

    @param unlimited true if the lifetime is unlimited
    """
    def set_unlimited_lifetime(self, unlimited: bool) -> None: ...

    """
    Gets if this Item lives forever.

    @return true if the lifetime is unlimited
    """
    def is_unlimited_lifetime(self) -> bool: ...

    """
    Sets the owner of this item.

    Other entities will not be able to pickup this item when an owner is set.

    @param owner UUID of new owner
    """
    def set_owner(self, owner: Optional[UUID]) -> None: ...

    """
    Get the owner of this item.

    @return UUID of owner
    """
    def get_owner(self) -> Optional[UUID]: ...

    """
    Set the thrower of this item.

    The thrower is the entity which dropped the item. This affects the
    trigger criteria for item pickups, for things such as advancements.

    @param uuid UUID of thrower
    """
    def set_thrower(self, uuid: Optional[UUID]) -> None: ...

    """
    Get the thrower of this item.

    The thrower is the entity which dropped the item.

    @return UUID of thrower
    """
    def get_thrower(self) -> Optional[UUID]: ...