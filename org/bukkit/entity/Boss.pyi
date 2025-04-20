from org.bukkit.boss import BossBar
from typing import Optional

class Boss(Entity):
    """
    Represents the Boss Entity.
    """

    def get_boss_bar(self) -> Optional[BossBar]:
        """
        Returns the BossBar of the Boss

        Returns:
            the BossBar of the entity
        """
        ...