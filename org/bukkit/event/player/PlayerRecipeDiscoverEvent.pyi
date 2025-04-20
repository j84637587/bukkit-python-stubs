from org.bukkit.NamespacedKey import NamespacedKey
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.player.PlayerEvent import PlayerEvent
from typing import Any

class PlayerRecipeDiscoverEvent(PlayerEvent, Cancellable):
    """
    Called when a player discovers a new recipe in the recipe book.
    """

    handlers: HandlerList

    def __init__(self, who: Player, recipe: NamespacedKey) -> None:
        ...

    def getRecipe(self) -> NamespacedKey:
        """
        Get the namespaced key of the discovered recipe.

        @return: the discovered recipe
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...