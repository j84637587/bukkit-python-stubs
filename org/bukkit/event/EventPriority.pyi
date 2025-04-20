from enum import Enum

class EventPriority(Enum):
    """
    Represents an event's priority in execution.
    <p>
    Listeners with lower priority are called first
    will listeners with higher priority are called last.
    <p>
    Listeners are called in following order:
    LOWEST -> LOW -> NORMAL -> HIGH -> HIGHEST -> MONITOR
    """
    
    LOWEST: int = 0
    """
    Event call is of very low importance and should be run first, to allow
    other plugins to further customise the outcome
    """
    
    LOW: int = 1
    """
    Event call is of low importance
    """
    
    NORMAL: int = 2
    """
    Event call is neither important nor unimportant, and may be run
    normally
    """
    
    HIGH: int = 3
    """
    Event call is of high importance
    """
    
    HIGHEST: int = 4
    """
    Event call is critical and must have the final say in what happens
    to the event
    """
    
    MONITOR: int = 5
    """
    Event is listened to purely for monitoring the outcome of an event.
    <p>
    No modifications to the event should be made under this priority
    """
    
    def __init__(self, slot: int) -> None:
        self.slot: int = slot

    def get_slot(self) -> int:
        """
        :return: the slot value of the event priority
        """
        ...