from typing import Optional
from org.bukkit.entity import Entity, LivingEntity

class EvokerFangs(Entity):
    """
    Represents Evoker Fangs.
    """

    def get_owner(self) -> Optional[LivingEntity]:
        """
        Gets the {@link LivingEntity} which summoned the fangs.

        @return: the {@link LivingEntity} which summoned the fangs
        """
        ...

    def set_owner(self, owner: Optional[LivingEntity]) -> None:
        """
        Sets the {@link LivingEntity} which summoned the fangs.

        @param owner: the {@link LivingEntity} which summoned the fangs
        """
        ...

    def get_attack_delay(self) -> int:
        """
        Get the delay in ticks until the fang attacks.

        @return: the delay
        """
        ...

    def set_attack_delay(self, delay: int) -> None:
        """
        Set the delay in ticks until the fang attacks.

        @param delay: the delay, must be positive
        """
        ...