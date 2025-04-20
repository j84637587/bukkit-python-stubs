from org.bukkit.entity import Vehicle
from org.bukkit.entity import Tameable
from org.bukkit.inventory import AbstractHorseInventory
from typing import Protocol

class Horse:
    class Variant:
        pass

class AbstractHorse(Protocol[Vehicle, Tameable]):
    """
    Represents a Horse-like creature.
    """

    def get_variant(self) -> Horse.Variant:
        """
        Gets the horse's variant.
        A horse's variant defines its physical appearance and capabilities.
        Whether a horse is a regular horse, donkey, mule, or other kind of horse
        is determined using the variant.

        @return: a {@link Horse.Variant} representing the horse's variant
        @deprecated: different variants are different classes
        """
        ...

    def set_variant(self, variant: Horse.Variant) -> None:
        """
        @param variant: variant
        @deprecated: you are required to spawn a different entity
        """
        ...

    def get_domestication(self) -> int:
        """
        Gets the domestication level of this horse.
        A higher domestication level indicates that the horse is closer to
        becoming tame. As the domestication level gets closer to the max
        domestication level, the chance of the horse becoming tame increases.

        @return: domestication level
        """
        ...

    def set_domestication(self, level: int) -> None:
        """
        Sets the domestication level of this horse.
        Setting the domestication level to a high value will increase the
        horse's chances of becoming tame.
        Domestication level must be greater than zero and no greater than
        the max domestication level of the horse, determined with
        {@link #getMaxDomestication()}

        @param level: domestication level
        """
        ...

    def get_max_domestication(self) -> int:
        """
        Gets the maximum domestication level of this horse.
        The higher this level is, the longer it will likely take
        for the horse to be tamed.

        @return: the max domestication level
        """
        ...

    def set_max_domestication(self, level: int) -> None:
        """
        Sets the maximum domestication level of this horse.
        Setting a higher max domestication will increase the amount of
        domesticating (feeding, riding, etc.) necessary in order to tame it,
        while setting a lower max value will have the opposite effect.
        Maximum domestication must be greater than zero.

        @param level: the max domestication level
        """
        ...

    def get_jump_strength(self) -> float:
        """
        Gets the jump strength of this horse.
        Jump strength defines how high the horse can jump. A higher jump strength
        increases how high a jump will go.

        @return: the horse's jump strength
        """
        ...

    def set_jump_strength(self, strength: float) -> None:
        """
        Sets the jump strength of this horse.
        A higher jump strength increases how high a jump will go.
        Setting a jump strength to 0 will result in no jump.
        You cannot set a jump strength to a value below 0 or
        above 2.

        @param strength: jump strength for this horse
        """
        ...

    def is_eating_haystack(self) -> bool:
        """
        Gets whether the horse is currently grazing hay.

        @return: true if eating hay
        """
        ...

    def set_eating_haystack(self, eating_haystack: bool) -> None:
        """
        Sets whether the horse is grazing hay.

        @param eating_haystack: new hay grazing status
        """
        ...

    def get_inventory(self) -> AbstractHorseInventory:
        ...