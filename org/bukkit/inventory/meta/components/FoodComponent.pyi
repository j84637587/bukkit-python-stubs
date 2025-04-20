from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory.meta.components.consumable import ConsumableComponent
from org.jetbrains.annotations import ApiStatus
from typing import Protocol

class FoodComponent(Protocol[ConfigurationSerializable]):
    """Represents a component which can handle food stats in any item.
    <br>
    <b>Note:</b> Items with food stats has no effect unless the item can be
    consumed, see {@link ConsumableComponent}.
    """

    def get_nutrition(self) -> int:
        """Gets the food restored by this item when eaten.

        Returns:
            nutrition value
        """
        ...

    def set_nutrition(self, nutrition: int) -> None:
        """Sets the food restored by this item when eaten.

        Args:
            nutrition: new nutrition value, must be non-negative
        """
        ...

    def get_saturation(self) -> float:
        """Gets the saturation restored by this item when eaten.

        Returns:
            saturation value
        """
        ...

    def set_saturation(self, saturation: float) -> None:
        """Sets the saturation restored by this item when eaten.

        Args:
            saturation: new saturation value
        """
        ...

    def can_always_eat(self) -> bool:
        """Gets if this item can be eaten even when not hungry.

        Returns:
            true if always edible
        """
        ...

    def set_can_always_eat(self, can_always_eat: bool) -> None:
        """Sets if this item can be eaten even when not hungry.

        Args:
            can_always_eat: whether always edible
        """
        ...
