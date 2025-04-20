from typing import Collection, Optional
from .nameable import Nameable
from .living_entity import LivingEntity
from .potion_effect import PotionEffect
from .potion_effect_type import PotionEffectType
from .tile_state import TileState
from .lockable import Lockable

class Beacon(TileState, Lockable, Nameable):
    """
    Represents a captured state of a beacon.
    """

    def get_entities_in_range(self) -> Collection[LivingEntity]:
        """
        Returns the list of players within the beacon's range of effect.
        This will return an empty list if the block represented by this state is
        no longer a beacon.

        @return: the players in range
        @raises IllegalStateException: if this block state is not placed
        """
        ...

    def get_tier(self) -> int:
        """
        Returns the tier of the beacon pyramid (0-4). The tier refers to the
        beacon's power level, based on how many layers of blocks are in the
        pyramid. Tier 1 refers to a beacon with one layer of 9 blocks under it.

        @return: the beacon tier
        """
        ...

    def get_primary_effect(self) -> Optional[PotionEffect]:
        """
        Returns the primary effect set on the beacon.

        @return: the primary effect or None if not set
        """
        ...

    def set_primary_effect(self, effect: Optional[PotionEffectType]) -> None:
        """
        Set the primary effect on this beacon, or None to clear.

        @param effect: new primary effect
        """
        ...

    def get_secondary_effect(self) -> Optional[PotionEffect]:
        """
        Returns the secondary effect set on the beacon.

        @return: the secondary effect or None if no secondary effect
        """
        ...

    def set_secondary_effect(self, effect: Optional[PotionEffectType]) -> None:
        """
        Set the secondary effect on this beacon, or None to clear. Note that tier
        must be >= 4 for this effect to be active.

        @param effect: desired secondary effect
        """
        ...