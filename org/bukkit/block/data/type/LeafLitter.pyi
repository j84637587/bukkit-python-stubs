from org.bukkit.block.data import Directional

class LeafLitter(Directional):
    """
    'segment_amount' represents the number of segments.
    """

    def get_segment_amount(self) -> int:
        """
        Gets the value of the 'segment_amount' property.

        @return: the 'segment_amount' value
        """
        ...

    def set_segment_amount(self, segment_amount: int) -> None:
        """
        Sets the value of the 'segment_amount' property.

        @param segment_amount: the new 'segment_amount' value
        """
        ...

    def get_maximum_segment_amount(self) -> int:
        """
        Gets the maximum allowed value of the 'segment_amount' property.

        @return: the maximum 'segment_amount' value
        """
        ...