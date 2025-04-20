from typing import Collection, Optional
from org.bukkit import Keyed

class Advancement(Keyed):
    """
    Represents an advancement that may be awarded to a player. This class is not
    reference safe as the underlying advancement may be reloaded.
    """

    def get_criteria(self) -> Collection[str]:
        """
        Get all the criteria present in this advancement.

        Returns:
            a unmodifiable copy of all criteria
        """
        ...

    def get_requirements(self) -> "AdvancementRequirements":
        """
        Returns the requirements for this advancement.

        Returns:
            an AdvancementRequirements object.
        """
        ...

    def get_display(self) -> Optional["AdvancementDisplay"]:
        """
        Returns the display information for this advancement.

        This includes its name, description and other visible tags.

        Returns:
            a AdvancementDisplay object, or None if not set.
        """
        ...
