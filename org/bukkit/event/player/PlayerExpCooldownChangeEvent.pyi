from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Final, Literal

class PlayerExpCooldownChangeEvent(PlayerEvent):
    """
    Called when a player's experience cooldown changes.
    """

    handlers: Final[HandlerList]
    newCooldown: int
    reason: 'ChangeReason'

    def __init__(self, player: Player, newcooldown: int, reason: 'ChangeReason') -> None:
        super().__init__(player)
        self.newCooldown = newcooldown
        self.reason = reason

    def getReason(self) -> 'ChangeReason':
        """
        Gets the reason for the change.

        Returns:
            The reason for the change
        """
        ...

    def getNewCooldown(self) -> int:
        """
        Gets the new cooldown for the player.

        Returns:
            The new cooldown
        """
        ...

    def setNewCooldown(self, newCooldown: int) -> None:
        """
        Sets the new cooldown for the player.

        Args:
            newCooldown: The new cooldown to set
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

class ChangeReason:
    """
    Enum for the reason of the cooldown change.
    """
    PICKUP_ORB: Literal['PICKUP_ORB']
    PLUGIN: Literal['PLUGIN']