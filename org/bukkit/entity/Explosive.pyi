from org.bukkit.entity import Entity

class Explosive(Entity):
    """
    A representation of an explosive entity
    """

    def set_yield(self, yield: float) -> None:
        """
        Set the radius affected by this explosive's explosion.
        <br>
        This is the base yield, which may be affected by other entity attributes.

        :param yield: The explosive yield
        """
        ...

    def get_yield(self) -> float:
        """
        Return the radius or yield of this explosive's explosion.
        <br>
        This is the base yield, which may be affected by other entity attributes.

        :return: the radius of blocks affected
        """
        ...

    def set_is_incendiary(self, is_incendiary: bool) -> None:
        """
        Set whether or not this explosive's explosion causes fire

        :param is_incendiary: Whether it should cause fire
        """
        ...

    def is_incendiary(self) -> bool:
        """
        Return whether or not this explosive creates a fire when exploding

        :return: true if the explosive creates fire, false otherwise
        """
        ...