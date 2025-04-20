from org.bukkit import Instrument
from org.bukkit import Note
from org.bukkit.block.data import Powerable
from typing import Protocol

"""
'instrument' is the type of sound made when this note block is activated.
<br>
'note' is the specified tuned pitch that the instrument will be played in.
"""
class NoteBlock(Powerable, Protocol):

    """
    Gets the value of the 'instrument' property.

    @return: the 'instrument' value
    """
    def get_instrument(self) -> Instrument:
        ...

    """
    Sets the value of the 'instrument' property.

    @param instrument: the new 'instrument' value
    """
    def set_instrument(self, instrument: Instrument) -> None:
        ...

    """
    Gets the value of the 'note' property.

    @return: the 'note' value
    """
    def get_note(self) -> Note:
        ...

    """
    Sets the value of the 'note' property.

    @param note: the new 'note' value
    """
    def set_note(self, note: Note) -> None:
        ...