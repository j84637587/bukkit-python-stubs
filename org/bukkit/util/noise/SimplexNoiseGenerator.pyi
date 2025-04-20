from random import Random
from org.bukkit import World
from typing import List

class SimplexNoiseGenerator(PerlinNoiseGenerator):
    """
    Generates simplex-based noise.
    <p>
    This is a modified version of the freely published version in the paper by
    Stefan Gustavson at
    <a href="http://staffwww.itn.liu.se/~stegu/simplexnoise/simplexnoise.pdf">
    http://staffwww.itn.liu.se/~stegu/simplexnoise/simplexnoise.pdf</a>
    """

    SQRT_3: float
    SQRT_5: float
    F2: float
    G2: float
    G22: float
    F3: float
    G3: float
    F4: float
    G4: float
    G42: float
    G43: float
    G44: float
    grad4: List[List[int]]
    simplex: List[List[int]]
    offsetW: float
    instance: 'SimplexNoiseGenerator'

    def __init__(self) -> None:
        ...

    def __init__(self, world: World) -> None:
        ...

    def __init__(self, seed: int) -> None:
        ...

    def __init__(self, rand: Random) -> None:
        ...

    @staticmethod
    def dot(g: List[int], x: float, y: float) -> float:
        ...

    @staticmethod
    def dot(g: List[int], x: float, y: float, z: float) -> float:
        ...

    @staticmethod
    def dot(g: List[int], x: float, y: float, z: float, w: float) -> float:
        ...

    @staticmethod
    def getNoise(xin: float) -> float:
        ...

    @staticmethod
    def getNoise(xin: float, yin: float) -> float:
        ...

    @staticmethod
    def getNoise(xin: float, yin: float, zin: float) -> float:
        ...

    @staticmethod
    def getNoise(x: float, y: float, z: float, w: float) -> float:
        ...

    def noise(self, xin: float, yin: float, zin: float) -> float:
        ...

    def noise(self, xin: float, yin: float) -> float:
        ...

    def noise(self, x: float, y: float, z: float, w: float) -> float:
        ...

    @staticmethod
    def getInstance() -> 'SimplexNoiseGenerator':
        ...