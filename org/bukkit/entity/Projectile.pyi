from org.bukkit.entity import Entity
from org.bukkit.projectiles import ProjectileSource
from typing import Optional

class Projectile(Entity):
    """
    Represents a shootable entity.
    """

    def get_shooter(self) -> Optional[ProjectileSource]:
        """
        Retrieve the shooter of this projectile.

        :return: the {@link ProjectileSource} that shot this projectile
        """
        ...

    def set_shooter(self, source: Optional[ProjectileSource]) -> None:
        """
        Set the shooter of this projectile.

        :param source: the {@link ProjectileSource} that shot this projectile
        """
        ...

    def does_bounce(self) -> bool:
        """
        Determine if this projectile should bounce or not when it hits.

        :return: true if it should bounce.
        :deprecated: does not do anything
        """
        ...

    def set_bounce(self, does_bounce: bool) -> None:
        """
        Set whether or not this projectile should bounce or not when it hits
        something.

        :param does_bounce: whether or not it should bounce.
        :deprecated: does not do anything
        """
        ...