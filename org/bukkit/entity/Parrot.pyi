from typing import Protocol, Literal

class Variant:
    """Represents the variant of a parrot - ie its color."""
    RED: Literal['RED']
    BLUE: Literal['BLUE']
    GREEN: Literal['GREEN']
    CYAN: Literal['CYAN']
    GRAY: Literal['GRAY']

class Tameable(Protocol):
    pass

class Sittable(Protocol):
    pass

class Parrot(Tameable, Sittable, Protocol):
    """Represents a Parrot."""

    def get_variant(self) -> Variant:
        """Get the variant of this parrot.

        Returns:
            parrot variant
        """
        ...

    def set_variant(self, variant: Variant) -> None:
        """Set the variant of this parrot.

        Args:
            variant: parrot variant
        """
        ...

    def is_dancing(self) -> bool:
        """Gets whether a parrot is dancing.

        Returns:
            Whether the parrot is dancing
        """
        ...