from org.bukkit.entity import Entity
from org.bukkit.entity import ComplexLivingEntity
from typing import Protocol

class ComplexEntityPart(Protocol):
    """
    Represents a single part of a {@link ComplexLivingEntity}
    """

    def get_parent(self) -> ComplexLivingEntity:
        """
        Gets the parent {@link ComplexLivingEntity} of this part.

        @return: Parent complex entity
        """
        ...