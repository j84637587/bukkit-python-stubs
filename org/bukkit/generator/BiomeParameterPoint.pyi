from typing import Protocol

class BiomeParameterPoint(Protocol):
    """
    Represents the biome noise parameters which may be passed to a world
    generator.
    """

    def get_temperature(self) -> float:
        """
        Gets the temperature of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns:
            The temperature of the biome at this point
        """
        ...

    def get_max_temperature(self) -> float:
        """
        Gets the maximum temperature that is possible.

        Returns:
            The maximum temperature
        """
        ...

    def get_min_temperature(self) -> float:
        """
        Gets the minimum temperature that is possible.

        Returns:
            The minimum temperature
        """
        ...

    def get_humidity(self) -> float:
        """
        Gets the humidity of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns:
            The humidity of the biome at this point
        """
        ...

    def get_max_humidity(self) -> float:
        """
        Gets the maximum humidity that is possible.

        Returns:
            The maximum humidity
        """
        ...

    def get_min_humidity(self) -> float:
        """
        Gets the minimum humidity that is possible.

        Returns:
            The minimum humidity
        """
        ...

    def get_continentalness(self) -> float:
        """
        Gets the continentalness of the biome at this point that is suggested by
        the NoiseGenerator.

        Returns:
            The continentalness of the biome at this point
        """
        ...

    def get_max_continentalness(self) -> float:
        """
        Gets the maximum continentalness that is possible.

        Returns:
            The maximum continentalness
        """
        ...

    def get_min_continentalness(self) -> float:
        """
        Gets the minimum continentalness that is possible.

        Returns:
            The minimum continentalness
        """
        ...

    def get_erosion(self) -> float:
        """
        Gets the erosion of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns:
            The erosion of the biome at this point
        """
        ...

    def get_max_erosion(self) -> float:
        """
        Gets the maximum erosion that is possible.

        Returns:
            The maximum erosion
        """
        ...

    def get_min_erosion(self) -> float:
        """
        Gets the minimum erosion that is possible.

        Returns:
            The minimum erosion
        """
        ...

    def get_depth(self) -> float:
        """
        Gets the depth of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns:
            The depth of the biome at this point
        """
        ...

    def get_max_depth(self) -> float:
        """
        Gets the maximum depth that is possible.

        Returns:
            The maximum depth
        """
        ...

    def get_min_depth(self) -> float:
        """
        Gets the minimum depth that is possible.

        Returns:
            The minimum depth
        """
        ...

    def get_weirdness(self) -> float:
        """
        Gets the weirdness of the biome at this point that is suggested by the
        NoiseGenerator.

        Returns:
            The weirdness of the biome at this point
        """
        ...

    def get_max_weirdness(self) -> float:
        """
        Gets the maximum weirdness that is possible.

        Returns:
            The maximum weirdness
        """
        ...

    def get_min_weirdness(self) -> float:
        """
        Gets the minimum weirdness that is possible.

        Returns:
            The minimum weirdness
        """
        ...