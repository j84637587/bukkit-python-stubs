from org.bukkit.block.data import Directional

class EndPortalFrame(Directional):
    """
    'eye' denotes whether this end portal frame has been activated by having an
    eye of ender placed in it.
    """

    def has_eye(self) -> bool:
        """
        Gets the value of the 'eye' property.

        :return: the 'eye' value
        """
        ...

    def set_eye(self, eye: bool) -> None:
        """
        Sets the value of the 'eye' property.

        :param eye: the new 'eye' value
        """
        ...