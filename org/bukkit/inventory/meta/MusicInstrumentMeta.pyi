from org.bukkit import MusicInstrument
from typing import Optional

class MusicInstrumentMeta(ItemMeta):
    """
    Interface for MusicInstrumentMeta.
    """

    def set_instrument(self, instrument: Optional[MusicInstrument]) -> None:
        """
        Sets the goat horn's instrument.

        :param instrument: the instrument to set
        """
        ...

    def get_instrument(self) -> Optional[MusicInstrument]:
        """
        Gets the instrument of the goat horn.

        :return: The instrument of the goat horn
        """
        ...

    def clone(self) -> MusicInstrumentMeta:
        """
        Clones the MusicInstrumentMeta.

        :return: A clone of the MusicInstrumentMeta
        """
        ...