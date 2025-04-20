from org.bukkit.entity import Fireball

class WitherSkull(Fireball):
    """
    Represents a wither skull {@link Fireball}.
    """

    def set_charged(self, charged: bool) -> None:
        """
        Sets the charged status of the wither skull.

        :param charged: whether it should be charged
        """
        ...

    def is_charged(self) -> bool:
        """
        Gets whether or not the wither skull is charged.

        :return: whether the wither skull is charged
        """
        ...