from org.bukkit.block.data import AnaloguePowerable

"""
'inverted' denotes whether this daylight detector is in the inverted mode,
i.e. activates in the absence of light rather than presence.
"""
class DaylightDetector(AnaloguePowerable):
    """
    Gets the value of the 'inverted' property.

    @return: the 'inverted' value
    """
    def is_inverted(self) -> bool: ...

    """
    Sets the value of the 'inverted' property.

    @param inverted: the new 'inverted' value
    """
    def set_inverted(self, inverted: bool) -> None: ...