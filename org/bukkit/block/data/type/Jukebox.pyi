from org.bukkit.block.data import BlockData

class Jukebox(BlockData):
    """
    'has_record' is a quick flag to check whether this jukebox has a record
    inside it.
    """

    def has_record(self) -> bool:
        """
        Gets the value of the 'has_record' property.

        @return: the 'has_record' value
        """
        ...