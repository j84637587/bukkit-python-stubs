from org.bukkit import Sound
from typing import Protocol

class SoundGroup(Protocol):
    """
    Represents a group of sounds for blocks that are played when various actions
    happen (ie stepping, breaking, hitting, etc).
    """

    def get_volume() -> float:
        """
        Get the volume these sounds are played at.

        Note that this volume does not always represent the actual volume
        received by the client.

        :return: volume
        """

    def get_pitch() -> float:
        """
        Gets the pitch these sounds are played at.

        Note that this pitch does not always represent the actual pitch received
        by the client.

        :return: pitch
        """

    def get_break_sound() -> Sound:
        """
        Gets the corresponding breaking sound for this group.

        :return: the break sound
        """

    def get_step_sound() -> Sound:
        """
        Gets the corresponding step sound for this group.

        :return: the step sound
        """

    def get_place_sound() -> Sound:
        """
        Gets the corresponding place sound for this group.

        :return: the place sound
        """

    def get_hit_sound() -> Sound:
        """
        Gets the corresponding hit sound for this group.

        :return: the hit sound
        """

    def get_fall_sound() -> Sound:
        """
        Gets the corresponding fall sound for this group.

        :return: the fall sound
        """