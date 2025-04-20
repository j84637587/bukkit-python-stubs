from typing import Optional
from org.bukkit.Location import Location

"""
A crystal that heals nearby EnderDragons
"""
class EnderCrystal(Entity):
    """
    Return whether or not this end crystal is showing the
    bedrock slate underneath it.

    @return true if the bottom is being shown
    """
    def is_showing_bottom(self) -> bool: ...

    """
    Sets whether or not this end crystal is showing the
    bedrock slate underneath it.

    @param showing whether the bedrock slate should be shown
    """
    def set_showing_bottom(self, showing: bool) -> None: ...

    """
    Gets the location that this end crystal is pointing its beam to.

    @return the location that the beam is pointed to, or null if the beam is not shown
    """
    def get_beam_target(self) -> Optional[Location]: ...

    """
    Sets the location that this end crystal is pointing to. Passing a null
    value will remove the current beam.

    @param location the location to point the beam to
    @throws IllegalArgumentException for differing worlds
    """
    def set_beam_target(self, location: Optional[Location]) -> None: ...