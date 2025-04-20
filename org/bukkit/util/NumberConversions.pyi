from typing import Optional

class NumberConversions:
    """
    Utils for casting number types to other number types
    """

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated")

    @staticmethod
    def floor(num: float) -> int:
        """Returns the largest integer less than or equal to num."""
        ...

    @staticmethod
    def ceil(num: float) -> int:
        """Returns the smallest integer greater than or equal to num."""
        ...

    @staticmethod
    def round(num: float) -> int:
        """Returns the closest integer to num."""
        ...

    @staticmethod
    def square(num: float) -> float:
        """Returns the square of num."""
        ...

    @staticmethod
    def to_int(object: Optional[object]) -> int:
        """Converts an object to an int."""
        ...

    @staticmethod
    def to_float(object: Optional[object]) -> float:
        """Converts an object to a float."""
        ...

    @staticmethod
    def to_double(object: Optional[object]) -> float:
        """Converts an object to a double (float in Python)."""
        ...

    @staticmethod
    def to_long(object: Optional[object]) -> int:
        """Converts an object to a long (int in Python)."""
        ...

    @staticmethod
    def to_short(object: Optional[object]) -> int:
        """Converts an object to a short (int in Python)."""
        ...

    @staticmethod
    def to_byte(object: Optional[object]) -> int:
        """Converts an object to a byte (int in Python)."""
        ...

    @staticmethod
    def is_finite(d: float) -> bool:
        """Checks if the given double is finite."""
        ...

    @staticmethod
    def is_finite(f: float) -> bool:
        """Checks if the given float is finite."""
        ...

    @staticmethod
    def check_finite(d: float, message: str) -> None:
        """Checks if the given double is finite, raises an exception if not."""
        ...

    @staticmethod
    def check_finite(f: float, message: str) -> None:
        """Checks if the given float is finite, raises an exception if not."""
        ...