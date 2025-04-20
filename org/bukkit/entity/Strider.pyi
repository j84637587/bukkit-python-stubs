from org.bukkit.entity import Steerable, Vehicle

class Strider(Steerable, Vehicle):
    """
    Represents a Strider.
    """

    def is_shivering(self) -> bool:
        """
        Check whether or not this strider is out of warm blocks and shivering.

        :return: true if shivering, false otherwise
        """
        ...

    def set_shivering(self, shivering: bool) -> None:
        """
        Set whether or not this strider is shivering.

        Note that the shivering state is updated frequently on the server,
        therefore this method may not affect the entity for long enough to have a
        noticeable difference.

        :param shivering: its new shivering state
        """
        ...