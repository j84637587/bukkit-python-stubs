from org.bukkit.entity import AbstractHorse

class ChestedHorse(AbstractHorse):
    """
    Represents Horse-like creatures which can carry an inventory.
    """

    def is_carrying_chest(self) -> bool:
        """
        Gets whether the horse has a chest equipped.

        :return: true if the horse has chest storage
        """
        ...

    def set_carrying_chest(self, chest: bool) -> None:
        """
        Sets whether the horse has a chest equipped. Removing a chest will also
        clear the chest's inventory.

        :param chest: true if the horse should have a chest
        """
        ...