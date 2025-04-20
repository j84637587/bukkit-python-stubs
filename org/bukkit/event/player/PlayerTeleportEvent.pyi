from org.bukkit.Location import Location
from org.bukkit.entity.Player import Player
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.player.PlayerMoveEvent import PlayerMoveEvent
from typing import Optional

class PlayerTeleportEvent(PlayerMoveEvent):
    """
    Holds information for player teleport events
    """
    handlers: HandlerList = HandlerList()
    cause: 'PlayerTeleportEvent.TeleportCause' = 'PlayerTeleportEvent.TeleportCause.UNKNOWN'

    def __init__(self, player: Player, from_location: Location, to_location: Optional[Location] = None) -> None:
        super().__init__(player, from_location, to_location)

    def __init__(self, player: Player, from_location: Location, to_location: Optional[Location] = None, cause: 'PlayerTeleportEvent.TeleportCause' = None) -> None:
        super().__init__(player, from_location, to_location)
        self.cause = cause

    """
    Gets the cause of this teleportation event

    @return Cause of the event
    """
    def get_cause(self) -> 'PlayerTeleportEvent.TeleportCause':
        ...

    class TeleportCause:
        """
        Indicates the teleporation was caused by a player throwing an Ender Pearl
        """
        ENDER_PEARL = ...
        """
        Indicates the teleportation was caused by a player executing a command
        """
        COMMAND = ...
        """
        Indicates the teleportation was caused by a plugin
        """
        PLUGIN = ...
        """
        Indicates the teleportation was caused by a player entering a Nether portal
        """
        NETHER_PORTAL = ...
        """
        Indicates the teleportation was caused by a player entering an End portal
        """
        END_PORTAL = ...
        """
        Indicates the teleportation was caused by a player teleporting to a Entity/Player via the spectator menu
        """
        SPECTATE = ...
        """
        Indicates the teleportation was caused by a player entering an End gateway
        """
        END_GATEWAY = ...
        """
        Indicates the teleportation was caused by a player consuming chorus fruit
        """
        CHORUS_FRUIT = ...
        """
        Indicates the teleportation was caused by a player exiting a vehicle
        """
        DISMOUNT = ...
        """
        Indicates the teleportation was caused by a player exiting a bed
        """
        EXIT_BED = ...
        """
        Indicates the teleportation was caused by an event not covered by this enum
        """
        UNKNOWN = ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...