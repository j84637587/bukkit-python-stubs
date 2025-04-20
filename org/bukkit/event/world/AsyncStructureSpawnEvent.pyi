from org.bukkit.World import World
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.generator.structure.Structure import Structure
from org.bukkit.util.BoundingBox import BoundingBox
from org.jetbrains.annotations import NotNull

class AsyncStructureSpawnEvent(WorldEvent, Cancellable):
    """
    Called when a {@link Structure} is naturally generated in the world.
    """

    handlers: HandlerList

    def __init__(self, world: World, structure: Structure, bounding_box: BoundingBox, chunk_x: int, chunk_z: int) -> None:
        ...

        def get_structure(self) -> Structure:
        """
        Get the structure reference that is generated.

        @return the structure
        """
        ...

        def get_bounding_box(self) -> BoundingBox:
        """
        Get the bounding box of the structure.

        @return the bounding box
        """
        ...

    def get_chunk_x(self) -> int:
        """
        Get the x coordinate of the origin chunk of the structure.

        <b>Note, it is not safe to attempt to retrieve or interact with this
        chunk. This event is informative only!</b>

        @return the chunk x coordinate
        """
        ...

    def get_chunk_z(self) -> int:
        """
        Get the z coordinate of the origin chunk of the structure.

        <b>Note, it is not safe to attempt to retrieve or interact with this
        chunk. This event is informative only!</b>

        @return the chunk z coordinate
        """
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...