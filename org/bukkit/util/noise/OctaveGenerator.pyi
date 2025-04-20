from typing import List
from org.bukkit.util.noise import NoiseGenerator

class OctaveGenerator:
    """
    Creates noise using unbiased octaves
    """

    octaves: List[NoiseGenerator]
    xScale: float
    yScale: float
    zScale: float

    def __init__(self, octaves: List[NoiseGenerator]) -> None:
        """
        Initializes the OctaveGenerator with the given octaves.

        :param octaves: The noise generators to use for creating noise.
        """
        ...

    def setScale(self, scale: float) -> None:
        """
        Sets the scale used for all coordinates passed to this generator.
        This is the equivalent to setting each coordinate to the specified value.

        :param scale: New value to scale each coordinate by
        """
        ...

    def getXScale(self) -> float:
        """
        Gets the scale used for each X-coordinates passed.

        :return: X scale
        """
        ...

    def setXScale(self, scale: float) -> None:
        """
        Sets the scale used for each X-coordinates passed.

        :param scale: New X scale
        """
        ...

    def getYScale(self) -> float:
        """
        Gets the scale used for each Y-coordinates passed.

        :return: Y scale
        """
        ...

    def setYScale(self, scale: float) -> None:
        """
        Sets the scale used for each Y-coordinates passed.

        :param scale: New Y scale
        """
        ...

    def getZScale(self) -> float:
        """
        Gets the scale used for each Z-coordinates passed.

        :return: Z scale
        """
        ...

    def setZScale(self, scale: float) -> None:
        """
        Sets the scale used for each Z-coordinates passed.

        :param scale: New Z scale
        """
        ...

    def getOctaves(self) -> List[NoiseGenerator]:
        """
        Gets a clone of the individual octaves used within this generator.

        :return: Clone of the individual octaves
        """
        ...

    def noise(self, x: float, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 1D coordinates using the specified number of
        octaves and parameters.

        :param x: X-coordinate
        :param frequency: How much to alter the frequency by each octave
        :param amplitude: How much to alter the amplitude by each octave
        :return: Resulting noise
        """
        ...

    def noise(self, x: float, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 1D coordinates using the specified number of
        octaves and parameters.

        :param x: X-coordinate
        :param frequency: How much to alter the frequency by each octave
        :param amplitude: How much to alter the amplitude by each octave
        :param normalized: If true, normalize the value to [-1, 1]
        :return: Resulting noise
        """
        ...

    def noise(self, x: float, y: float, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 2D coordinates using the specified number of
        octaves and parameters.

        :param x: X-coordinate
        :param y: Y-coordinate
        :param frequency: How much to alter the frequency by each octave
        :param amplitude: How much to alter the amplitude by each octave
        :return: Resulting noise
        """
        ...

    def noise(self, x: float, y: float, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 2D coordinates using the specified number of
        octaves and parameters.

        :param x: X-coordinate
        :param y: Y-coordinate
        :param frequency: How much to alter the frequency by each octave
        :param amplitude: How much to alter the amplitude by each octave
        :param normalized: If true, normalize the value to [-1, 1]
        :return: Resulting noise
        """
        ...

    def noise(self, x: float, y: float, z: float, frequency: float, amplitude: float) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters.

        :param x: X-coordinate
        :param y: Y-coordinate
        :param z: Z-coordinate
        :param frequency: How much to alter the frequency by each octave
        :param amplitude: How much to alter the amplitude by each octave
        :return: Resulting noise
        """
        ...

    def noise(self, x: float, y: float, z: float, frequency: float, amplitude: float, normalized: bool) -> float:
        """
        Generates noise for the 3D coordinates using the specified number of
        octaves and parameters.

        :param x: X-coordinate
        :param y: Y-coordinate
        :param z: Z-coordinate
        :param frequency: How much to alter the frequency by each octave
        :param amplitude: How much to alter the amplitude by each octave
        :param normalized: If true, normalize the value to [-1, 1]
        :return: Resulting noise
        """
        ...