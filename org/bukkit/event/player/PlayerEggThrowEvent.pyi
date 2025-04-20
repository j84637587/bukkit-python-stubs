from org.bukkit.entity import Egg
from org.bukkit.entity import EntityType
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Literal

class PlayerEggThrowEvent(PlayerEvent):
    """
    Called when a player throws an egg and it might hatch
    """

    handlers: HandlerList

    def __init__(self, player: Player, egg: Egg, hatching: bool, num_hatches: int, hatching_type: EntityType) -> None:
        ...

    def getEgg(self) -> Egg:
        """
        Gets the egg involved in this event.

        :return: the egg involved in this event
        """
        ...

    def isHatching(self) -> bool:
        """
        Gets whether the egg is hatching or not. Will be what the server
        would've done without interaction.

        :return: boolean Whether the egg is going to hatch or not
        """
        ...

    def setHatching(self, hatching: bool) -> None:
        """
        Sets whether the egg will hatch or not.

        :param hatching: true if you want the egg to hatch, false if you want it not to
        """
        ...

    def getHatchingType(self) -> EntityType:
        """
        Get the type of the mob being hatched (EntityType.CHICKEN by default)

        :return: The type of the mob being hatched by the egg
        """
        ...

    def setHatchingType(self, hatch_type: EntityType) -> None:
        """
        Change the type of mob being hatched by the egg

        :param hatch_type: The type of the mob being hatched by the egg
        """
        ...

    def getNumHatches(self) -> int:
        """
        Get the number of mob hatches from the egg. By default the number will
        be the number the server would've done
        <ul>
        <li>7/8 chance of being 0
        <li>31/256 ~= 1/8 chance to be 1
        <li>1/256 chance to be 4
        </ul>

        :return: The number of mobs going to be hatched by the egg
        """
        ...

    def setNumHatches(self, num_hatches: int) -> None:
        """
        Change the number of mobs coming out of the hatched egg
        <p>
        The boolean hatching will override this number. Ie. If hatching =
        false, this number will not matter

        :param num_hatches: The number of mobs coming out of the egg
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...