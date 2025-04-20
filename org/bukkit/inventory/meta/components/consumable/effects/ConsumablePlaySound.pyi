from org.bukkit import Sound
from typing import Optional

class ConsumablePlaySound:
    """
    Represent a sound played when an item is consumed.
    """

    def get_sound(self) -> Optional[Sound]:
        """
        Gets the sound to play on completion of the item's consumption.

        Returns:
            the sound
        """
        ...

    def set_sound(self, sound: Optional[Sound]) -> None:
        """
        Sets the sound to play on completion of the item's consumption.

        Args:
            sound: sound
        """
        ...