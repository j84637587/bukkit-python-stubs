from typing import Protocol

class AbstractArrow(Protocol):
    pass

class SpectralArrow(AbstractArrow, Protocol):
    """
    Represents a spectral arrow.
    """

    def get_glowing_ticks(self) -> int:
        """
        Returns the amount of time that this arrow will apply
        the glowing effect for.

        Returns:
            int: the glowing effect ticks
        """
        ...

    def set_glowing_ticks(self, duration: int) -> None:
        """
        Sets the amount of time to apply the glowing effect for.

        Args:
            duration (int): the glowing effect ticks
        """
        ...