from typing import List
from org.bukkit.potion import PotionEffect
from org.jetbrains.annotations import NotNull

"""
Represent the effects applied when an item is consumed.
"""
class ConsumableApplyEffects:

    """
    Gets the effects which may be applied by this item when consumed.

    @return consumable effects
    """
        def getEffects(self) -> List[PotionEffect]: ...

    """
    Sets the effects which may be applied by this item when consumed.

    @param effects new effects
    """
    def setEffects(self, effects: List[PotionEffect]) -> None: ...

    """
    Adds an effect which may be applied by this item when consumed.

    @param effect the effect
    @return the added effect
    """
        def addEffect(self, effect: PotionEffect) -> PotionEffect: ...

    """
    Gets the probability of this effect being applied.

    @return probability
    """
    def getProbability(self) -> float: ...

    """
    Sets the probability of this effect being applied.

    @param probability between 0 and 1 inclusive.
    """
    def setProbability(self, probability: float) -> None: ...