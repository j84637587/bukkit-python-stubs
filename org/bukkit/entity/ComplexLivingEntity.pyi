from typing import Set
from org.bukkit.entity import LivingEntity
from org.bukkit.entity import ComplexEntityPart

class ComplexLivingEntity(LivingEntity):
    """
    Represents a complex living entity - one that is made up of various smaller
    parts
    """

    def get_parts(self) -> Set[ComplexEntityPart]:
        """
        Gets a list of parts that belong to this complex entity

        @return: Set of parts
        """
        ...