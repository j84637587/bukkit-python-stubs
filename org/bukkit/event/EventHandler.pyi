from enum import Enum
from typing import Callable, TypeVar

T = TypeVar('T')

class EventPriority(Enum):
    LOWEST = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    HIGHEST = 5
    MONITOR = 6

class EventHandler:
    """
    An annotation to mark methods as being event handler methods
    """

    def __init__(self, priority: EventPriority = EventPriority.NORMAL, ignore_cancelled: bool = False) -> None:
        """
        Define the priority of the event.
        <p>
        First priority to the last priority executed:
        <ol>
        <li>LOWEST
        <li>LOW
        <li>NORMAL
        <li>HIGH
        <li>HIGHEST
        <li>MONITOR
        </ol>
        @return the priority
        """
        ...

    @property
    def priority(self) -> EventPriority:
        ...

    @property
    def ignore_cancelled(self) -> bool:
        ...