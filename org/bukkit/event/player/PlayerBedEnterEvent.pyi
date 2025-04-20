from org.bukkit.World import World
from org.bukkit.block.Block import Block
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.Event import Result
from typing import Literal

class PlayerBedEnterEvent(PlayerEvent, Cancellable):
    """
    This event is fired when the player is almost about to enter the bed.
    """

    class BedEnterResult:
        """
        Represents the default possible outcomes of this event.
        """
        OK: Literal['OK']
        NOT_POSSIBLE_HERE: Literal['NOT_POSSIBLE_HERE']
        NOT_POSSIBLE_NOW: Literal['NOT_POSSIBLE_NOW']
        TOO_FAR_AWAY: Literal['TOO_FAR_AWAY']
        NOT_SAFE: Literal['NOT_SAFE']
        OTHER_PROBLEM: Literal['OTHER_PROBLEM']

    handlers: HandlerList
    bed: Block
    bedEnterResult: BedEnterResult
    useBed: Result

    def __init__(self, who: Player, bed: Block, bedEnterResult: BedEnterResult) -> None:
        ...

    def __init__(self, who: Player, bed: Block) -> None:
        ...

    def getBedEnterResult(self) -> BedEnterResult:
        """
        This describes the default outcome of this event.

        @return: the bed enter result representing the default outcome of this event
        """
        ...

    def useBed(self) -> Result:
        """
        This controls the action to take with the bed that was clicked on.
        <p>
        In case of {@link org.bukkit.event.Event.Result#DEFAULT}, the default outcome is described by
        {@link #getBedEnterResult()}.

        @return: the action to take with the interacted bed
        @see: #setUseBed(org.bukkit.event.Event.Result)
        """
        ...

    def setUseBed(self, useBed: Result) -> None:
        """
        Sets the action to take with the interacted bed.
        <p>
        {@link org.bukkit.event.Event.Result#ALLOW} will result in the player sleeping, regardless of
        the default outcome described by {@link #getBedEnterResult()}.
        <br>
        {@link org.bukkit.event.Event.Result#DENY} will prevent the player from sleeping. This has the
        same effect as canceling the event via {@link #setCancelled(boolean)}.
        <br>
        {@link org.bukkit.event.Event.Result#DEFAULT} will result in the outcome described by
        {@link #getBedEnterResult()}.

        @param useBed: the action to take with the interacted bed
        @see: #useBed()
        """
        ...

    def isCancelled(self) -> bool:
        """
        Gets the cancellation state of this event. Set to true if you want to
        prevent the player from sleeping.
        <p>
        Canceling the event has the same effect as setting {@link #useBed()} to
        {@link org.bukkit.event.Event.Result#DENY}.
        <p>
        For backwards compatibility reasons this also returns true if
        {@link #useBed()} is {@link org.bukkit.event.Event.Result#DEFAULT} and the
        {@link #getBedEnterResult() default action} is to prevent bed entering.

        @return: boolean cancellation state
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A canceled event will not be
        executed in the server, but will still pass to other plugins.
        <p>
        Canceling this event will prevent use of the bed.

        @param cancel: true if you wish to cancel this event
        """
        ...

    def getBed(self) -> Block:
        """
        Returns the bed block involved in this event.

        @return: the bed block involved in this event
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def getHandlerList() -> HandlerList:
        ...