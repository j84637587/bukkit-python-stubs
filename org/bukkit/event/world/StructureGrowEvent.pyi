from typing import List, Optional
from org.bukkit import Location
from org.bukkit import TreeType
from org.bukkit.block import BlockState
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.world import WorldEvent
from org.jetbrains.annotations import NotNull, Nullable

class StructureGrowEvent(WorldEvent, Cancellable):
    """
    Event that is called when an organic structure attempts to grow (Sapling {@literal ->}
    Tree), (Mushroom {@literal ->} Huge Mushroom), naturally or using bonemeal.
    """

    handlers: HandlerList

    def __init__(self,
                 location: Location,
                 species: TreeType,
                 bonemeal: bool,
                 player: Optional[Player],
                 blocks: List[BlockState]) -> None:
        ...

        def getLocation(self) -> Location:
        """
        Gets the location of the structure.

        @return Location of the structure
        """
        ...

        def getSpecies(self) -> TreeType:
        """
        Gets the species type (birch, normal, pine, red mushroom, brown
        mushroom)

        @return Structure species
        """
        ...

    def isFromBonemeal(self) -> bool:
        """
        Checks if structure was grown using bonemeal.

        @return True if the structure was grown using bonemeal.
        """
        ...

        def getPlayer(self) -> Optional[Player]:
        """
        Gets the player that created the structure.

        @return Player that created the structure, null if was not created
            manually
        """
        ...

        def getBlocks(self) -> List[BlockState]:
        """
        Gets a list of all blocks associated with the structure.

        @return list of all blocks associated with the structure.
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...