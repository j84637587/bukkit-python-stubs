from typing import Optional
from org.bukkit import Keyed, Bukkit, NamespacedKey

class FeatureFlag(Keyed):
    """
    This represents a Feature Flag for a World.
    Flags which are unavailable in the current version will be null and/or
    removed.
    """
    VANILLA: Optional[FeatureFlag] = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("vanilla"))

    """
    AVAILABLE BETWEEN VERSIONS: 1.19.3 - 1.21.1
    @deprecated not available since 1.21.2
    """
    BUNDLE: Optional[FeatureFlag] = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("bundle"))

    """
    AVAILABLE BETWEEN VERSIONS: 1.19 - 1.19.4
    @deprecated not available since 1.20
    """
    UPDATE_1_20: Optional[FeatureFlag] = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("update_1_20"))

    TRADE_REBALANCE: Optional[FeatureFlag] = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("trade_rebalance"))

    """
    AVAILABLE BETWEEN VERSIONS: 1.20.5 - 1.20.6
    @deprecated not available since 1.21
    """
    UPDATE_121: Optional[FeatureFlag] = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("update_1_21"))

    """
    AVAILABLE BETWEEN VERSIONS: 1.21.2 - 1.21.3
    @deprecated not available since 1.21.4
    """
    WINTER_DROP: Optional[FeatureFlag] = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("winter_drop"))

    REDSTONE_EXPERIMENTS: Optional[FeatureFlag] = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("redstone_experiments"))

    MINECART_IMPROVEMENTS: Optional[FeatureFlag] = Bukkit.getUnsafe().getFeatureFlag(NamespacedKey.minecraft("minecart_improvements"))