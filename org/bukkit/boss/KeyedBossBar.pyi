from org.bukkit.boss import BossBar
from org.bukkit import Keyed

class KeyedBossBar(BossBar, Keyed):
    """Represents a custom :class:`BossBar` that has a
    :class:`org.bukkit.NamespacedKey`
    """
    pass