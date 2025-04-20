from typing import Union

class NoiseGenerator:
    """
    Base class for all noise generators
    """

    perm: list[int]  # protected final int[] perm = new int[512];
    offsetX: float
    offsetY: float
    offsetZ: float

    @staticmethod
    def floor(x: float) -> int:
        """Speedy floor, faster than (int)Math.floor(x)

        Args:
            x: Value to floor

        Returns:
            Floored value
        """
        ...

    @staticmethod
    def fade(x: float) -> float:
        """Fade function for noise generation.

        Args:
            x: Input value

        Returns:
            Faded value
        """
        ...

    @staticmethod
    def lerp(x: float, y: float, z: float) -> float:
        """Linear interpolation function.

        Args:
            x: Interpolation factor
            y: Start value
            z: End value

        Returns:
            Interpolated value
        """
        ...

    @staticmethod
    def grad(hash: int, x: float, y: float, z: float) -> float:
        """Gradient function for noise generation.

        Args:
            hash: Hash value
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            Gradient value
        """
        ...

    def noise(self, x: float) -> float:
        """Computes and returns the 1D noise for the given coordinate in 1D space

        Args:
            x: X coordinate

        Returns:
            Noise at given location, from range -1 to 1
        """
        ...

    def noise(self, x: float, y: float) -> float:
        """Computes and returns the 2D noise for the given coordinates in 2D space

        Args:
            x: X coordinate
            y: Y coordinate

        Returns:
            Noise at given location, from range -1 to 1
        """
        ...

    def noise(self, x: float, y: float, z: float) -> float:
        """Computes and returns the 3D noise for the given coordinates in 3D space

        Args:
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            Noise at given location, from range -1 to 1
        """
        ...

    def noise(self, x: float, octaves: int, frequency: float, amplitude: float) -> float:
        """Generates noise for the 1D coordinates using the specified number of
        octaves and parameters

        Args:
            x: X-coordinate
            octaves: Number of octaves to use
            frequency: How much to alter the frequency by each octave
            amplitude: How much to alter the amplitude by each octave

        Returns:
            Resulting noise
        """
        ...

    def noise(self, x: float, octaves: int, frequency: float, amplitude: float, normalized: bool) -> float:
        """Generates noise for the 1D coordinates using the specified number of
        octaves and parameters

        Args:
            x: X-coordinate
            octaves: Number of octaves to use
            frequency: How much to alter the frequency by each octave
            amplitude: How much to alter the amplitude by each octave
            normalized: If true, normalize the value to [-1, 1]

        Returns:
            Resulting noise
        """
        ...

    def noise(self, x: float, y: float, octaves: int, frequency: float, amplitude: float) -> float:
        """Generates noise for the 2D coordinates using the specified number of
        octaves and parameters

        Args:
            x: X-coordinate
            y: Y-coordinate
            octaves: Number of octaves to use
            frequency: How much to alter the frequency by each octave
            amplitude: How much to alter the amplitude by each octave

        Returns:
            Resulting noise
        """
        ...

    def noise(self, x: float, y: float, octaves: int, frequency: float, amplitude: float, normalized: bool) -> float:
        """Generates noise for the 2D coordinates using the specified number of
        octaves and parameters

        Args:
            x: X-coordinate
            y: Y-coordinate
            octaves: Number of octaves to use
            frequency: How much to alter the frequency by each octave
            amplitude: How much to alter the amplitude by each octave
            normalized: If true, normalize the value to [-1, 1]

        Returns:
            Resulting noise
        """
        ...

    def noise(self, x: float, y: float, z: float, octaves: int, frequency: float, amplitude: float) -> float:
        """Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        Args:
            x: X-coordinate
            y: Y-coordinate
            z: Z-coordinate
            octaves: Number of octaves to use
            frequency: How much to alter the frequency by each octave
            amplitude: How much to alter the amplitude by each octave

        Returns:
            Resulting noise
        """
        ...

    def noise(self, x: float, y: float, z: float, octaves: int, frequency: float, amplitude: float, normalized: bool) -> float:
        """Generates noise for the 3D coordinates using the specified number of
        octaves and parameters

        Args:
            x: X-coordinate
            y: Y-coordinate
            z: Z-coordinate
            octaves: Number of octaves to use
            frequency: How much to alter the frequency by each octave
            amplitude: How much to alter the amplitude by each octave
            normalized: If true, normalize the value to [-1, 1]

        Returns:
            Resulting noise
        """
        ...