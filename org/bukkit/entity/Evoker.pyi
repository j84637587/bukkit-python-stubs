from typing import Optional, Literal

class Evoker(Spellcaster):
    """Represents an Evoker "Illager"."""

    class Spell:
        """Represents the current spell the Evoker is using."""
        
        NONE: Literal['NONE']
        SUMMON: Literal['SUMMON']
        FANGS: Literal['FANGS']
        WOLOLO: Literal['WOLOLO']
        DISAPPEAR: Literal['DISAPPEAR']
        BLINDNESS: Literal['BLINDNESS']

    def get_current_spell(self) -> Spell:
        """
        Gets the Spell the Evoker is currently using.

        Returns:
            Spell: the current spell
        """
        ...

    def set_current_spell(self, spell: Optional[Spell]) -> None:
        """
        Sets the Spell the Evoker is currently using.

        Args:
            spell (Optional[Spell]): the spell the evoker should be using
        """
        ...