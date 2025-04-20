from org.bukkit import Material
from org.bukkit import TreeSpecies
from typing import Protocol, Literal

class Boat(Protocol):
    """
    Represents a boat entity.
    """

    def getWoodType(self) -> TreeSpecies:
        """
        Gets the wood type of the boat.

        Returns:
            TreeSpecies: the wood type
        """
        ...

    def setWoodType(self, species: TreeSpecies) -> None:
        """
        Sets the wood type of the boat.

        Args:
            species (TreeSpecies): the new wood type
        """
        ...

    def getBoatType(self) -> 'Boat.Type':
        """
        Gets the type of the boat.

        Returns:
            Boat.Type: the boat type
        """
        ...

    def setBoatType(self, type: 'Boat.Type') -> None:
        """
        Sets the type of the boat.

        Args:
            type (Boat.Type): the new type
        """
        ...

    def getMaxSpeed(self) -> float:
        """
        Gets the maximum speed of a boat. The speed is unrelated to the
        velocity.

        Returns:
            float: The max speed.
        """
        ...

    def setMaxSpeed(self, speed: float) -> None:
        """
        Sets the maximum speed of a boat. Must be nonnegative. Default is 0.4D.

        Args:
            speed (float): The max speed.
        """
        ...

    def getOccupiedDeceleration(self) -> float:
        """
        Gets the deceleration rate (newSpeed = curSpeed * rate) of occupied
        boats. The default is 0.2.

        Returns:
            float: The rate of deceleration
        """
        ...

    def setOccupiedDeceleration(self, rate: float) -> None:
        """
        Sets the deceleration rate (newSpeed = curSpeed * rate) of occupied
        boats. Setting this to a higher value allows for quicker acceleration.
        The default is 0.2.

        Args:
            rate (float): deceleration rate
        """
        ...

    def getUnoccupiedDeceleration(self) -> float:
        """
        Gets the deceleration rate (newSpeed = curSpeed * rate) of unoccupied
        boats. The default is -1. Values below 0 indicate that no additional
        deceleration is imposed.

        Returns:
            float: The rate of deceleration
        """
        ...

    def setUnoccupiedDeceleration(self, rate: float) -> None:
        """
        Sets the deceleration rate (newSpeed = curSpeed * rate) of unoccupied
        boats. Setting this to a higher value allows for quicker deceleration
        of boats when a player disembarks. The default is -1. Values below 0
        indicate that no additional deceleration is imposed.

        Args:
            rate (float): deceleration rate
        """
        ...

    def getWorkOnLand(self) -> bool:
        """
        Get whether boats can work on land.

        Returns:
            bool: whether boats can work on land
        """
        ...

    def setWorkOnLand(self, workOnLand: bool) -> None:
        """
        Set whether boats can work on land.

        Args:
            workOnLand (bool): whether boats can work on land
        """
        ...

    def getStatus(self) -> 'Boat.Status':
        """
        Gets the status of the boat.

        Returns:
            Boat.Status: the status
        """
        ...


class BoatType:
    """
    Represents the type of boats.
    """

    OAK: Literal['OAK'] = 'OAK'
    SPRUCE: Literal['SPRUCE'] = 'SPRUCE'
    BIRCH: Literal['BIRCH'] = 'BIRCH'
    JUNGLE: Literal['JUNGLE'] = 'JUNGLE'
    ACACIA: Literal['ACACIA'] = 'ACACIA'
    CHERRY: Literal['CHERRY'] = 'CHERRY'
    DARK_OAK: Literal['DARK_OAK'] = 'DARK_OAK'
    MANGROVE: Literal['MANGROVE'] = 'MANGROVE'
    BAMBOO: Literal['BAMBOO'] = 'BAMBOO'

    def getMaterial(self) -> Material:
        """
        Gets the material of the boat type.

        Returns:
            Material: a material
        """
        ...


class BoatStatus:
    """
    Represents the status of the boat.
    """

    IN_WATER: Literal['IN_WATER'] = 'IN_WATER'
    UNDER_WATER: Literal['UNDER_WATER'] = 'UNDER_WATER'
    UNDER_FLOWING_WATER: Literal['UNDER_FLOWING_WATER'] = 'UNDER_FLOWING_WATER'
    ON_LAND: Literal['ON_LAND'] = 'ON_LAND'
    IN_AIR: Literal['IN_AIR'] = 'IN_AIR'