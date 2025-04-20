from collections import UserList
from enum import Enum
from typing import List, Dict, Collection, Optional
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import RegisteredListener
from org.jetbrains.annotations import NotNull

class EventPriority(Enum):
    # Enum members should be defined here based on the Java code
    pass

class HandlerList:
    """
    A list of event handlers, stored per-event. Based on lahwran's fevents.
    """

    handlers: Optional[List[RegisteredListener]] = None
    handlerslots: Dict[EventPriority, List[RegisteredListener]]
    allLists: List['HandlerList'] = []

    @staticmethod
    def bakeAll() -> None:
        """
        Bake all handler lists. Best used just after all normal event
        registration is complete, ie just after all plugins are loaded if
        you're using fevents in a plugin system.
        """
        pass

    @staticmethod
    def unregisterAll() -> None:
        """
        Unregister all listeners from all handler lists.
        """
        pass

    @staticmethod
    def unregisterAll(plugin: Plugin) -> None:
        """
        Unregister a specific plugin's listeners from all handler lists.

        :param plugin: plugin to unregister
        """
        pass

    @staticmethod
    def unregisterAll(listener: 'Listener') -> None:
        """
        Unregister a specific listener from all handler lists.

        :param listener: listener to unregister
        """
        pass

    def __init__(self) -> None:
        """
        Create a new handler list and initialize using EventPriority.
        The HandlerList is then added to meta-list for use in bakeAll()
        """
        pass

    def register(self, listener: RegisteredListener) -> None:
        """
        Register a new listener in this handler list.

        :param listener: listener to register
        """
        pass

    def registerAll(self, listeners: Collection[RegisteredListener]) -> None:
        """
        Register a collection of new listeners in this handler list.

        :param listeners: listeners to register
        """
        pass

    def unregister(self, listener: RegisteredListener) -> None:
        """
        Remove a listener from a specific order slot.

        :param listener: listener to remove
        """
        pass

    def unregister(self, plugin: Plugin) -> None:
        """
        Remove a specific plugin's listeners from this handler.

        :param plugin: plugin to remove
        """
        pass

    def unregister(self, listener: 'Listener') -> None:
        """
        Remove a specific listener from this handler.

        :param listener: listener to remove
        """
        pass

    def bake(self) -> None:
        """
        Bake HashMap and ArrayLists to 2d array - does nothing if not necessary.
        """
        pass

        def getRegisteredListeners(self) -> List[RegisteredListener]:
        """
        Get the baked registered listeners associated with this handler list.

        :return: the array of registered listeners
        """
        pass

        @staticmethod
    def getRegisteredListeners(plugin: Plugin) -> List[RegisteredListener]:
        """
        Get a specific plugin's registered listeners associated with this
        handler list.

        :param plugin: the plugin to get the listeners of
        :return: the list of registered listeners
        """
        pass

        @staticmethod
    def getHandlerLists() -> List['HandlerList']:
        """
        Get a list of all handler lists for every event type.

        :return: the list of all handler lists
        """
        pass