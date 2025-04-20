from typing import Literal, Protocol

class Tilt:
    """The tilt of a leaf."""
    NONE: Literal['NONE']
    UNSTABLE: Literal['UNSTABLE']
    PARTIAL: Literal['PARTIAL']
    FULL: Literal['FULL']

class Dripleaf(Protocol):
    pass

class BigDripleaf(Dripleaf, Protocol):
    """
    'tilt' indicates how far the leaf is tilted.
    """

    def get_tilt(self) -> Tilt:
        """
        Gets the value of the 'tilt' property.

        Returns:
            Tilt: the 'tilt' value
        """
        ...

    def set_tilt(self, tilt: Tilt) -> None:
        """
        Sets the value of the 'tilt' property.

        Args:
            tilt (Tilt): the new 'tilt' value
        """
        ...