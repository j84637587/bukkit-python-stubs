from typing import Protocol

class AbstractHorse(Protocol):
    pass

class Sittable(Protocol):
    pass

class Camel(AbstractHorse, Sittable):
    """
    Represents a Camel.
    """

    def is_dashing(self) -> bool:
        """
        Gets whether this camel is dashing (sprinting).

        :return: dashing status
        """
        ...

    def set_dashing(self, dashing: bool) -> None:
        """
        Sets whether this camel is dashing (sprinting).

        :param dashing: new dashing status
        """
        ...