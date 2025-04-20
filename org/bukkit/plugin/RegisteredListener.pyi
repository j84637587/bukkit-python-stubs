from org.bukkit.event import Cancellable, Event, EventException, EventPriority, Listener
from org.bukkit.plugin import Plugin, EventExecutor
from typing import Any

class RegisteredListener:
    """
    Stores relevant information for plugin listeners
    """
    
    def __init__(self, listener: Listener, executor: EventExecutor, priority: EventPriority, plugin: Plugin, ignore_cancelled: bool) -> None:
        ...

    """
    Gets the listener for this registration

    @return: Registered Listener
    """
    def get_listener(self) -> Listener:
        ...

    """
    Gets the plugin for this registration

    @return: Registered Plugin
    """
    def get_plugin(self) -> Plugin:
        ...

    """
    Gets the priority for this registration

    @return: Registered Priority
    """
    def get_priority(self) -> EventPriority:
        ...

    """
    Calls the event executor

    @param event: The event
    @raises EventException: If an event handler throws an exception.
    """
    def call_event(self, event: Event) -> None:
        ...

    """
    Whether this listener accepts cancelled events

    @return: True when ignoring cancelled events
    """
    def is_ignoring_cancelled(self) -> bool:
        ...