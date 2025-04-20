from typing import Protocol

class Fish(Protocol):
    pass

class PufferFish(Fish, Protocol):
    """Represents a puffer fish."""

    def get_puff_state(self) -> int:
        """Returns the current puff state of this fish (i.e. how inflated it is).

        Returns:
            current puff state
        """
        ...

    def set_puff_state(self, state: int) -> None:
        """Sets the current puff state of this fish (i.e. how inflated it is).

        Args:
            state: new puff state
        """
        ...