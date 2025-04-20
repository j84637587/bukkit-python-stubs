from typing import Protocol
from org.bukkit.block.structure import Mirror, StructureRotation, UsageMode
from org.bukkit.entity import LivingEntity
from org.bukkit.util import BlockVector

class Structure(Protocol):
    """
    Represents a structure block that can save and load blocks from a file. They
    can only be used by OPs, and are not obtainable in survival.
    """

    def get_structure_name(self) -> str:
        """
        The name of this structure.

        :return: structure name
        """
        ...

    def set_structure_name(self, name: str) -> None:
        """
        Set the name of this structure. This is case-sensitive. The name of the
        structure in the {@link UsageMode#SAVE} structure block MUST match the
        name within the {@link UsageMode#CORNER} block or the size calculation
        will fail.

        :param name: the case-sensitive name of this structure
        """
        ...

    def get_author(self) -> str:
        """
        Get the name of who created this structure.

        :return: the name of whoever created this structure.
        """
        ...

    def set_author(self, author: str) -> None:
        """
        Set the name of whoever created this structure.

        :param author: whoever created this structure (not empty)
        """
        ...

    def set_author_entity(self, living_entity: LivingEntity) -> None:
        """
        Set the name of whoever created this structure using a
        {@link LivingEntity}.

        :param living_entity: the entity who created this structure
        """
        ...

    def get_relative_position(self) -> BlockVector:
        """
        The relative position of the structure outline based on the position of
        the structure block. Maximum allowed distance is 48 blocks in any
        direction.

        :return: a Location which contains the relative distance this structure is
        from the structure block.
        """
        ...

    def set_relative_position(self, vector: BlockVector) -> None:
        """
        Set the relative position from the structure block. Maximum allowed
        distance is 48 blocks in any direction.

        :param vector: the {@link BlockVector} containing the relative origin
        coordinates of this structure.
        """
        ...

    def get_structure_size(self) -> BlockVector:
        """
        The distance to the opposite corner of this structure. The maximum
        structure size is 48x48x48. When a structure has successfully been
        calculated (i.e. it is within the maximum allowed distance) a white
        border surrounds the structure.

        :return: a {@link BlockVector} which contains the total size of the
        structure.
        """
        ...

    def set_structure_size(self, vector: BlockVector) -> None:
        """
        Set the maximum size of this structure from the origin point. Maximum
        allowed size is 48x48x48.

        :param vector: the {@link BlockVector} containing the size of this
        structure, based off of the origin coordinates.
        """
        ...

    def set_mirror(self, mirror: Mirror) -> None:
        """
        Sets the mirroring of the structure.

        :param mirror: the new mirroring method
        """
        ...

    def get_mirror(self) -> Mirror:
        """
        How this structure is mirrored.

        :return: the current mirroring method
        """
        ...

    def set_rotation(self, rotation: StructureRotation) -> None:
        """
        Set how this structure is rotated.

        :param rotation: the new rotation
        """
        ...

    def get_rotation(self) -> StructureRotation:
        """
        Get how this structure is rotated.

        :return: the new rotation
        """
        ...

    def set_usage_mode(self, mode: UsageMode) -> None:
        """
        Set the {@link UsageMode} of this structure block.

        :param mode: the new mode to set.
        """
        ...

    def get_usage_mode(self) -> UsageMode:
        """
        Get the {@link UsageMode} of this structure block.

        :return: the mode this block is currently in.
        """
        ...

    def set_ignore_entities(self, ignore_entities: bool) -> None:
        """
        While in {@link UsageMode#SAVE} mode, this will ignore any entities when
        saving the structure.
        <br>
        While in {@link UsageMode#LOAD} mode this will ignore any entities that
        were saved to file.

        :param ignore_entities: the flag to set
        """
        ...

    def is_ignore_entities(self) -> bool:
        """
        Get if this structure block should ignore entities.

        :return: true if the appropriate {@link UsageMode} should ignore entities.
        """
        ...

    def set_show_air(self, show_air: bool) -> None:
        """
        Set if the structure outline should show air blocks.

        :param show_air: if the structure block should show air blocks
        """
        ...

    def is_show_air(self) -> bool:
        """
        Check if this structure block is currently showing all air blocks

        :return: true if the structure block is showing all air blocks
        """
        ...

    def set_bounding_box_visible(self, show_bounding_box: bool) -> None:
        """
        Set if this structure box should show the bounding box.

        :param show_bounding_box: if the structure box should be shown
        """
        ...

    def is_bounding_box_visible(self) -> bool:
        """
        Get if this structure block is currently showing the bounding box.

        :return: true if the bounding box is shown
        """
        ...

    def set_integrity(self, integrity: float) -> None:
        """
        Set the integrity of the structure. Integrity must be between 0.0 and 1.0
        Lower integrity values will result in more blocks being removed when
        loading a structure. Integrity and {@link #getSeed()} are used together
        to determine which blocks are randomly removed to mimic "decay."

        :param integrity: the integrity of this structure
        """
        ...

    def get_integrity(self) -> float:
        """
        Get the integrity of this structure.

        :return: the integrity of this structure
        """
        ...

    def set_seed(self, seed: int) -> None:
        """
        The seed used to determine which blocks will be removed upon loading.
        {@link #getIntegrity()} and seed are used together to determine which
        blocks are randomly removed to mimic "decay."

        :param seed: the seed used to determine how many blocks will be removed
        """
        ...

    def get_seed(self) -> int:
        """
        The seed used to determine how many blocks are removed upon loading of
        this structure.

        :return: the seed used
        """
        ...

    def set_metadata(self, metadata: str) -> None:
        """
        Only applicable while in {@link UsageMode#DATA}. Metadata are specific
        functions that can be applied to the structure location. Consult the
        <a href="https://minecraft.wiki/w/Structure_Block#Data">Minecraft
        wiki</a> for more information.

        :param metadata: the function to perform on the selected location
        """
        ...

    def get_metadata(self) -> str:
        """
        Get the metadata function this structure block will perform when
        activated. Consult the
        <a href="https://minecraft.wiki/w/Structure_Block#Data">Minecraft
        Wiki</a> for more information.

        :return: the function that will be performed when this block is activated
        """
        ...