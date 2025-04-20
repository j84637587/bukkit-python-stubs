from org.bukkit.entity import ComplexLivingEntity, Boss, Mob, Enemy
from org.bukkit import World
from org.bukkit.boss import DragonBattle
from typing import Optional

class EnderDragon(ComplexLivingEntity, Boss, Mob, Enemy):
    """
    Represents an Ender Dragon
    """

    class Phase:
        """
        Represents a phase or action that an Ender Dragon can perform.
        """
        CIRCLING = ...
        STRAFING = ...
        FLY_TO_PORTAL = ...
        LAND_ON_PORTAL = ...
        LEAVE_PORTAL = ...
        BREATH_ATTACK = ...
        SEARCH_FOR_BREATH_ATTACK_TARGET = ...
        ROAR_BEFORE_ATTACK = ...
        CHARGE_PLAYER = ...
        DYING = ...
        HOVER = ...

    def get_phase(self) -> Phase:
        """
        Gets the current phase that the dragon is performing.

        Returns:
            Phase: the current phase
        """
        ...

    def set_phase(self, phase: Phase) -> None:
        """
        Sets the next phase for the dragon to perform.

        Args:
            phase (Phase): the next phase
        """
        ...

    def get_dragon_battle(self) -> Optional[DragonBattle]:
        """
        Get the {@link DragonBattle} associated with this EnderDragon.
        This will return None for the following reasons:
        - The EnderDragon is not in the End dimension
        - The EnderDragon was summoned by command/API

        Returns:
            DragonBattle: the dragon battle
        """
        ...

    def get_death_animation_ticks(self) -> int:
        """
        Get the current time in ticks relative to the start of this dragon's
        death animation.

        If this dragon is alive, 0 will be returned. This value will never exceed
        200 (the length of the animation).

        Returns:
            int: this dragon's death animation ticks
        """
        ...