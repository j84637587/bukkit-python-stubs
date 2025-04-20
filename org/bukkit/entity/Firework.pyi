from org.bukkit.entity import Projectile
from org.bukkit.inventory.meta import FireworkMeta
from typing import Optional

class Firework(Projectile):
    """
    Interface representing a Firework entity.
    """

    def get_firework_meta(self) -> FireworkMeta:
        """
        Get a copy of the fireworks meta.

        Returns:
            A copy of the current Firework meta.
        """
        ...

    def set_firework_meta(self, meta: FireworkMeta) -> None:
        """
        Apply the provided meta to the fireworks.

        Args:
            meta: The FireworkMeta to apply.
        """
        ...

    def set_attached_to(self, entity: Optional['LivingEntity']) -> bool:
        """
        Set the LivingEntity to which this firework is attached.

        When attached to an entity, the firework effect will act as normal but
        remain positioned on the entity. If the entity is gliding, then the entity
        will receive a boost in the direction that they are looking.

        Args:
            entity: the entity to which the firework should be attached, or
            None to remove the attached entity.

        Returns:
            True if the entity could be attached, False if the firework was
            already detonated.
        """
        ...

    def get_attached_to(self) -> Optional['LivingEntity']:
        """
        Get the LivingEntity to which this firework is attached.

        When attached to an entity, the firework effect will act as normal but
        remain positioned on the entity. If the entity is gliding, then the entity
        will receive a boost in the direction that they are looking.

        Returns:
            The attached entity, or None if none.
        """
        ...

    def set_life(self, ticks: int) -> bool:
        """
        Set the ticks that this firework has been alive. If this value exceeds
        getMaxLife(), the firework will detonate.

        Args:
            ticks: the ticks to set. Must be greater than or equal to 0.

        Returns:
            True if the life was set, False if this firework has already detonated.
        """
        ...

    def get_life(self) -> int:
        """
        Get the ticks that this firework has been alive. When this value reaches
        getMaxLife(), the firework will detonate.

        Returns:
            The life ticks.
        """
        ...

    def set_max_life(self, ticks: int) -> bool:
        """
        Set the time in ticks this firework will exist until it is detonated.

        Args:
            ticks: the ticks to set. Must be greater than 0.

        Returns:
            True if the time was set, False if this firework has already detonated.
        """
        ...

    def get_max_life(self) -> int:
        """
        Get the time in ticks this firework will exist until it is detonated.

        Returns:
            The maximum life in ticks.
        """
        ...

    def detonate(self) -> None:
        """
        Cause this firework to explode at earliest opportunity, as if it has no
        remaining fuse.
        """
        ...

    def is_detonated(self) -> bool:
        """
        Check whether or not this firework has detonated.

        Returns:
            True if detonated, False if still in the world.
        """
        ...

    def is_shot_at_angle(self) -> bool:
        """
        Gets if the firework was shot at an angle (i.e. from a crossbow).

        A firework which was not shot at an angle will fly straight upwards.

        Returns:
            Shot at angle status.
        """
        ...

    def set_shot_at_angle(self, shot_at_angle: bool) -> None:
        """
        Sets if the firework was shot at an angle (i.e. from a crossbow).

        A firework which was not shot at an angle will fly straight upwards.

        Args:
            shot_at_angle: the new shotAtAngle.
        """
        ...