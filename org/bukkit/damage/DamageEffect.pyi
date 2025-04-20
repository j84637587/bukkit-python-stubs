from typing import Protocol
from org.bukkit import Sound
from com.google.common.base import Preconditions
from org.bukkit import Bukkit
from org.jetbrains.annotations import ApiStatus, NotNull

class DamageEffect(Protocol):
    """
    Represents a type of effect that occurs when damage is inflicted. Currently,
    effects only determine the sound that plays.
    """

    HURT: 'DamageEffect'
    THORNS: 'DamageEffect'
    DROWNING: 'DamageEffect'
    BURNING: 'DamageEffect'
    POKING: 'DamageEffect'
    FREEZING: 'DamageEffect'

    @staticmethod
        def getDamageEffect(key: str) -> 'DamageEffect':
        """
        Get a DamageEffect by its key.

        :param key: The key for the DamageEffect
        :return: The DamageEffect
        """
        ...

        def getSound(self) -> Sound:
        """
        Get the Sound played for this DamageEffect.

        :return: the sound
        """
        ...