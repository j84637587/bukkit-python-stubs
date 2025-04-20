from org.bukkit.entity import Entity
from org.bukkit.entity import FishHook
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from typing import Optional

"""
Thrown when a player is fishing
"""
class PlayerFishEvent(PlayerEvent, Cancellable):
    handlers: HandlerList = HandlerList()
    entity: Optional[Entity]
    cancel: bool
    exp: int
    state: 'State'
    hookEntity: FishHook
    hand: Optional[EquipmentSlot]

    def __init__(self, player: Player, entity: Optional[Entity], hookEntity: FishHook, hand: Optional[EquipmentSlot], state: 'State') -> None:
        ...

    def __init__(self, player: Player, entity: Optional[Entity], hookEntity: FishHook, state: 'State') -> None:
        ...

    """
    Gets the entity caught by the player.
    If player has fished successfully, the result may be cast to {@link
    org.bukkit.entity.Item}.

    @return Entity caught by the player, Entity if fishing, and null if
        bobber has gotten stuck in the ground or nothing has been caught
    """
    def getCaught(self) -> Optional[Entity]:
        ...

    """
    Gets the fishing hook.

    @return the entity representing the fishing hook/bobber.
    """
    def getHook(self) -> FishHook:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Gets the amount of experience received when fishing.
    Note: This value has no default effect unless the event state is {@link
    State#CAUGHT_FISH}.

    @return the amount of experience to drop
    """
    def getExpToDrop(self) -> int:
        ...

    """
    Sets the amount of experience received when fishing.
    Note: This value has no default effect unless the event state is {@link
    State#CAUGHT_FISH}.

    @param amount the amount of experience to drop
    """
    def setExpToDrop(self, amount: int) -> None:
        ...

    """
    Get the hand that was used in this event.
    The hand used is only present when the event state is {@link State#FISHING}.
    In all other states, the hand is null.

    @return the hand
    """
    def getHand(self) -> Optional[EquipmentSlot]:
        ...

    """
    Gets the state of the fishing

    @return A State detailing the state of the fishing
    """
    def getState(self) -> 'State':
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...


"""
An enum to specify the state of the fishing
"""
class State:
    FISHING = ...
    CAUGHT_FISH = ...
    CAUGHT_ENTITY = ...
    IN_GROUND = ...
    FAILED_ATTEMPT = ...
    REEL_IN = ...
    BITE = ...