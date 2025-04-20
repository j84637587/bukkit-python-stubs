from org.bukkit.entity import Entity
from typing import Optional

class ShulkerBullet:
    """
    Interface representing a ShulkerBullet, which is a type of Projectile.
    """

    def get_target(self) -> Optional[Entity]:
        """
        Retrieve the target of this bullet.

        Returns:
            Optional[Entity]: the targeted entity
        """
        ...

    def set_target(self, target: Optional[Entity]) -> None:
        """
        Sets the target of this bullet.

        Args:
            target (Optional[Entity]): the entity to target
        """
        ...