from org.bukkit.entity import Entity
from org.bukkit.entity import Vehicle
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from typing import Optional

class VehicleDamageEvent(VehicleEvent, Cancellable):
    """
    Raised when a vehicle receives damage.
    """

    handlers: HandlerList

    def __init__(self, vehicle: Vehicle, attacker: Optional[Entity], damage: float) -> None:
        ...

    def get_attacker(self) -> Optional[Entity]:
        """
        Gets the Entity that is attacking the vehicle

        :return: the Entity that is attacking the vehicle
        """
        ...

    def get_damage(self) -> float:
        """
        Gets the damage done to the vehicle

        :return: the damage done to the vehicle
        """
        ...

    def set_damage(self, damage: float) -> None:
        """
        Sets the damage done to the vehicle

        :param damage: The damage
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