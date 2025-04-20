from typing import Collection, Optional
from org.bukkit.entity import LivingEntity
from org.bukkit.util import BoundingBox

class Conduit(TileState):
    """
    Represents a captured state of a conduit.
    """

    def is_active(self) -> bool:
        """
        Checks whether or not this conduit is active.
        A conduit is considered active if there are at least 16 valid frame
        blocks surrounding it and the conduit is surrounded by a 3x3x3 area of
        water source blocks (or waterlogged blocks), at which point its animation
        will activate, start spinning, and apply effects to nearby players.

        @return: true if active, false otherwise
        """
        ...

    def is_hunting(self) -> bool:
        """
        Get whether or not this conduit is actively hunting for nearby hostile
        creatures.
        A conduit will hunt if it is active (see {@link #isActive()}) and its
        frame is complete (it is surrounded by at least 42 valid frame blocks).
        While hunting, the {@link #getTarget()
        conduit's target}, if within its {@link #getHuntingArea() hunting area},
        will be damaged every 2 seconds.

        @return: true if hunting, false otherwise
        """
        ...

    def get_frame_blocks(self) -> Collection['Block']:
        """
        Get a {@link Collection} of all {@link Block Blocks} that make up the
        frame of this conduit. The returned collection will contain only blocks
        that match the types required by the conduit to make up a valid frame,
        not the blocks at which the conduit is searching,
        meaning it will be of variable size depending on how many valid frames
        are surrounding the conduit at the time of invocation.

        @return: the frame blocks
        """
        ...

    def get_frame_block_count(self) -> int:
        """
        Get the amount of valid frame blocks that are currently surrounding the
        conduit.

        @return: the frame block count
        """
        ...

    def get_range(self) -> int:
        """
        Get the range (measured in blocks) within which players will receive the
        conduit's benefits.

        @return: the conduit range
        """
        ...

    def set_target(self, target: Optional[LivingEntity]) -> bool:
        """
        Set the conduit's hunting target.
        Note that the value set by this method may be overwritten by the
        conduit's periodic hunting logic. If the target is ever set to
        null, the conduit will continue to look for a new target.
        Additionally, if the target is set to an entity that does not meet a
        conduit's hunting conditions (e.g. the entity is not within the
        {@link #getHuntingArea() hunting area}, has already been killed, etc.)
        then the passed entity will be ignored and the conduit will also continue
        to look for a new target.

        @param target: the target entity, or null to remove the target

        @return: true if the target was changed, false if the target was the same
        """
        ...

    def get_target(self) -> Optional[LivingEntity]:
        """
        Get the conduit's hunting target.

        @return: the hunting target, or null if the conduit does not have a target
        """
        ...

    def has_target(self) -> bool:
        """
        Check whether or not this conduit has an active (alive) hunting target.

        @return: true if has a hunting target, false otherwise
        """
        ...

    def get_hunting_area(self) -> BoundingBox:
        """
        Get a {@link BoundingBox} (relative to real-world coordinates) in which
        the conduit will search for hostile entities to target.

        @return: the hunting area bounding box
        """
        ...