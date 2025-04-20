from typing import Protocol, Optional

from .chunk import Chunk
from org.bukkit import Location
from org.bukkit import Material
from .world import World
import org.bukkit.block_data import BlockData
from org.bukkit_data import MaterialData
from .metadatable import Metadatable


class BlockState(Metadatable, Protocol):
    """
    Represents a captured state of a block, which will not change
    automatically.
    <p>
    Unlike Block, which only one object can exist per coordinate, BlockState
    can exist multiple times for any given Block. Note that another plugin may
    change the state of the block and you will not know, or they may change the
    block to another type entirely, causing your BlockState to become invalid.
    """

    def get_block(self) -> Block:
        """
        Gets the block represented by this block state.

        @return: the block represented by this block state
        @raises IllegalStateException: if this block state is not placed
        """
        ...

    def get_data(self) -> MaterialData:
        """
        Gets the metadata for this block state.

        @return: block specific metadata
        """
        ...

    def get_block_data(self) -> BlockData:
        """
        Gets the data for this block state.

        @return: block specific data
        """
        ...

    def copy(self) -> BlockState:
        """
        Returns a copy of this BlockState as an unplaced BlockState.

        @return: a copy of the block state
        """
        ...

    def copy(self, location: Location) -> BlockState:
        """
        Copies the state to another block as an unplaced BlockState.

        @param location: the location to copy the block state to
        @return: the new block state
        """
        ...

    def get_type(self) -> Material:
        """
        Gets the type of this block state.

        @return: block type
        """
        ...

    def get_light_level(self) -> int:
        """
        Gets the current light level of the block represented by this block state.

        @return: the light level between 0-15
        @raises IllegalStateException: if this block state is not placed
        """
        ...

    def get_world(self) -> World:
        """
        Gets the world which contains the block represented by this block state.

        @return: the world containing the block represented by this block state
        @raises IllegalStateException: if this block state is not placed
        """
        ...

    def get_x(self) -> int:
        """
        Gets the x-coordinate of this block state.

        @return: x-coordinate
        """
        ...

    def get_y(self) -> int:
        """
        Gets the y-coordinate of this block state.

        @return: y-coordinate
        """
        ...

    def get_z(self) -> int:
        """
        Gets the z-coordinate of this block state.

        @return: z-coordinate
        """
        ...

    def get_location(self) -> Location:
        """
        Gets the location of this block state.
        <p>
        If this block state is not placed the location's world will be null!

        @return: the location
        """
        ...

    def get_location(self, loc: Optional[Location]) -> Optional[Location]:
        """
        Stores the location of this block state in the provided Location object.
        <p>
        If the provided Location is null this method does nothing and returns
        null.
        <p>
        If this block state is not placed the location's world will be null!

        @param loc: the location to copy into
        @return: The Location object provided or null
        """
        ...

    def get_chunk(self) -> Chunk:
        """
        Gets the chunk which contains the block represented by this block state.

        @return: the containing Chunk
        @raises IllegalStateException: if this block state is not placed
        """
        ...

    def set_data(self, data: MaterialData) -> None:
        """
        Sets the metadata for this block state.

        @param data: New block specific metadata
        """
        ...

    def set_block_data(self, data: BlockData) -> None:
        """
        Sets the data for this block state.

        @param data: New block specific data
        """
        ...

    def set_type(self, type: Material) -> None:
        """
        Sets the type of this block state.

        @param type: Material to change this block state to
        """
        ...

    def update(self) -> bool:
        """
        Attempts to update the block represented by this state, setting it to
        the new values as defined by this state.
        <p>
        This has the same effect as calling update(false). That is to say,
        this will not modify the state of a block if it is no longer the same
        type as it was when this state was taken. It will return false in this
        eventuality.

        @return: true if the update was successful, otherwise false
        @see: #update(boolean)
        """
        ...

    def update(self, force: bool) -> bool:
        """
        Attempts to update the block represented by this state, setting it to
        the new values as defined by this state.
        <p>
        This has the same effect as calling update(force, true). That is to
        say, this will trigger a physics update to surrounding blocks.

        @param force: true to forcefully set the state
        @return: true if the update was successful, otherwise false
        """
        ...

    def update(self, force: bool, apply_physics: bool) -> bool:
        """
        Attempts to update the block represented by this state, setting it to
        the new values as defined by this state.
        <p>
        If this state is not placed, this will have no effect and return true.
        <p>
        Unless force is true, this will not modify the state of a block if it
        is no longer the same type as it was when this state was taken. It will
        return false in this eventuality.
        <p>
        If force is true, it will set the type of the block to match the new
        state, set the state data and then return true.
        <p>
        If applyPhysics is true, it will trigger a physics update on
        surrounding blocks which could cause them to update or disappear.

        @param force: true to forcefully set the state
        @param apply_physics: false to cancel updating physics on surrounding
            blocks
        @return: true if the update was successful, otherwise false
        """
        ...

    def get_raw_data(self) -> int:
        """
        @return: The data as a raw byte.
        @deprecated: Magic value
        """
        ...

    def set_raw_data(self, data: int) -> None:
        """
        @param data: The new data value for the block.
        @deprecated: Magic value
        """
        ...

    def is_placed(self) -> bool:
        """
        Returns whether this state is placed in the world.
        <p>
        Some methods will not work if the block state isn't
        placed in the world.

        @return: whether the state is placed in the world
                or 'virtual' (e.g. on an itemstack)
        """
        ...