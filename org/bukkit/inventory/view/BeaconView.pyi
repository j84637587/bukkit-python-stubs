from org.bukkit.inventory import BeaconInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.potion import PotionEffectType
from typing import Optional

class BeaconView(InventoryView):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    beacon view data.
    """

    def get_top_inventory(self) -> BeaconInventory:
        """ 
        Retrieves the top inventory of the beacon view.
        """
        ...

    def get_tier(self) -> int:
        """
        Gets the tier of the beacon
        <p>
        Beacon tier is deduced by the height of the pyramid the beacon is
        standing on. The level of the beacon is 0 unless the beacon is activated.
        <p>
        @return The tier of the beacon
        """
        ...

    def get_primary_effect(self) -> Optional[PotionEffectType]:
        """
        Gets the primary effect of the beacon.
        <p>
        If the beacon level is high enough where the primary effect can be
        upgraded to level two, e.g. Speed 2. Instead of
        {@link #getSecondaryEffect()} being null it {@link #getSecondaryEffect()}
        returns the same {@link PotionEffectType} as this method.
        <p>
        @return The primary effect enabled on the beacon
        """
        ...

    def get_secondary_effect(self) -> Optional[PotionEffectType]:
        """
        Gets the secondary effect of the beacon.
        <p>
        If the beacon level is high enough where the primary effect can be
        upgraded to level two, e.g. Speed 2. The secondary effect will return the
        same effect as {@link #getPrimaryEffect()}.
        <p>
        @return The secondary effect enabled on the beacon
        """
        ...

    def set_primary_effect(self, effect: Optional[PotionEffectType]) -> None:
        """
        Sets the primary effect of the beacon, or null to clear
        <p>
        The {@link PotionEffectType} provided must be one that is already within
        the beacon as a valid option.
        <ol>
        <li>{@link PotionEffectType#SPEED}
        <li>{@link PotionEffectType#HASTE}
        <li>{@link PotionEffectType#RESISTANCE}
        <li>{@link PotionEffectType#JUMP_BOOST}
        <li>{@link PotionEffectType#STRENGTH}
        <li>{@link PotionEffectType#REGENERATION}
        </ol>
        <p>
        @param effect desired primary effect
        """
        ...

    def set_secondary_effect(self, effect: Optional[PotionEffectType]) -> None:
        """
        Sets the secondary effect on this beacon, or null to clear. Note that
        tier must be &gt;= 4 and a primary effect must be set in order for this
        effect to be active.
        <p>
        The {@link PotionEffectType} provided must be one that is already within
        the beacon as a valid option.
        <ol>
        <li>{@link PotionEffectType#SPEED}
        <li>{@link PotionEffectType#HASTE}
        <li>{@link PotionEffectType#RESISTANCE}
        <li>{@link PotionEffectType#JUMP_BOOST}
        <li>{@link PotionEffectType#STRENGTH}
        <li>{@link PotionEffectType#REGENERATION}
        </ol>
        <p>
        @param effect the desired secondary effect
        """
        ...