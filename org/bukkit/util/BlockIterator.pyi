from typing import Iterator, NoReturn
from org.bukkit.Location import Location
from org.bukkit.World import World
from org.bukkit.block.Block import Block
from org.bukkit.block.BlockFace import BlockFace
from org.bukkit.entity.LivingEntity import LivingEntity
from org.jetbrains.annotations import NotNull

class BlockIterator(Iterator[Block]):
    """
    This class performs ray tracing and iterates along blocks on a line
    """

    def __init__(self, world: World, start: 'Vector', direction: 'Vector', y_offset: float, max_distance: int) -> None:
        """
        Constructs the BlockIterator.
        <p>
        This considers all blocks as 1x1x1 in size.

        @param world The world to use for tracing
        @param start A Vector giving the initial location for the trace
        @param direction A Vector pointing in the direction for the trace
        @param y_offset The trace begins vertically offset from the start vector
            by this value
        @param max_distance This is the maximum distance in blocks for the
            trace. Setting this value above 140 may lead to problems with
            unloaded chunks. A value of 0 indicates no limit
        """
        ...

    def __init__(self, loc: Location, y_offset: float, max_distance: int) -> None:
        """
        Constructs the BlockIterator.
        <p>
        This considers all blocks as 1x1x1 in size.

        @param loc The location for the start of the ray trace
        @param y_offset The trace begins vertically offset from the start vector
            by this value
        @param max_distance This is the maximum distance in blocks for the
            trace. Setting this value above 140 may lead to problems with
            unloaded chunks. A value of 0 indicates no limit
        """
        ...

    def __init__(self, loc: Location, y_offset: float) -> None:
        """
        Constructs the BlockIterator.
        <p>
        This considers all blocks as 1x1x1 in size.

        @param loc The location for the start of the ray trace
        """
        ...

    def __init__(self, loc: Location) -> None:
        """
        Constructs the BlockIterator.
        <p>
        This considers all blocks as 1x1x1 in size.

        @param loc The location for the start of the ray trace
        """
        ...

    def __init__(self, entity: LivingEntity, max_distance: int) -> None:
        """
        Constructs the BlockIterator.
        <p>
        This considers all blocks as 1x1x1 in size.

        @param entity Information from the entity is used to set up the trace
        @param max_distance This is the maximum distance in blocks for the
            trace. Setting this value above 140 may lead to problems with
            unloaded chunks. A value of 0 indicates no limit
        """
        ...

    def __init__(self, entity: LivingEntity) -> None:
        """
        Constructs the BlockIterator.
        <p>
        This considers all blocks as 1x1x1 in size.

        @param entity Information from the entity is used to set up the trace
        """
        ...

    def hasNext(self) -> bool:
        """
        Returns true if the iteration has more elements
        """
        ...

    def next(self) -> Block:
        """
        Returns the next Block in the trace

        @return the next Block in the trace
        """
        ...

    def remove(self) -> NoReturn:
        """
        Removes the current element from the iterator.
        """
        ...

    def scan(self) -> None:
        ...
    
    def blockEquals(self, a: Block, b: Block) -> bool:
        ...

    def getXFace(self, direction: 'Vector') -> BlockFace:
        ...

    def getYFace(self, direction: 'Vector') -> BlockFace:
        ...

    def getZFace(self, direction: 'Vector') -> BlockFace:
        ...

    def getXLength(self, direction: 'Vector') -> float:
        ...

    def getYLength(self, direction: 'Vector') -> float:
        ...

    def getZLength(self, direction: 'Vector') -> float:
        ...

    def getPosition(self, direction: float, position: float, block_position: int) -> float:
        ...

    def getXPosition(self, direction: 'Vector', position: 'Vector', block: Block) -> float:
        ...

    def getYPosition(self, direction: 'Vector', position: 'Vector', block: Block) -> float:
        ...

    def getZPosition(self, direction: 'Vector', position: 'Vector', block: Block) -> float:
        ...