from org.bukkit.potion import PotionEffectType
from typing import Any

class PotionEffectTypeWrapper(PotionEffectType):
    """
    @deprecated only for backwards compatibility, PotionEffectTypeWrapper is no longer used.
    """
    
    def __init__(self) -> None:
        """
        Initializes a new instance of PotionEffectTypeWrapper.
        """
        ...

    def get_type(self) -> PotionEffectType:
        """
        Get the potion type bound to this wrapper.

        Returns:
            The potion effect type
        """
        ...