from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Literal

class Door(MaterialData):
    """
    Represents a door.

    This class was previously deprecated, but has been retrofitted to
    work with modern doors. Some methods are undefined dependant on <code>isTopHalf()</code>
    due to Minecraft's internal representation of doors.

    @see Material.LEGACY_WOODEN_DOOR
    @see Material.LEGACY_IRON_DOOR_BLOCK
    @see Material.LEGACY_SPRUCE_DOOR
    @see Material.LEGACY_BIRCH_DOOR
    @see Material.LEGACY_JUNGLE_DOOR
    @see Material.LEGACY_ACACIA_DOOR
    @see Material.LEGACY_DARK_OAK_DOOR

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    """
    
    def __init__(self) -> None:
        """
        @deprecated Artifact of old API, equivalent to new <code>Door(Material.LEGACY_WOODEN_DOOR);</code>
        """
        super().__init__(Material.LEGACY_WOODEN_DOOR)

    def __init__(self, type: Material) -> None:
        pass

    def __init__(self, type: Material, face: BlockFace) -> None:
        self.__init__(type, face, False)

    def __init__(self, type: Material, face: BlockFace, isOpen: bool) -> None:
        pass

    def __init__(self, type: Material, isHingeRight: bool) -> None:
        pass

    def __init__(self, species: TreeSpecies, face: BlockFace) -> None:
        self.__init__(self.getWoodDoorOfSpecies(species), face, False)

    def __init__(self, species: TreeSpecies, face: BlockFace, isOpen: bool) -> None:
        self.__init__(self.getWoodDoorOfSpecies(species), face, isOpen)

    def __init__(self, species: TreeSpecies, isHingeRight: bool) -> None:
        self.__init__(self.getWoodDoorOfSpecies(species), isHingeRight)

    def __init__(self, type: Material, data: int) -> None:
        """
        @param type the type
        @param data the raw data value
        @deprecated Magic value
        """
        pass

    @staticmethod
    def getWoodDoorOfSpecies(species: TreeSpecies) -> Material:
        """
        Returns the item type of a wooden door for the given tree species.

        @param species The species of wood door required.
        @return The item type for the given species.

        @see Material.LEGACY_WOODEN_DOOR
        @see Material.LEGACY_SPRUCE_DOOR
        @see Material.LEGACY_BIRCH_DOOR
        @see Material.LEGACY_JUNGLE_DOOR
        @see Material.LEGACY_ACACIA_DOOR
        @see Material.LEGACY_DARK_OAK_DOOR
        """
        pass

    def isOpen(self) -> bool:
        """
        Result is undefined if <code>isTopHalf()</code> is true.
        """
        pass

    def setOpen(self, isOpen: bool) -> None:
        """
        Set whether the door is open. Undefined if <code>isTopHalf()</code> is true.
        """
        pass

    def isTopHalf(self) -> bool:
        """
        @return whether this is the top half of the door
        """
        pass

    def setTopHalf(self, isTopHalf: bool) -> None:
        """
        Configure this part of the door to be either the top or the bottom half

        @param isTopHalf True to make it the top half.
        """
        pass

    def getHingeCorner(self) -> BlockFace:
        """
        @return BlockFace.SELF
        @deprecated This method should not be used; use hinge and facing accessors instead.
        """
        pass

    def toString(self) -> str:
        """
        @return string representation of the door
        """
        pass

    def setFacingDirection(self, face: BlockFace) -> None:
        """
        Set the direction that this door should is facing.

        Undefined if <code>isTopHalf()</code> is true.

        @param face the direction
        """
        pass

    def getFacing(self) -> BlockFace:
        """
        Get the direction that this door is facing.

        Undefined if <code>isTopHalf()</code> is true.

        @return the direction
        """
        pass

    def getHinge(self) -> bool:
        """
        Returns the side of the door the hinge is on.

        Undefined if <code>isTopHalf()</code> is false.

        @return false for left hinge, true for right hinge
        """
        pass

    def setHinge(self, isHingeRight: bool) -> None:
        """
        Set whether the hinge is on the left or right side. Left is false, right is true.

        Undefined if <code>isTopHalf()</code> is false.

        @param isHingeRight True if the hinge is on the right hand side, false if the hinge is on the left hand side.
        """
        pass

    def clone(self) -> 'Door':
        """
        @return a clone of this door
        """
        pass