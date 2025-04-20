from typing import Optional
from org.bukkit.entity import Entity
from .event.block import BellRingEvent
from .TileState import TileState
import org.bukkit.blockFace import BlockFace

class Bell(TileState):
    """
    Represents a captured state of Bell.
    """

    def ring(self, entity: Optional[Entity], direction: Optional[BlockFace]) -> bool:
        """
        Ring this bell. This will call a BellRingEvent.

        :param entity: the entity ringing the bell
        :param direction: the direction from which the bell was rung or None to
                          ring in the direction that the bell is facing
        :return: true if rung successfully, false if the event was cancelled
        """
        ...

    def ring(self, entity: Optional[Entity]) -> bool:
        """
        Ring this bell in the direction that the bell is facing. This will call a
        BellRingEvent.

        :param entity: the entity ringing the bell
        :return: true if rung successfully, false if the event was cancelled
        """
        ...

    def ring(self, direction: Optional[BlockFace]) -> bool:
        """
        Ring this bell. This will call a BellRingEvent.

        :param direction: the direction from which the bell was rung or None to
                          ring in the direction that the bell is facing
        :return: true if rung successfully, false if the event was cancelled
        """
        ...

    def ring(self) -> bool:
        """
        Ring this bell in the direction that the bell is facing. This will call a
        BellRingEvent.

        :return: true if rung successfully, false if the event was cancelled
        """
        ...

    def is_shaking(self) -> bool:
        """
        Check whether or not this bell is shaking. A bell is considered to be
        shaking if it was recently rung.
        A bell will typically shake for 50 ticks.

        :return: true if shaking, false otherwise
        """
        ...

    def get_shaking_ticks(self) -> int:
        """
        Get the amount of ticks since this bell has been shaking, or 0 if the
        bell is not currently shaking.
        A bell will typically shake for 50 ticks.

        :return: the time in ticks since the bell was rung, or 0 if not shaking
        """
        ...

    def is_resonating(self) -> bool:
        """
        Check whether or not this bell is resonating. A bell is considered to be
        resonating if is_shaking() while shaking, raiders were detected
        in the area and are ready to be highlighted to nearby players.
        A bell will typically resonate for 40 ticks.

        :return: true if resonating, false otherwise
        """
        ...

    def get_resonating_ticks(self) -> int:
        """
        Get the amount of ticks since this bell has been resonating, or 0 if the
        bell is not currently resonating.
        A bell will typically resonate for 40 ticks.

        :return: the time in ticks since the bell has been resonating, or 0 if not
                 resonating
        """
        ...