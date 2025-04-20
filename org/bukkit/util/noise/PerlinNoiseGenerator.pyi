from random import Random
from org.bukkit import World
from typing import Optional

class PerlinNoiseGenerator:
    """
    Generates noise using the "classic" perlin generator

    @see SimplexNoiseGenerator "Improved" and faster version with slightly
        different results
    """
    
    grad3: list[list[int]] = [[1, 1, 0], [-1, 1, 0], [1, -1, 0], [-1, -1, 0],
                               [1, 0, 1], [-1, 0, 1], [1, 0, -1], [-1, 0, -1],
                               [0, 1, 1], [0, -1, 1], [0, 1, -1], [0, -1, -1]]
    instance: 'PerlinNoiseGenerator' = None  # type: ignore
    perm: list[int] = [0] * 512
    offsetX: float
    offsetY: float
    offsetZ: float

    def __init__(self) -> None:
        """
        Initializes the PerlinNoiseGenerator with default parameters.
        """
        p: list[int] = [151, 160, 137, 91, 90, 15, 131, 13, 201,
                         95, 96, 53, 194, 233, 7, 225, 140, 36, 103, 30, 69, 142, 8, 99, 37,
                         240, 21, 10, 23, 190, 6, 148, 247, 120, 234, 75, 0, 26, 197, 62,
                         94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33, 88, 237, 149, 56,
                         87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134, 139,
                         48, 27, 166, 77, 146, 158, 231, 83, 111, 229, 122, 60, 211, 133,
                         230, 220, 105, 92, 41, 55, 46, 245, 40, 244, 102, 143, 54, 65, 25,
                         63, 161, 1, 216, 80, 73, 209, 76, 132, 187, 208, 89, 18, 169, 200,
                         196, 135, 130, 116, 188, 159, 86, 164, 100, 109, 198, 173, 186, 3,
                         64, 52, 217, 226, 250, 124, 123, 5, 202, 38, 147, 118, 126, 255,
                         82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42,
                         223, 183, 170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153,
                         101, 155, 167, 43, 172, 9, 129, 22, 39, 253, 19, 98, 108, 110, 79,
                         113, 224, 232, 178, 185, 112, 104, 218, 246, 97, 228, 251, 34, 242,
                         193, 238, 210, 144, 12, 191, 179, 162, 241, 81, 51, 145, 235, 249,
                         14, 239, 107, 49, 192, 214, 31, 181, 199, 106, 157, 184, 84, 204,
                         176, 115, 121, 50, 45, 127, 4, 150, 254, 138, 236, 205, 93, 222,
                         114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180]

        for i in range(512):
            self.perm[i] = p[i & 255]

    def __init__(self, world: World) -> None:
        """
        Creates a seeded perlin noise generator for the given world

        @param world World to construct this generator for
        """
        self.__init__(Random(world.getSeed()))

    def __init__(self, seed: int) -> None:
        """
        Creates a seeded perlin noise generator for the given seed

        @param seed Seed to construct this generator for
        """
        self.__init__(Random(seed))

    def __init__(self, rand: Random) -> None:
        """
        Creates a seeded perlin noise generator with the given Random

        @param rand Random to construct with
        """
        self.offsetX = rand.random() * 256
        self.offsetY = rand.random() * 256
        self.offsetZ = rand.random() * 256

        for i in range(256):
            self.perm[i] = rand.randint(0, 255)

        for i in range(256):
            pos = rand.randint(0, 256 - i) + i
            old = self.perm[i]

            self.perm[i] = self.perm[pos]
            self.perm[pos] = old
            self.perm[i + 256] = self.perm[i]

    @staticmethod
    def getNoise(x: float) -> float:
        """
        Computes and returns the 1D unseeded perlin noise for the given
        coordinates in 1D space

        @param x X coordinate
        @return Noise at given location, from range -1 to 1
        """
        return PerlinNoiseGenerator.instance.noise(x)

    @staticmethod
    def getNoise(x: float, y: float) -> float:
        """
        Computes and returns the 2D unseeded perlin noise for the given
        coordinates in 2D space

        @param x X coordinate
        @param y Y coordinate
        @return Noise at given location, from range -1 to 1
        """
        return PerlinNoiseGenerator.instance.noise(x, y)

    @staticmethod
    def getNoise(x: float, y: float, z: float) -> float:
        """
        Computes and returns the 3D unseeded perlin noise for the given
        coordinates in 3D space

        @param x X coordinate
        @param y Y coordinate
        @param z Z coordinate
        @return Noise at given location, from range -1 to 1
        """
        return PerlinNoiseGenerator.instance.noise(x, y, z)

    @staticmethod
    def getInstance() -> 'PerlinNoiseGenerator':
        """
        Gets the singleton unseeded instance of this generator

        @return Singleton
        """
        return PerlinNoiseGenerator.instance

    def noise(self, x: float, y: float, z: float) -> float:
        """
        Computes the noise value for the given coordinates.

        @param x X coordinate
        @param y Y coordinate
        @param z Z coordinate
        @return Computed noise value
        """
        pass  # Implementation omitted

    @staticmethod
    def getNoise(x: float, octaves: int, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 1D coordinates using the specified number of
        octaves and parameters

        @param x X-coordinate
        @param octaves Number of octaves to use
        @param frequency How much to alter the frequency by each octave
        @param amplitude How much to alter the amplitude by each octave
        @return Resulting noise
        """
        return PerlinNoiseGenerator.instance.noise(x, octaves, frequency, amplitude)

    @staticmethod
    def getNoise(x: float, y: float, octaves: int, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 2D coordinates using the specified number of
        octaves and parameters

        @param x X-coordinate
        @param y Y-coordinate
        @param octaves Number of octaves to use
        @param frequency How much to alter the frequency by each octave
        @param amplitude How much to alter the amplitude by each octave
        @return Resulting noise
        """
        return PerlinNoiseGenerator.instance.noise(x, y, octaves, frequency, amplitude)

    @staticmethod
    def getNoise(x: float, y: float, z: float, octaves: int, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        @param x X-coordinate
        @param y Y-coordinate
        @param z Z-coordinate
        @param octaves Number of octaves to use
        @param frequency How much to alter the frequency by each octave
        @param amplitude How much to alter the amplitude by each octave
        @return Resulting noise
        """
        return PerlinNoiseGenerator.instance.noise(x, y, z, octaves, frequency, amplitude)