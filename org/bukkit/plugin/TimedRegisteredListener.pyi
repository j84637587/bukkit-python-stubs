from org.bukkit.event import Event
from org.bukkit.event import EventException
from org.bukkit.event import EventPriority
from org.bukkit.event import Listener
from org.bukkit.plugin import RegisteredListener
from org.bukkit.plugin import Plugin
from typing import Type, Optional

class TimedRegisteredListener(RegisteredListener):
    """
    Extends RegisteredListener to include timing information
    """
    
    def __init__(self, plugin_listener: Listener, event_executor: 'EventExecutor', event_priority: EventPriority, registered_plugin: Plugin, listen_cancelled: bool) -> None:
        ...

    def call_event(self, event: Event) -> None:
        ...

    @staticmethod
    def get_common_superclass(class1: Type, class2: Type) -> Type:
        ...

    def reset(self) -> None:
        """
        Resets the call count and total time for this listener
        """
        ...

    def get_count(self) -> int:
        """
        Gets the total times this listener has been called

        @return: Times this listener has been called
        """
        ...

    def get_total_time(self) -> int:
        """
        Gets the total time calls to this listener have taken

        @return: Total time for all calls of this listener
        """
        ...

    def get_event_class(self) -> Optional[Type[Event]]:
        """
        Gets the class of the events this listener handled. If it handled
        multiple classes of event, the closest shared superclass will be
        returned, such that for any event this listener has handled,
        <code>this.getEventClass().isAssignableFrom(event.getClass())</code>
        and no class <code>this.getEventClass().isAssignableFrom(clazz)
        {@literal && this.getEventClass() != clazz &&}
        event.getClass().isAssignableFrom(clazz)</code> for all handled events.

        @return: the event class handled by this RegisteredListener
        """
        ...

    def has_multiple(self) -> bool:
        """
        Gets whether this listener has handled multiple events, such that for
        some two events, <code>eventA.getClass() != eventB.getClass()</code>.

        @return: true if this listener has handled multiple events
        """
        ...