from typing import Literal, Protocol
from typing_extensions import Final

class Illager(Protocol):
    pass

class Spellcaster(Illager, Protocol):
    """Represents a spell casting "Illager"."""

    class Spell:
        """Represents the current spell the entity is using."""
        
        NONE: Final[Literal['NONE']]
        SUMMON_VEX: Final[Literal['SUMMON_VEX']]
        FANGS: Final[Literal['FANGS']]
        WOLOLO: Final[Literal['WOLOLO']]
        DISAPPEAR: Final[Literal['DISAPPEAR']]
        BLINDNESS: Final[Literal['BLINDNESS']]

    def get_spell(self) -> Spell:
        """Gets the Spell the entity is currently using.

        Returns:
            The current spell.
        """
        ...

    def set_spell(self, spell: Spell) -> None:
        """Sets the Spell the entity is currently using.

        Args:
            spell: The spell the entity should be using.
        """
        ...