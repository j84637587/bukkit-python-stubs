from org.bukkit.entity import AbstractArrow
from org.bukkit.entity import Item
from org.bukkit.entity import Player
from org.jetbrains.annotations import NotNull

class PlayerPickupArrowEvent(PlayerPickupItemEvent):
    """
    Thrown when a player picks up an arrow from the ground.
    """

    def __init__(self, player: NotNull[Player], item: NotNull[Item], arrow: NotNull[AbstractArrow]) -> None:
        ...

    """
    Get the arrow being picked up by the player

    @return The arrow being picked up
    """
        def get_arrow(self) -> AbstractArrow:
        ...