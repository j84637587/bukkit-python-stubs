from typing import Optional

class Damageable(ItemMeta):
    """
    Represents an item that has durability and can take damage.
    """

    def has_damage(self) -> bool:
        """
        Checks to see if this item has damage

        :return: true if this has damage
        """
        ...

    def get_damage(self) -> int:
        """
        Gets the damage

        :return: the damage
        """
        ...

    def set_damage(self, damage: int) -> None:
        """
        Sets the damage

        :param damage: item damage
        """
        ...

    def has_max_damage(self) -> bool:
        """
        Checks to see if this item has a maximum amount of damage.

        :return: true if this has maximum amount of damage
        """
        ...

    def get_max_damage(self) -> int:
        """
        Gets the maximum amount of damage.
        Plugins should check has_max_damage() before calling this method.

        :return: the maximum amount of damage
        """
        ...

    def set_max_damage(self, max_damage: Optional[int]) -> None:
        """
        Sets the maximum amount of damage.

        :param max_damage: maximum amount of damage
        """
        ...

    def clone(self) -> 'Damageable':
        ...