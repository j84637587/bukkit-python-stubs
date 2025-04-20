from random import Random
from org.bukkit import World
from org.bukkit.util.noise import OctaveGenerator, NoiseGenerator
from typing import List

class PerlinOctaveGenerator(OctaveGenerator):
    """
    Creates perlin noise through unbiased octaves
    """

    def __init__(self, world: World, octaves: int) -> None:
        """
        Creates a perlin octave generator for the given world

        :param world: World to construct this generator for
        :param octaves: Amount of octaves to create
        """
        ...

    def __init__(self, seed: int, octaves: int) -> None:
        """
        Creates a perlin octave generator for the given world

        :param seed: Seed to construct this generator for
        :param octaves: Amount of octaves to create
        """
        ...

    def __init__(self, rand: Random, octaves: int) -> None:
        """
        Creates a perlin octave generator for the given Random

        :param rand: Random object to construct this generator for
        :param octaves: Amount of octaves to create
        """
        ...

    @staticmethod
    def create_octaves(rand: Random, octaves: int) -> List[NoiseGenerator]:
        """
        Creates octaves for the perlin noise generator

        :param rand: Random object to construct this generator for
        :param octaves: Amount of octaves to create
        :return: Array of NoiseGenerator
        """
        ...