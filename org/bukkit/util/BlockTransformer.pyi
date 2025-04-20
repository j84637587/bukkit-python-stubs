from org.bukkit.block import BlockState
from org.bukkit.block.data import BlockData
from org.bukkit.generator import LimitedRegion
from org.jetbrains.annotations import ApiStatus, NotNull
from typing import Protocol

class BlockTransformer(Protocol):
    """
    A BlockTransformer is used to modify blocks that are placed by structure.
    """

    class TransformationState(Protocol):
        """
        The TransformationState allows access to the original block state and the
        block state of the block that was at the location of the transformation
        in the world before the transformation started.
        """

                def getOriginal(self) -> BlockState:
            """
            Creates a clone of the original block state that a structure wanted
            to place and caches it for the current transformer.

            @return: a clone of the original block state.
            """
            ...

                def getWorld(self) -> BlockState:
            """
            Creates a clone of the block state that was at the location of the
            currently modified block at the start of the transformation process
            and caches it for the current transformer.

            @return: a clone of the world block state.
            """
            ...

        def transform(self,
                  region: LimitedRegion,
                  x: int,
                  y: int,
                  z: int,
                  current: BlockState,
                  state: TransformationState) -> BlockState:
        """
        Transforms a block in a structure.

        NOTE: The usage of BlockData.createBlockState() can provide even
        more flexibility to return the exact block state you might want to
        return.

        @param region: the accessible region
        @param x: the x position of the block
        @param y: the y position of the block
        @param z: the z position of the block
        @param current: the state of the block that should be placed
        @param state: the state of this transformation.

        @return: the new block state
        """
        ...