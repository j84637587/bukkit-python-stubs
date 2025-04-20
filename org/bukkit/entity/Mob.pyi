from org.bukkit.entity import LivingEntity
from org.bukkit.loot import Lootable
from org.bukkit import Sound
from typing import Optional

class Mob(LivingEntity, Lootable):
    """
    Represents a Mob. Mobs are living entities with simple AI.
    """

    def set_target(self, target: Optional[LivingEntity]) -> None:
        """
        Instructs this Mob to set the specified LivingEntity as its target.
        <p>
        Hostile creatures may attack their target, and friendly creatures may
        follow their target.

        @param target New LivingEntity to target, or null to clear the target
        """
        ...

    def get_target(self) -> Optional[LivingEntity]:
        """
        Gets the current target of this Mob

        @return Current target of this creature, or null if none exists
        """
        ...

    def set_aware(self, aware: bool) -> None:
        """
        Sets whether this mob is aware of its surroundings.

        Unaware mobs will still move if pushed, attacked, etc. but will not move
        or perform any actions on their own. Unaware mobs may also have other
        unspecified behaviours disabled, such as drowning.

        @param aware whether the mob is aware
        """
        ...

    def is_aware(self) -> bool:
        """
        Gets whether this mob is aware of its surroundings.

        Unaware mobs will still move if pushed, attacked, etc. but will not move
        or perform any actions on their own. Unaware mobs may also have other
        unspecified behaviours disabled, such as drowning.

        @return whether the mob is aware
        """
        ...

    def get_ambient_sound(self) -> Optional[Sound]:
        """
        Get the Sound this mob makes while ambiently existing. This sound
        may change depending on the current state of the entity, and may also
        return null under specific conditions. This sound is not constant.
        For instance, villagers will make different passive noises depending
        on whether or not they are actively trading with a player, or make no
        ambient noise while sleeping.

        @return the ambient sound, or null if this entity is ambiently quiet
        """
        ...