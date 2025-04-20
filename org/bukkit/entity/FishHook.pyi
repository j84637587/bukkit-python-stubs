from typing import Optional
from org.jetbrains.annotations import NotNull, Nullable
from org.bukkit.entity import Projectile, Entity

class FishHook(Projectile):
    """Represents a fishing hook."""

    def get_min_wait_time(self) -> int:
        """Get the minimum number of ticks one has to wait for a fish appearing.
        
        The default is 100 ticks (5 seconds).
        Note that this is before applying lure.
        
        Returns:
            Minimum number of ticks one has to wait for a fish appearing
        """
        ...

    def set_min_wait_time(self, min_wait_time: int) -> None:
        """Set the minimum number of ticks one has to wait for a fish appearing.
        
        The default is 100 ticks (5 seconds).
        Note that this is before applying lure.
        
        Args:
            min_wait_time: Minimum number of ticks one has to wait for a fish appearing
        """
        ...

    def get_max_wait_time(self) -> int:
        """Get the maximum number of ticks one has to wait for a fish appearing.
        
        The default is 600 ticks (30 seconds).
        Note that this is before applying lure.
        
        Returns:
            Maximum number of ticks one has to wait for a fish appearing
        """
        ...

    def set_max_wait_time(self, max_wait_time: int) -> None:
        """Set the maximum number of ticks one has to wait for a fish appearing.
        
        The default is 600 ticks (30 seconds).
        Note that this is before applying lure.
        
        Args:
            max_wait_time: Maximum number of ticks one has to wait for a fish appearing
        """
        ...

    def set_wait_time(self, min: int, max: int) -> None:
        """Set both the minimum (default 100) and maximum (default 600) amount
        of ticks one has to wait for a fish appearing.
        
        Args:
            min: minimum ticks for a fish to appear
            max: maximum ticks for a fish to appear
        """
        ...

    def get_min_lure_time(self) -> int:
        """Get the minimum number of ticks one has to wait for a fish to bite
        after appearing.
        
        The default is 20 ticks (1 second).
        Lure does not affect this value.
        This will also effect the radius (0.1 * lureTime) of where
        the fish will appear.
        
        Returns:
            Minimum number of ticks one has to wait for a fish to bite
        """
        ...

    def set_min_lure_time(self, min_lure_time: int) -> None:
        """Set the minimum number of ticks one has to wait for a fish to bite
        after appearing.
        
        The default is 20 ticks (1 second).
        Lure does not affect this value.
        This will also effect the radius (0.1 * lureTime) of where
        the fish will appear.
        
        Args:
            min_lure_time: Minimum number of ticks one has to wait for a fish to bite
        """
        ...

    def get_max_lure_time(self) -> int:
        """Get the maximum number of ticks one has to wait for a fish to bite
        after appearing.
        
        The default is 80 ticks (4 second).
        Lure does not affect this value.
        This will also effect the radius (0.1 * lureTime) of where
        the fish will appear.
        
        Returns:
            Maximum number of ticks one has to wait for a fish to bite
        """
        ...

    def set_max_lure_time(self, max_lure_time: int) -> None:
        """Set the maximum number of ticks one has to wait for a fish to bite
        after appearing.
        
        The default is 80 ticks (4 second).
        Lure does not affect this value.
        This will also effect the radius (0.1 * lureTime) of where
        the fish will appear.
        
        Args:
            max_lure_time: Maximum number of ticks one has to wait for a fish to bite
        """
        ...

    def set_lure_time(self, min: int, max: int) -> None:
        """Set both the minimum (default 20) and maximum (default 80) amount
        of ticks one has to wait for a fish to bite after appearing.
        
        Args:
            min: minimum ticks to wait for a bite
            max: maximum ticks to wait for a bite
        """
        ...

    def get_min_lure_angle(self) -> float:
        """Get the minimum angle (in degrees, 0 being positive Z 90 being negative
        X) of where a fish will appear after the wait time.
        
        The default is 0 degrees.
        
        Returns:
            Minimum angle of where a fish will appear
        """
        ...

    def set_min_lure_angle(self, min_lure_angle: float) -> None:
        """Set the minimum angle (in degrees, 0 being positive Z 90 being negative
        X) of where a fish will appear after the wait time.
        
        The default is 0 degrees.
        
        Args:
            min_lure_angle: Minimum angle of where a fish may appear
        """
        ...

    def get_max_lure_angle(self) -> float:
        """Get the maximum angle (in degrees, 0 being positive Z 90 being negative
        X) of where a fish will appear after the wait time.
        
        The default is 360 degrees.
        
        Returns:
            Maximum angle of where a fish will appear
        """
        ...

    def set_max_lure_angle(self, max_lure_angle: float) -> None:
        """Set the maximum angle (in degrees, 0 being positive Z 90 being negative
        X) of where a fish will appear after the wait time.
        
        The default is 360 degrees.
        
        Args:
            max_lure_angle: Maximum angle of where a fish may appear
        """
        ...

    def set_lure_angle(self, min: float, max: float) -> None:
        """Set both the minimum (default 0) and maximum (default 360) angle of where
        a fish will appear after the wait time.
        
        0 degrees is positive Z, 90 degrees is negative X.
        
        Args:
            min: minimum angle in degrees
            max: maximum angle in degrees
        """
        ...

    def get_apply_lure(self) -> bool:
        """Get whether the lure enchantment should be applied to reduce the wait
        time.
        
        The default is true.
        Lure reduces the wait time by 100 ticks (5 seconds) for each level of the
        enchantment.
        
        Returns:
            Whether the lure enchantment should be applied to reduce the wait time
        """
        ...

    def set_apply_lure(self, apply_lure: bool) -> None:
        """Set whether the lure enchantment should be applied to reduce the wait
        time.
        
        The default is true.
        Lure reduces the wait time by 100 ticks (5 seconds) for each level of the
        enchantment.
        
        Args:
            apply_lure: Whether the lure enchantment should be applied to reduce
            the wait time
        """
        ...

    def get_bite_chance(self) -> float:
        """Gets the chance of a fish biting.
        
        0.0 = No Chance.
        1.0 = Instant catch.
        
        Returns:
            chance the bite chance
        @deprecated has no effect in newer Minecraft versions
        """
        ...

    def set_bite_chance(self, chance: float) -> None:
        """Sets the chance of a fish biting.
        
        0.0 = No Chance.
        1.0 = Instant catch.
        
        Args:
            chance: the bite chance
            
        Raises:
            IllegalArgumentException: if the bite chance is not between 0 and 1
        @deprecated has no effect in newer Minecraft versions
        """
        ...

    def is_in_open_water(self) -> bool:
        """Check whether or not this fish hook is in open water.
        
        Open water is defined by a 5x4x5 area of water, air and lily pads. If in
        open water, treasure items may be caught.
        
        Returns:
            true if in open water, false otherwise
        """
        ...

    def get_hooked_entity(self) -> Optional[Entity]:
        """Get the entity hooked by this fish hook.
        
        Returns:
            the hooked entity. None if none
        """
        ...

    def set_hooked_entity(self, entity: Optional[Entity]) -> None:
        """Set the entity hooked by this fish hook.
        
        Args:
            entity: the entity to set, or None to unhook
        """
        ...

    def pull_hooked_entity(self) -> bool:
        """Pull the hooked entity to the caster of this fish hook. If no entity is
        hooked, this method has no effect.
        
        Returns:
            true if pulled, false if no entity is hooked
        """
        ...

    def is_sky_influenced(self) -> bool:
        """Whether or not wait and lure time will be impacted by direct sky access.
        
        True by default, causes a 50% time increase on average.
        
        Returns:
            skylight access influences catch rate
        """
        ...

    def set_sky_influenced(self, sky_influenced: bool) -> None:
        """Set whether or not wait and lure time will be impacted by direct sky
        access.
        
        True by default, causes a 50% time increase on average.
        
        Args:
            sky_influenced: if this hook is influenced by skylight access
        """
        ...

    def is_rain_influenced(self) -> bool:
        """Whether or not wait and lure time will be impacted by rain.
        
        True by default, causes a 25% time decrease on average.
        
        Returns:
            rain influences catch rate
        """
        ...

    def set_rain_influenced(self, rain_influenced: bool) -> None:
        """Set whether or not wait and lure time will be impacted by rain.
        
        True by default, causes a 25% time decrease on average.
        
        Args:
            rain_influenced: if this hook is influenced by rain
        """
        ...

    def get_state(self) -> NotNull['HookState']:
        """Get the current state of this fish hook.
        
        Returns:
            the fish hook state
        """
        ...

    class HookState:
        """Represents a state in which a fishing hook may be."""

        UNHOOKED = ...
        HOOKED_ENTITY = ...
        BOBBING = ...