from typing import Protocol

class Sittable(Protocol):
    """
    An animal that can sit still.
    """

    def is_sitting(self) -> bool:
        """
        Checks if this animal is sitting

        Returns:
            bool: true if sitting
        """
        ...

    def set_sitting(self, sitting: bool) -> None:
        """
        Sets if this animal is sitting. Will remove any path that the animal
        was following beforehand.

        Args:
            sitting (bool): true if sitting
        """
        ...