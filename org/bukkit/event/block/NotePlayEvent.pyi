from org.bukkit.Instrument import Instrument
from org.bukkit.Note import Note
from org.bukkit.block.Block import Block
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from typing import Optional

class NotePlayEvent(BlockEvent, Cancellable):
    """
    Called when a note block is being played through player interaction or a
    redstone current.
    """

    handlers: HandlerList

    def __init__(self, block: Block, instrument: Instrument, note: Note) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Gets the {@link Instrument} to be used.

    @return the Instrument
    """
    def getInstrument(self) -> Instrument:
        ...

    """
    Gets the {@link Note} to be played.

    @return the Note
    """
    def getNote(self) -> Note:
        ...

    """
    Overrides the {@link Instrument} to be used.

    @param instrument the Instrument. Has no effect if null.
    @deprecated no effect on newer Minecraft versions
    """
    def setInstrument(self, instrument: Optional[Instrument]) -> None:
        ...

    """
    Overrides the {@link Note} to be played.

    @param note the Note. Has no effect if null.
    @deprecated no effect on newer Minecraft versions
    """
    def setNote(self, note: Optional[Note]) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...