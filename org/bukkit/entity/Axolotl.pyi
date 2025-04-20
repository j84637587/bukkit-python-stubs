from typing import Protocol
from org.bukkit.entity import Animals
from org.jetbrains.annotations import NotNull

class Variant:
    """Represents the variant of an axolotl - ie its color."""
    LUCY: 'Variant'
    WILD: 'Variant'
    GOLD: 'Variant'
    CYAN: 'Variant'
    BLUE: 'Variant'


class Axolotl(Animals, Protocol):
    """An Axolotl."""

    def is_playing_dead(self) -> bool:
        """Gets if this axolotl is playing dead.

        An axolotl may play dead when it is damaged underwater.

        Returns:
            playing dead status
        """
        ...

    def set_playing_dead(self, playing_dead: bool) -> None:
        """Sets if this axolotl is playing dead.

        An axolotl may play dead when it is damaged underwater.

        Args:
            playing_dead: playing dead status
        """
        ...

        def get_variant(self) -> Variant:
        """Get the variant of this axolotl.

        Returns:
            axolotl variant
        """
        ...

    def set_variant(self, variant: NotNull[Variant]) -> None:
        """Set the variant of this axolotl.

        Args:
            variant: axolotl variant
        """
        ...