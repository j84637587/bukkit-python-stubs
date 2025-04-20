from typing import List
from org.bukkit.block import Biome
from org.jetbrains.annotations import NotNull

class BiomeProvider:
    """Class for providing biomes."""

        def get_biome(self, world_info: 'WorldInfo', x: int, y: int, z: int) -> Biome:
        """Return the Biome which should be present at the provided location.

        Notes:
        This method must be completely thread safe and able to handle
        multiple concurrent callers.

        This method should only return biomes which are present in the list
        returned by get_biomes(WorldInfo)

        This method should never return Biome.CUSTOM.

        Args:
            world_info: The world info of the world the biome will be used for
            x: The X-coordinate from world origin
            y: The Y-coordinate from world origin
            z: The Z-coordinate from world origin

        Returns:
            Biome for the given location
        """
        ...

        def get_biome(self, world_info: 'WorldInfo', x: int, y: int, z: int, biome_parameter_point: 'BiomeParameterPoint') -> Biome:
        """Return the Biome which should be present at the provided location.

        Notes:
        This method must be completely thread safe and able to handle
        multiple concurrent callers.

        This method should only return biomes which are present in the list
        returned by get_biomes(WorldInfo)

        This method should never return Biome.CUSTOM.
        Only this method is called if both this and
        get_biome(WorldInfo, int, int, int) are overridden.

        Args:
            world_info: The world info of the world the biome will be used for
            x: The X-coordinate from world origin
            y: The Y-coordinate from world origin
            z: The Z-coordinate from world origin
            biome_parameter_point: The parameter point that is provided by default
                                  for this location (contains temperature, humidity,
                                  continentalness, erosion, depth and weirdness)

        Returns:
            Biome for the given location
        """
        return self.get_biome(world_info, x, y, z)

        def get_biomes(self, world_info: 'WorldInfo') -> List[Biome]:
        """Returns a list with every biome the BiomeProvider will use for
        the given world.

        Notes:
        This method only gets called once, when the world is loaded. Returning
        another list or modifying the values from the initial returned list later
        one, are not respected.

        This method should never return a list which contains
        Biome.CUSTOM.

        Args:
            world_info: The world info of the world the list will be used for

        Returns:
            A list with every biome the BiomeProvider uses
        """
        ...