from org.bukkit.Location import Location
from org.bukkit.entity.Monster import Monster
from typing import Optional

class Vex(Monster):
    """
    Represents a Vex.
    """

    def is_charging(self) -> bool:
        """
        Gets the charging state of this entity.

        When this entity is charging it will having a glowing red texture.

        @return charging state
        """
        ...

    def set_charging(self, charging: bool) -> None:
        """
        Sets the charging state of this entity.

        When this entity is charging it will having a glowing red texture.

        @param charging new state
        """
        ...

    def get_bound(self) -> Optional[Location]:
        """
        Gets the bound of this entity.

        An idle vex will navigate a 15x11x15 area centered around its bound
        location.

        When summoned by an Evoker, this location will be set to that of the
        summoner.

        @return {@link Location} of the bound or null if not set
        """
        ...

    def set_bound(self, location: Optional[Location]) -> None:
        """
        Sets the bound of this entity.

        An idle vex will navigate a 15x11x15 area centered around its bound
        location.

        When summoned by an Evoker, this location will be set to that of the
        summoner.

        @param location {@link Location} of the bound or null to clear
        """
        ...

    def get_life_ticks(self) -> int:
        """
        Gets the remaining lifespan of this entity.

        @return life in ticks
        """
        ...

    def set_life_ticks(self, life_ticks: int) -> None:
        """
        Sets the remaining lifespan of this entity.

        @param life_ticks life in ticks, or negative for unlimited lifespan
        """
        ...

    def has_limited_life(self) -> bool:
        """
        Gets if the entity has a limited life.

        @return true if the entity has limited life
        """
        ...