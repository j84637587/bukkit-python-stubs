from org.bukkit.entity import Animals
from org.bukkit import Material
from typing import Protocol

class Steerable(Animals, Protocol):
    """
    Represents an entity which may be saddled, ridden and steered using an item.
    """

    def has_saddle(self) -> bool:
        """
        Check if the pig has a saddle.

        :return: if the pig has been saddled.
        """
        ...

    def set_saddle(self, saddled: bool) -> None:
        """
        Sets if the pig has a saddle or not

        :param saddled: set if the pig has a saddle or not.
        """
        ...

    def get_boost_ticks(self) -> int:
        """
        Get the time in ticks this entity's movement is being increased.

        Movement speed is often increased as a result of using the
        :py:meth:`get_steer_material`.

        :return: the current boost ticks
        """
        ...

    def set_boost_ticks(self, ticks: int) -> None:
        """
        Set the time in ticks this entity's movement will be increased.

        This will reset the current boost ticks to 0
        (:py:meth:`get_current_boost_ticks`).

        :param ticks: the boost time
        """
        ...

    def get_current_boost_ticks(self) -> int:
        """
        Get the time in ticks this entity's movement has been increased as of the
        most recent boost.

        Current boost ticks will never be :literal: > :py:meth:`get_boost_ticks`.

        :return: the current boost ticks
        """
        ...

    def set_current_boost_ticks(self, ticks: int) -> None:
        """
        Set the time in ticks this entity's movement has been increased relative
        to the most recent boost.

        :param ticks: the current boost ticks. Must be :literal: >= 0 and :literal: <=
        :py:meth:`get_boost_ticks`
        """
        ...

    def get_steer_material(self) -> Material:
        """
        Get the material used to steer this entity when ridden by a player.

        :return: the lure material
        """
        ...