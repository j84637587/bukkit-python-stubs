from random import Random
from org.bukkit import World
from org.bukkit.util.noise import OctaveGenerator, NoiseGenerator
from org.jetbrains.annotations import NotNull
from typing import List

class SimplexOctaveGenerator(OctaveGenerator):
    """
    Creates simplex noise through unbiased octaves
    """
    wScale: float = 1.0

    def __init__(self, world: NotNull[World], octaves: int) -> None:
        """
        Creates a simplex octave generator for the given world

        :param world: World to construct this generator for
        :param octaves: Amount of octaves to create
        """
        ...

    def __init__(self, seed: int, octaves: int) -> None:
        """
        Creates a simplex octave generator for the given world

        :param seed: Seed to construct this generator for
        :param octaves: Amount of octaves to create
        """
        ...

    def __init__(self, rand: NotNull[Random], octaves: int) -> None:
        """
        Creates a simplex octave generator for the given {@link Random}

        :param rand: Random object to construct this generator for
        :param octaves: Amount of octaves to create
        """
        ...

    def set_scale(self, scale: float) -> None:
        """
        Sets the scale for the generator.

        :param scale: New scale
        """
        ...

    def get_w_scale(self) -> float:
        """
        Gets the scale used for each W-coordinates passed

        :return: W scale
        """
        ...

    def set_w_scale(self, scale: float) -> None:
        """
        Sets the scale used for each W-coordinates passed

        :param scale: New W scale
        """
        ...

    def noise(self, x: float, y: float, z: float, w: float, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        :param x: X-coordinate
        :param y: Y-coordinate
        :param z: Z-coordinate
        :param w: W-coordinate
        :param frequency: How much to alter the frequency by each octave
        :param amplitude: How much to alter the amplitude by each octave
        :return: Resulting noise
        """
        ...

    def noise(self, x: float, y: float, z: float, w: float, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        :param x: X-coordinate
        :param y: Y-coordinate
        :param z: Z-coordinate
        :param w: W-coordinate
        :param frequency: How much to alter the frequency by each octave
        :param amplitude: How much to alter the amplitude by each octave
        :param normalized: If true, normalize the value to [-1, 1]
        :return: Resulting noise
        """
        ...

    @staticmethod
    def create_octaves(rand: NotNull[Random], octaves: int) -> List[NoiseGenerator]:
        """
        Creates octaves for the noise generator.

        :param rand: Random object to construct this generator for
        :param octaves: Amount of octaves to create
        :return: Array of NoiseGenerators
        """
        ...