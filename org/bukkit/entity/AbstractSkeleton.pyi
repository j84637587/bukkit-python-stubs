from typing import Protocol
from org.bukkit.entity import Monster
from org.bukkit.entity import Skeleton

class AbstractSkeleton(Protocol[Monster]):
    """
    This interface defines or represents the abstract concept of skeleton-like
    entities on the server. The interface is hence not a direct representation
    of an entity but rather serves as a parent to interfaces/entity types like
    {@link Skeleton}, {@link WitherSkeleton} or {@link Stray}.

    To compute what specific type of skeleton is present in a variable/field
    of this type, instanceOf checks against the specific subtypes listed prior
    are recommended.
    """

    @property
    def skeleton_type(self) -> Skeleton.SkeletonType:
        """
        Gets the current type of this skeleton.

        @return: Current type
        @deprecated: should check what class instance this is.
        """
        ...

    @skeleton_type.setter
    def skeleton_type(self, type: Skeleton.SkeletonType) -> None:
        """
        @param type: type
        @deprecated: Must spawn a new subtype variant
        """
        ...