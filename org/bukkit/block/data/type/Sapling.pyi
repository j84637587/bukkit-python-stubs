from org.bukkit.block.data import BlockData

class Sapling(BlockData):
    """
    'stage' represents the growth stage of a sapling.
    <br>
    When the sapling reaches {@link #getMaximumStage()} it will attempt to grow
    into a tree as the next stage.
    """

    def get_stage(self) -> int:
        """
        Gets the value of the 'stage' property.

        @return: the 'stage' value
        """
        ...

    def set_stage(self, stage: int) -> None:
        """
        Sets the value of the 'stage' property.

        @param stage: the new 'stage' value
        """
        ...

    def get_maximum_stage(self) -> int:
        """
        Gets the maximum allowed value of the 'stage' property.

        @return: the maximum 'stage' value
        """
        ...