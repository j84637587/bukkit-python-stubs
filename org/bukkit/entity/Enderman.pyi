from org.bukkit.block.data import BlockData
from org.bukkit.material import MaterialData
from org.jetbrains.annotations import NotNull, Nullable
from org.bukkit.entity import Monster
from org.bukkit.entity import Entity

"""
Represents an Enderman.
"""
class Enderman(Monster):

    """
    Gets the id and data of the block that the Enderman is carrying.

    @return MaterialData containing the id and data of the block
    """
        def get_carried_material(self) -> MaterialData: ...

    """
    Sets the id and data of the block that the Enderman is carrying.

    @param material data to set the carried block to
    """
    def set_carried_material(self, material: @NotNull MaterialData) -> None: ...

    """
    Gets the data of the block that the Enderman is carrying.

    @return BlockData containing the carried block, or null if none
    """
        def get_carried_block(self) -> BlockData: ...

    """
    Sets the data of the block that the Enderman is carrying.

    @param blockData data to set the carried block to, or null to remove
    """
    def set_carried_block(self, blockData: @Nullable BlockData) -> None: ...

    """
    Randomly teleports the Enderman in a 64x64x64 block cuboid region.
    <p>
    If the randomly selected point is in the ground, the point is moved 1 block
    down until air is found or until it goes under
    {@link org.bukkit.World#getMinHeight()}.
    <p>
    This method will return false if this Enderman is not alive, or if the
    teleport location was obstructed, or if the teleport location is in water.

    @return true if the teleport succeeded.
    """
    def teleport(self) -> bool: ...

    """
    Randomly teleports the Enderman towards the given <code>entity</code>.
    <p>
    The point is selected by drawing a vector between this enderman and the
    given <code>entity</code>. That vector's length is set to 16 blocks.
    That point is then moved within a 8x8x8 cuboid region. If the randomly
    selected point is in the ground, the point is moved 1 block down until
    air is found or until it goes under
    {@link org.bukkit.World#getMinHeight()}.
    <p>
    This method will return false if this Enderman is not alive, or if the
    teleport location was obstructed, or if the teleport location is in water.

    @param entity The entity to teleport towards.
    @return true if the teleport succeeded.
    """
    def teleport_towards(self, entity: @NotNull Entity) -> bool: ...