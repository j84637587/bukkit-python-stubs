from org.bukkit import DyeColor
from org.jetbrains.annotations import Nullable

class ShieldMeta(BannerMeta):
    """
    Interface for ShieldMeta.
    """

        def get_base_color(self) -> DyeColor:
        """
        Gets the base color for this shield.

        Returns:
            the base color or null
        """
        ...

    def set_base_color(self, color: Nullable[DyeColor]) -> None:
        """
        Sets the base color for this shield.
        Note: If the shield contains a
        Pattern, then a null base color will
        retain the pattern but default the base color to DyeColor.WHITE.

        Args:
            color: the base color or null
        """
        ...