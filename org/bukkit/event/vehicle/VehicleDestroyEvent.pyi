from org.bukkit.entity import Entity
from org.bukkit.entity import Vehicle
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import VehicleEvent
from typing import Optional

class VehicleDestroyEvent(VehicleEvent, Cancellable):
    """
    Raised when a vehicle is destroyed, which could be caused by either a
    player or the environment. This is not raised if the boat is simply
    'removed' due to other means.
    """
    
    handlers: HandlerList = HandlerList()
    attacker: Optional[Entity]
    cancelled: bool

    def __init__(self, vehicle: Vehicle, attacker: Optional[Entity]) -> None:
        """
        Initializes the VehicleDestroyEvent.

        :param vehicle: The vehicle that is being destroyed.
        :param attacker: The Entity that has destroyed the vehicle, potentially null.
        """
        ...

    def get_attacker(self) -> Optional[Entity]:
        """
        Gets the Entity that has destroyed the vehicle, potentially null.

        :return: the Entity that has destroyed the vehicle, potentially null.
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """
        Sets the event as cancelled or not.

        :param cancel: True to cancel the event, False otherwise.
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: the HandlerList for this event.
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: the static HandlerList for this event.
        """
        ...