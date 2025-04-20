from org.bukkit.entity import Explosive
from org.bukkit.entity import Minecart

class ExplosiveMinecart(Minecart, Explosive):
    """
    Represents a Minecart with TNT inside it that can explode when triggered.
    """

    def set_fuse_ticks(self, ticks: int) -> None:
        """
        Set the fuse ticks of this minecart.

        If the fuse ticks are set to a non-zero value, this will ignite the
        explosive.

        :param ticks: the ticks
        """
        ...

    def get_fuse_ticks(self) -> int:
        """
        Get the fuse ticks of this minecart.

        If the fuse ticks reach 0, the minecart will explode.

        :return: the fuse ticks, or -1 if this minecart's fuse has not yet been
        ignited
        """
        ...

    def get_explosion_speed_factor(self) -> float:
        """
        Gets the factor by which explosion yield increases based on Minecart
        speed.

        :return: increase factor
        """
        ...

    def set_explosion_speed_factor(self, factor: float) -> None:
        """
        Sets the factor by which explosion yield increases based on Minecart
        speed.

        :param factor: new factor
        """
        ...

    def ignite(self) -> None:
        """
        Ignite this minecart's fuse naturally.
        """
        ...

    def is_ignited(self) -> bool:
        """
        Check whether or not this minecart's fuse has been ignited.

        :return: true if ignited, false otherwise
        """
        ...

    def explode(self) -> None:
        """
        Immediately explode this minecart with the power assumed by its current
        movement.
        """
        ...

    def explode(self, power: float) -> None:
        """
        Immediately explode this minecart with the given power.

        :param power: the power to use. Must be positive and cannot exceed 5.0
        """
        ...