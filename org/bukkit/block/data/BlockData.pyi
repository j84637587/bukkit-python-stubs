from org.bukkit import Color
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit import Server
from org.bukkit import SoundGroup
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.block import BlockState
from org.bukkit.block import BlockSupport
from org.bukkit.block import PistonMoveReaction
from org.bukkit.block.structure import Mirror
from org.bukkit.block.structure import StructureRotation
from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import ApiStatus
from org.jetbrains.annotations import NotNull
from org.jetbrains.annotations import Nullable
from typing import Protocol

class BlockData(Protocol):
    """
    BlockData interface representing block data in the game.
    """

        def get_material(self) -> Material:
        """
        Get the Material represented by this block data.
        """
        ...

        def get_as_string(self) -> str:
        """
        Gets a string, which when passed into a method such as
        Server#createBlockData(java.lang.String) will unambiguously
        recreate this instance.
        """
        ...

        def get_as_string(self, hide_unspecified: bool) -> str:
        """
        Gets a string, which when passed into a method such as
        Server#createBlockData(java.lang.String) will recreate this or a
        similar instance where unspecified states (if any) may be optionally
        omitted.
        """
        ...

        def merge(self, data: BlockData) -> BlockData:
        """
        Merges all explicitly set states from the given data with this BlockData.
        """
        ...

    def matches(self, data: Nullable[BlockData]) -> bool:
        """
        Checks if the specified BlockData matches this block data.
        """
        ...

        def clone(self) -> BlockData:
        """
        Returns a copy of this BlockData.
        """
        ...

        def get_sound_group(self) -> SoundGroup:
        """
        Gets the block's SoundGroup which can be used to get its step
        sound, hit sound, and others.
        """
        ...

    def get_light_emission(self) -> int:
        """
        Get the amount of light emitted by this state when in the world.
        """
        ...

    def is_occluding(self) -> bool:
        """
        Check whether or not this state will occlude other blocks.
        """
        ...

    def requires_correct_tool_for_drops(self) -> bool:
        """
        Check whether or not this state requires a specific item to be used to drop
        items when broken.
        """
        ...

    def is_preferred_tool(self, tool: ItemStack) -> bool:
        """
        Returns if the given item is a preferred choice to break this Block.
        """
        ...

        def get_piston_move_reaction(self) -> PistonMoveReaction:
        """
        Returns the reaction of the block when moved by a piston.
        """
        ...

    def is_supported(self, block: Block) -> bool:
        """
        Checks if this state would be properly supported if it were placed at
        the given Block.
        """
        ...

    def is_supported(self, location: Location) -> bool:
        """
        Checks if this state would be properly supported if it were placed at
        the block at the given Location.
        """
        ...

    def is_face_sturdy(self, face: BlockFace, support: BlockSupport) -> bool:
        """
        Checks if a state's BlockFace is capable of providing a given level
        of BlockSupport for neighbouring block states.
        """
        ...

        def get_map_color(self) -> Color:
        """
        Gets the color this block should appear as when rendered on a map.
        """
        ...

        def get_placement_material(self) -> Material:
        """
        Gets the material that a player would use to place this block.
        """
        ...

    def rotate(self, rotation: StructureRotation) -> None:
        """
        Rotates this blockdata by the specified StructureRotation.
        """
        ...

    def mirror(self, mirror: Mirror) -> None:
        """
        Mirrors this blockdata using the specified Mirror.
        """
        ...

    def copy_to(self, other: BlockData) -> None:
        """
        Copies all applicable properties from this BlockData to the provided
        BlockData.
        """
        ...

            def create_block_state(self) -> BlockState:
        """
        Creates a new default BlockState for this type of Block, not
        bound to a location.
        """
        ...