from org.bukkit.block.data import Waterlogged

class Scaffolding(Waterlogged):
    """
    'bottom' indicates whether the scaffolding is floating or not.
    <br>
    'distance' indicates the distance from a scaffolding block placed above a
    'bottom' scaffold.
    <br>
    When 'distance' reaches {@link #getMaximumDistance()} the block will drop.
    """

    def is_bottom(self) -> bool:
        """
        Gets the value of the 'bottom' property.

        :return: the 'bottom' value
        """
        ...

    def set_bottom(self, bottom: bool) -> None:
        """
        Sets the value of the 'bottom' property.

        :param bottom: the new 'bottom' value
        """
        ...

    def get_distance(self) -> int:
        """
        Gets the value of the 'distance' property.

        :return: the 'distance' value
        """
        ...

    def set_distance(self, distance: int) -> None:
        """
        Sets the value of the 'distance' property.

        :param distance: the new 'distance' value
        """
        ...

    def get_maximum_distance(self) -> int:
        """
        Gets the maximum allowed value of the 'distance' property.

        :return: the maximum 'distance' value
        """
        ...