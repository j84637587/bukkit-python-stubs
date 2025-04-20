# org/bukkit/entity/Slime.pyi

from typing import Protocol

class Mob(Protocol):
    pass

class Enemy(Protocol):
    pass

class Slime(Mob, Enemy):
    """Represents a Slime."""

    def get_size(self) -> int:
        """@return The size of the slime."""
        ...

    def set_size(self, sz: int) -> None:
        """@param sz The new size of the slime."""
        ...