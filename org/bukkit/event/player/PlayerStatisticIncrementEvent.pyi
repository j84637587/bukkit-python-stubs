from org.bukkit import Bukkit
from org.bukkit import Material
from org.bukkit import Statistic
from org.bukkit.entity import EntityType
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.material import MaterialData
from typing import Optional

class PlayerStatisticIncrementEvent(PlayerEvent, Cancellable):
    """
    Called when a player statistic is incremented.
    <p>
    This event is not called for some high frequency statistics, e.g. movement
    based statistics.
    """

    handlers: HandlerList

    def __init__(self, player: Player, statistic: Statistic, initial_value: int, new_value: int) -> None:
        ...

    def __init__(self, player: Player, statistic: Statistic, initial_value: int, new_value: int, entity_type: EntityType) -> None:
        ...

    def __init__(self, player: Player, statistic: Statistic, initial_value: int, new_value: int, material: Material) -> None:
        ...

    def get_statistic(self) -> Statistic:
        """
        Gets the statistic that is being incremented.

        @return: the incremented statistic
        """
        ...

    def get_previous_value(self) -> int:
        """
        Gets the previous value of the statistic.

        @return: the previous value of the statistic
        """
        ...

    def get_new_value(self) -> int:
        """
        Gets the new value of the statistic.

        @return: the new value of the statistic
        """
        ...

    def get_entity_type(self) -> Optional[EntityType]:
        """
        Gets the EntityType if {@link #getStatistic() getStatistic()} is an
        entity statistic otherwise returns null.

        @return: the EntityType of the statistic
        """
        ...

    def get_material(self) -> Optional[Material]:
        """
        Gets the Material if {@link #getStatistic() getStatistic()} is a block
        or item statistic otherwise returns null.

        @return: the Material of the statistic
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