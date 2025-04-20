from typing import Dict, Set, Any
from org.bukkit.entity import Player
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import Messenger, PluginMessageListener, PluginMessageListenerRegistration
from org.jetbrains.annotations import NotNull

class StandardMessenger(Messenger):
    """
    Standard implementation to {@link Messenger}
    """

    incomingByChannel: Dict[str, Set[PluginMessageListenerRegistration]]
    incomingByPlugin: Dict[Plugin, Set[PluginMessageListenerRegistration]]
    outgoingByChannel: Dict[str, Set[Plugin]]
    outgoingByPlugin: Dict[Plugin, Set[str]]
    incomingLock: Any
    outgoingLock: Any

    def addToOutgoing(self, plugin: Plugin, channel: str) -> None:
        """
        Adds a plugin to the outgoing channel.
        """
        ...

    def removeFromOutgoing(self, plugin: Plugin, channel: str) -> None:
        """
        Removes a plugin from the outgoing channel.
        """
        ...

    def removeFromOutgoing(self, plugin: Plugin) -> None:
        """
        Removes all outgoing channels for a plugin.
        """
        ...

    def addToIncoming(self, registration: PluginMessageListenerRegistration) -> None:
        """
        Adds a registration to the incoming channel.
        """
        ...

    def removeFromIncoming(self, registration: PluginMessageListenerRegistration) -> None:
        """
        Removes a registration from the incoming channel.
        """
        ...

    def removeFromIncoming(self, plugin: Plugin, channel: str) -> None:
        """
        Removes all incoming registrations for a plugin on a specific channel.
        """
        ...

    def removeFromIncoming(self, plugin: Plugin) -> None:
        """
        Removes all incoming registrations for a plugin.
        """
        ...

    def isReservedChannel(self, channel: str) -> bool:
        """
        Checks if a channel is reserved.
        """
        ...

    def registerOutgoingPluginChannel(self, plugin: Plugin, channel: str) -> None:
        """
        Registers an outgoing plugin channel.
        """
        ...

    def unregisterOutgoingPluginChannel(self, plugin: Plugin, channel: str) -> None:
        """
        Unregisters an outgoing plugin channel.
        """
        ...

    def unregisterOutgoingPluginChannel(self, plugin: Plugin) -> None:
        """
        Unregisters all outgoing plugin channels for a plugin.
        """
        ...

    def registerIncomingPluginChannel(self, plugin: Plugin, channel: str, listener: PluginMessageListener) -> PluginMessageListenerRegistration:
        """
        Registers an incoming plugin channel.
        """
        ...

    def unregisterIncomingPluginChannel(self, plugin: Plugin, channel: str, listener: PluginMessageListener) -> None:
        """
        Unregisters an incoming plugin channel.
        """
        ...

    def unregisterIncomingPluginChannel(self, plugin: Plugin, channel: str) -> None:
        """
        Unregisters an incoming plugin channel.
        """
        ...

    def unregisterIncomingPluginChannel(self, plugin: Plugin) -> None:
        """
        Unregisters all incoming plugin channels for a plugin.
        """
        ...

    def getOutgoingChannels(self) -> Set[str]:
        """
        Gets all outgoing channels.
        """
        ...

    def getOutgoingChannels(self, plugin: Plugin) -> Set[str]:
        """
        Gets all outgoing channels for a specific plugin.
        """
        ...

    def getIncomingChannels(self) -> Set[str]:
        """
        Gets all incoming channels.
        """
        ...

    def getIncomingChannels(self, plugin: Plugin) -> Set[str]:
        """
        Gets all incoming channels for a specific plugin.
        """
        ...

    def getIncomingChannelRegistrations(self, plugin: Plugin) -> Set[PluginMessageListenerRegistration]:
        """
        Gets all incoming channel registrations for a specific plugin.
        """
        ...

    def getIncomingChannelRegistrations(self, channel: str) -> Set[PluginMessageListenerRegistration]:
        """
        Gets all incoming channel registrations for a specific channel.
        """
        ...

    def getIncomingChannelRegistrations(self, plugin: Plugin, channel: str) -> Set[PluginMessageListenerRegistration]:
        """
        Gets all incoming channel registrations for a specific plugin and channel.
        """
        ...

    def isRegistrationValid(self, registration: PluginMessageListenerRegistration) -> bool:
        """
        Checks if a registration is valid.
        """
        ...

    def isIncomingChannelRegistered(self, plugin: Plugin, channel: str) -> bool:
        """
        Checks if an incoming channel is registered for a plugin.
        """
        ...

    def isOutgoingChannelRegistered(self, plugin: Plugin, channel: str) -> bool:
        """
        Checks if an outgoing channel is registered for a plugin.
        """
        ...

    def dispatchIncomingMessage(self, source: Player, channel: str, message: bytes) -> None:
        """
        Dispatches an incoming message.
        """
        ...

    @staticmethod
    def validateChannel(channel: str) -> None:
        """
        Validates a Plugin Channel name.
        """
        ...

    @staticmethod
    def validateAndCorrectChannel(channel: str) -> str:
        """
        Validates and corrects a Plugin Channel name.
        """
        ...

    @staticmethod
    def validatePluginMessage(messenger: Messenger, source: Plugin, channel: str, message: bytes) -> None:
        """
        Validates the input of a Plugin Message.
        """
        ...