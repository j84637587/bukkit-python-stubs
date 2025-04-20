from typing import Optional, Type
from org.bukkit.entity import LivingEntity, Monster, Boss

class Wither(Monster, Boss):
    """
    Represents a Wither boss
    """

    def setTarget(self, target: Optional[LivingEntity]) -> None:
        """
        {@inheritDoc}
        <p>
        This method will set the target of the {@link Head#CENTER center head} of
        the wither.

        @see #setTarget(org.bukkit.entity.Wither.Head, org.bukkit.entity.LivingEntity)
        """
        ...

    def setTarget(self, head: Type[Wither.Head], target: Optional[LivingEntity]) -> None:
        """
        This method will set the target of individual heads {@link Head} of the
        wither.

        @param head the individual head
        @param target the entity that should be targeted
        """
        ...

    def getTarget(self, head: Type[Wither.Head]) -> Optional[LivingEntity]:
        """
        This method will get the target of individual heads {@link Head} of the
        wither.

        @param head the individual head
        @return the entity targeted by the given head, or null if none is
        targeted
        """
        ...

    def getInvulnerabilityTicks(self) -> int:
        """
        Returns the wither's current invulnerability ticks.

        @return amount of invulnerability ticks
        """
        ...

    def setInvulnerabilityTicks(self, ticks: int) -> None:
        """
        Sets the wither's current invulnerability ticks.

        When invulnerability ticks reach 0, the wither will trigger an explosion.

        @param ticks amount of invulnerability ticks
        """
        ...

    class Head:
        """
        Represents one of the Wither's heads.
        """
        CENTER = ...
        LEFT = ...
        RIGHT = ...