from org.bukkit.entity import Monster
from org.jetbrains.annotations import NotNull, Nullable

class Creeper(Monster):
    """Represents a Creeper"""

    def is_powered(self) -> bool:
        """Checks if this Creeper is powered (Electrocuted)

        Returns:
            bool: true if this creeper is powered
        """
        ...

    def set_powered(self, value: bool) -> None:
        """Sets the Powered status of this Creeper

        Args:
            value (bool): New Powered status
        """
        ...

    def set_max_fuse_ticks(self, ticks: int) -> None:
        """Set the maximum fuse ticks for this Creeper, where the maximum ticks
        is the amount of time in which a creeper is allowed to be in the
        primed state before exploding.

        Args:
            ticks (int): the new maximum fuse ticks
        """
        ...

    def get_max_fuse_ticks(self) -> int:
        """Get the maximum fuse ticks for this Creeper, where the maximum ticks
        is the amount of time in which a creeper is allowed to be in the
        primed state before exploding.

        Returns:
            int: the maximum fuse ticks
        """
        ...

    def set_fuse_ticks(self, ticks: int) -> None:
        """Set the fuse ticks for this Creeper, where the ticks is the amount of
        time in which a creeper has been in the primed state.

        Args:
            ticks (int): the new fuse ticks
        """
        ...

    def get_fuse_ticks(self) -> int:
        """Get the maximum fuse ticks for this Creeper, where the ticks is the
        amount of time in which a creeper has been in the primed state.

        Returns:
            int: the fuse ticks
        """
        ...

    def set_explosion_radius(self, radius: int) -> None:
        """Set the explosion radius in which this Creeper's explosion will affect.

        Args:
            radius (int): the new explosion radius
        """
        ...

    def get_explosion_radius(self) -> int:
        """Get the explosion radius in which this Creeper's explosion will affect.

        Returns:
            int: the explosion radius
        """
        ...

    def explode(self) -> None:
        """Makes this Creeper explode instantly.
        The resulting explosion can be cancelled by an
        `org.bukkit.event.entity.ExplosionPrimeEvent` and obeys the mob
        griefing gamerule.
        """
        ...

    def ignite(self, entity: NotNull['Entity'] = None) -> None:
        """Ignites this Creeper, beginning its fuse.
        The amount of time the Creeper takes to explode will depend on what
        `set_max_fuse_ticks` is set as.
        The resulting explosion can be cancelled by an
        `org.bukkit.event.entity.ExplosionPrimeEvent` and obeys the mob
        griefing gamerule.

        Args:
            entity (Entity, optional): the entity which ignited the creeper
        """
        ...

        def get_igniter(self) -> 'Entity':
        """Gets the entity which ignited the creeper, if available.

        Returns:
            Entity: the entity which ignited the creeper (if available) or None
        """
        ...