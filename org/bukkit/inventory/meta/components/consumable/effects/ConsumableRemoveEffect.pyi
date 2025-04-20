from typing import List
from org.bukkit.potion import PotionEffectType
from org.jetbrains.annotations import NotNull

"""
Represent the effects to be removed when an item is consumed.
"""
class ConsumableRemoveEffect:
    """
    Gets the effects which may be removed by this item when consumed.

    @return the effects
    """
        def get_effect_types(self) -> List[PotionEffectType]: ...

    """
    Sets the effects which may be removed by this item when consumed.

    @param effects new effects
    """
    def set_effect_types(self, effects: List[PotionEffectType]) -> None: ...

    """
    Adds an effect which may be applied by this item when consumed.

    @param effect the effect
    @return the added effect
    """
        def add_effect_type(self, effect: PotionEffectType) -> PotionEffectType: ...