from org.bukkit import NamespacedKey
from org.bukkit.configuration.serialization import ConfigurationSerializable
from typing import Optional

"""
Represents a component which determines the cooldown applied to use of this
item.
"""
class UseCooldownComponent(ConfigurationSerializable):
    """
    Gets the time in seconds it will take for an item in this cooldown group
    to be available to use again.

    @return cooldown time
    """
    def get_cooldown_seconds(self) -> float: ...

    """
    Sets the time in seconds it will take for an item in this cooldown group
    to be available to use again.

    @param cooldown new eat time, must be greater than 0
    """
    def set_cooldown_seconds(self, cooldown: float) -> None: ...

    """
    Gets the custom cooldown group to be used for similar items, if set.

    @return the cooldown group
    """
    def get_cooldown_group(self) -> Optional[NamespacedKey]: ...

    """
    Sets the custom cooldown group to be used for similar items.

    @param song the cooldown group
    """
    def set_cooldown_group(self, song: Optional[NamespacedKey]) -> None: ...