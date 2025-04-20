from typing import Collection, Optional

from .chunk import Chunk
from .fluid_collision_mode import FluidCollisionMode
from org.bukkit import Location
from org.bukkit import Material
from .translatable import Translatable
from .world import World
import org.bukkit.block_data import BlockData
from org.bukkit.entity import Entity
from .player import Player
from .item_stack import ItemStack
from .metadatable import Metadatable
from .bounding_box import BoundingBox
from .ray_trace_result import RayTraceResult
from .vector import Vector
from .voxel_shape import VoxelShape
import org.bukkit.block_face import BlockFace
import org.bukkit.block_state import BlockState
from .biome import Biome
from .piston_move_reaction import PistonMoveReaction

class Block(Metadatable, Translatable):
    """
    Represents a block. This is a live object, and only one Block may exist for
    any given location in a world. The state of the block may change
    concurrently to your own handling of it; use block.getState() to get a
    snapshot state of a block which will not be modified.

    Note that parts of this class which require access to the world at large
    (i.e. lighting and power) may not be able to be safely accessed during world
    generation when used in cases like BlockPhysicsEvent!!!!
    """

    def get_data(self) -> bytes:
        """
        Gets the metadata for this block

        :return: block specific metadata
        :deprecated: Magic value
        """
        ...

    def get_block_data(self) -> BlockData:
        """
        Gets the complete block data for this block

        :return: block specific data
        """
        ...

    def get_relative(self, mod_x: int, mod_y: int, mod_z: int) -> 'Block':
        """
        Gets the block at the given offsets

        :param modX: X-coordinate offset
        :param modY: Y-coordinate offset
        :param modZ: Z-coordinate offset
        :return: Block at the given offsets
        """
        ...

    def get_relative_face(self, face: BlockFace) -> 'Block':
        """
        Gets the block at the given face

        :param face: Face of this block to return
        :return: Block at the given face
        """
        ...

    def get_relative_face_distance(self, face: BlockFace, distance: int) -> 'Block':
        """
        Gets the block at the given distance of the given face

        :param face: Face of this block to return
        :param distance: Distance to get the block at
        :return: Block at the given face
        """
        ...

    def get_type(self) -> Material:
        """
        Gets the type of this block

        :return: block type
        """
        ...

    def get_light_level(self) -> bytes:
        """
        Gets the light level between 0-15

        :return: light level
        """
        ...

    def get_light_from_sky(self) -> bytes:
        """
        Get the amount of light at this block from the sky.

        :return: Sky light level
        """
        ...

    def get_light_from_blocks(self) -> bytes:
        """
        Get the amount of light at this block from nearby blocks.

        :return: Block light level
        """
        ...

    def get_world(self) -> World:
        """
        Gets the world which contains this Block

        :return: World containing this block
        """
        ...

    def get_x(self) -> int:
        """
        Gets the x-coordinate of this block

        :return: x-coordinate
        """
        ...

    def get_y(self) -> int:
        """
        Gets the y-coordinate of this block

        :return: y-coordinate
        """
        ...

    def get_z(self) -> int:
        """
        Gets the z-coordinate of this block

        :return: z-coordinate
        """
        ...

    def get_location(self) -> Location:
        """
        Gets the Location of the block

        :return: Location of block
        """
        ...

    def get_location_optional(self, loc: Optional[Location]) -> Optional[Location]:
        """
        Stores the location of the block in the provided Location object.

        :param loc: the location to copy into
        :return: The Location object provided or null
        """
        ...

    def get_chunk(self) -> Chunk:
        """
        Gets the chunk which contains this block

        :return: Containing Chunk
        """
        ...

    def set_block_data(self, data: BlockData) -> None:
        """
        Sets the complete data for this block

        :param data: new block specific data
        """
        ...

    def set_block_data_with_physics(self, data: BlockData, apply_physics: bool) -> None:
        """
        Sets the complete data for this block

        :param data: new block specific data
        :param apply_physics: false to cancel physics from the changed block
        """
        ...

    def set_type(self, type: Material) -> None:
        """
        Sets the type of this block

        :param type: Material to change this block to
        """
        ...

    def set_type_with_physics(self, type: Material, apply_physics: bool) -> None:
        """
        Sets the type of this block

        :param type: Material to change this block to
        :param apply_physics: False to cancel physics on the changed block.
        """
        ...

    def get_face(self, block: 'Block') -> Optional[BlockFace]:
        """
        Gets the face relation of this block compared to the given block.

        :param block: Block to compare against this block
        :return: BlockFace of this block which has the requested block, or null
        """
        ...

    def get_state(self) -> BlockState:
        """
        Captures the current state of this block.

        :return: BlockState with the current state of this block.
        """
        ...

    def get_biome(self) -> Biome:
        """
        Returns the biome that this block resides in

        :return: Biome type containing this block
        """
        ...

    def set_biome(self, bio: Biome) -> None:
        """
        Sets the biome that this block resides in

        :param bio: new Biome type for this block
        """
        ...

    def is_block_powered(self) -> bool:
        """
        Returns true if the block is being powered by Redstone.

        :return: True if the block is powered.
        """
        ...

    def is_block_indirectly_powered(self) -> bool:
        """
        Returns true if the block is being indirectly powered by Redstone.

        :return: True if the block is indirectly powered.
        """
        ...

    def is_block_face_powered(self, face: BlockFace) -> bool:
        """
        Returns true if the block face is being powered by Redstone.

        :param face: The block face
        :return: True if the block face is powered.
        """
        ...

    def is_block_face_indirectly_powered(self, face: BlockFace) -> bool:
        """
        Returns true if the block face is being indirectly powered by Redstone.

        :param face: The block face
        :return: True if the block face is indirectly powered.
        """
        ...

    def get_block_power_face(self, face: BlockFace) -> int:
        """
        Returns the redstone power being provided to this block face

        :param face: the face of the block to query or BlockFace.SELF for the block itself
        :return: The power level.
        """
        ...

    def get_block_power(self) -> int:
        """
        Returns the redstone power being provided to this block

        :return: The power level.
        """
        ...

    def is_empty(self) -> bool:
        """
        Checks if this block is empty.

        :return: true if this block is empty
        """
        ...

    def is_liquid(self) -> bool:
        """
        Checks if this block is liquid.

        :return: true if this block is liquid
        """
        ...

    def get_temperature(self) -> float:
        """
        Gets the temperature of this block.

        :return: Temperature of this block
        """
        ...

    def get_humidity(self) -> float:
        """
        Gets the humidity of the biome of this block

        :return: Humidity of this block
        """
        ...

    def get_piston_move_reaction(self) -> PistonMoveReaction:
        """
        Returns the reaction of the block when moved by a piston

        :return: reaction
        """
        ...

    def break_naturally(self) -> bool:
        """
        Breaks the block and spawns items as if a player had digged it regardless of the tool.

        :return: true if the block was destroyed
        """
        ...

    def break_naturally_with_tool(self, tool: Optional[ItemStack]) -> bool:
        """
        Breaks the block and spawns items as if a player had digged it with a specific tool

        :param tool: The tool or item in hand used for digging
        :return: true if the block was destroyed
        """
        ...

    def apply_bone_meal(self, face: BlockFace) -> bool:
        """
        Simulate bone meal application to this block (if possible).

        :param face: the face on which bonemeal should be applied
        :return: true if the block was bonemealed, false otherwise
        """
        ...

    def get_drops(self) -> Collection[ItemStack]:
        """
        Returns a list of items which would drop by destroying this block

        :return: a list of dropped items for this type of block
        """
        ...

    def get_drops_with_tool(self, tool: Optional[ItemStack]) -> Collection[ItemStack]:
        """
        Returns a list of items which would drop by destroying this block with a specific tool

        :param tool: The tool or item in hand used for digging
        :return: a list of dropped items for this type of block
        """
        ...

    def get_drops_with_tool_entity(self, tool: ItemStack, entity: Optional[Entity]) -> Collection[ItemStack]:
        """
        Returns a list of items which would drop by the entity destroying this block with a specific tool

        :param tool: The tool or item in hand used for digging
        :param entity: the entity destroying the block
        :return: a list of dropped items for this type of block
        """
        ...

    def is_preferred_tool(self, tool: ItemStack) -> bool:
        """
        Returns if the given item is a preferred choice to break this Block.

        :param tool: The tool or item used for breaking this block
        :return: true if the tool is preferred for breaking this block.
        """
        ...

    def get_break_speed(self, player: Player) -> float:
        """
        Gets the speed at which the given player would break this block, taking into account tools, potion effects, whether or not the player is in water, enchantments, etc.

        :param player: player breaking the block
        :return: the speed at which the player breaks this block
        """
        ...

    def is_passable(self) -> bool:
        """
        Checks if this block is passable.

        :return: <code>true</code> if passable
        """
        ...

    def ray_trace(self, start: Location, direction: Vector, max_distance: float, fluid_collision_mode: FluidCollisionMode) -> Optional[RayTraceResult]:
        """
        Performs a ray trace that checks for collision with this specific block in its current state using its precise collision shape.

        :param start: the start location
        :param direction: the ray direction
        :param max_distance: the maximum distance
        :param fluid_collision_mode: the fluid collision mode
        :return: the ray trace hit result, or <code>null</code> if there is no hit
        """
        ...

    def get_bounding_box(self) -> BoundingBox:
        """
        Gets the approximate bounding box for this block.

        :return: the approximate bounding box of the block
        """
        ...

    def get_collision_shape(self) -> VoxelShape:
        """
        Gets the collision shape of this block.

        :return: a {@link VoxelShape} representing the collision shape of this block.
        """
        ...

    def can_place(self, data: BlockData) -> bool:
        """
        Checks if this block is a valid placement location for the specified block data.

        :param data: the block data to check
        :return: <code>true</code> if the block data can be placed here
        """
        ...