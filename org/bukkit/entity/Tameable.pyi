from typing import Optional
from org.bukkit.entity import Animals
from org.jetbrains.annotations import Nullable

class Tameable(Animals):
    """
    Check if this is tamed
    <p>
    If something is tamed then a player can not tame it through normal
    methods, even if it does not belong to anyone in particular.
    """

    def is_tamed(self) -> bool:
        ...

    """
    Sets if this has been tamed. Not necessary if the method setOwner has
    been used, as it tames automatically.
    <p>
    If something is tamed then a player can not tame it through normal
    methods, even if it does not belong to anyone in particular.
    
    @param tame true if tame
    """

    def set_tamed(self, tame: bool) -> None:
        ...

    """
    Gets the current owning AnimalTamer
    
    @return the owning AnimalTamer, or null if not owned
    """

    def get_owner(self) -> Optional['AnimalTamer']:
        ...

    """
    Set this to be owned by given AnimalTamer.
    <p>
    If the owner is not null, this will be tamed and will have any current
    path it is following removed. If the owner is set to null, this will be
    untamed, and the current owner removed.
    
    @param tamer the AnimalTamer who should own this
    """

    def set_owner(self, tamer: Optional['AnimalTamer']) -> None:
        ...