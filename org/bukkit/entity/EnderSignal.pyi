from org.bukkit.Location import Location
from org.bukkit.inventory.ItemStack import ItemStack
from typing import Optional

class EnderSignal(Entity):
    """
    Represents an EnderSignal, which is created upon throwing an ender eye.
    """

    def get_target_location(self) -> Location:
        """
        Get the location this EnderSignal is moving towards.

        Returns:
            Location: the Location this EnderSignal is moving towards.
        """
        ...

    def set_target_location(self, location: Location) -> None:
        """
        Set the Location this EnderSignal is moving towards.
        When setting a new target location, the getDropItem() resets to
        a random value and the despawn timer gets set back to 0.

        Args:
            location (Location): the new target location
        """
        ...

    def get_drop_item(self) -> bool:
        """
        Gets if the EnderSignal should drop an item on death.
        If true, it will drop an item. If false, it will shatter.

        Returns:
            bool: true if the EnderSignal will drop an item on death, or false if it will shatter
        """
        ...

    def set_drop_item(self, drop: bool) -> None:
        """
        Sets if the EnderSignal should drop an item on death; or if it should shatter.

        Args:
            drop (bool): true if the EnderSignal should drop an item on death, or false if it should shatter.
        """
        ...

    def get_item(self) -> ItemStack:
        """
        Get the ItemStack to be displayed while in the air and to be dropped on death.

        Returns:
            ItemStack: the item stack
        """
        ...

    def set_item(self, item: Optional[ItemStack]) -> None:
        """
        Set the ItemStack to be displayed while in the air and to be dropped on death.

        Args:
            item (Optional[ItemStack]): the item to set. If None, resets to the default eye of ender
        """
        ...

    def get_despawn_timer(self) -> int:
        """
        Gets the amount of time this entity has been alive (in ticks).
        When this number is greater than 80, it will despawn on the next tick.

        Returns:
            int: the number of ticks this EnderSignal has been alive.
        """
        ...

    def set_despawn_timer(self, timer: int) -> None:
        """
        Set how long this entity has been alive (in ticks).
        When this number is greater than 80, it will despawn on the next tick.

        Args:
            timer (int): how long (in ticks) this EnderSignal has been alive.
        """
        ...