from org.bukkit.event import Event
from org.bukkit.event import EventException
from org.bukkit.event import Listener
from typing import Protocol

class EventExecutor(Protocol):
    """
    Interface which defines the class for event call backs to plugins
    """
    
    def execute(self, listener: Listener, event: Event) -> None:
        """ 
        Executes the event with the given listener.
        
        Args:
            listener (Listener): The listener to execute the event for.
            event (Event): The event to be executed.
        
        Raises:
            EventException: If an error occurs during event execution.
        """
        ...