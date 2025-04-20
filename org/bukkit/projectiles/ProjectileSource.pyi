from org.bukkit.entity import Projectile
from org.bukkit.util import Vector
from typing import Type, TypeVar, Optional

T = TypeVar('T', bound=Projectile)

class ProjectileSource:
    """
    Represents a valid source of a projectile.
    """

    def launch_projectile(self, projectile: Type[T]) -> T:
        """
        Launches a Projectile from the ProjectileSource.

        :param projectile: class of the projectile to launch
        :return: the launched projectile
        """
        ...

    def launch_projectile(self, projectile: Type[T], velocity: Optional[Vector]) -> T:
        """
        Launches a Projectile from the ProjectileSource with an
        initial velocity.

        :param projectile: class of the projectile to launch
        :param velocity: the velocity with which to launch
        :return: the launched projectile
        """
        ...