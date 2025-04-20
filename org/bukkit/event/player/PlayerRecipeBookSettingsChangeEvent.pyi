from typing import Literal, Type
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from org.jetbrains.annotations import NotNull

"""
Called when a player changes recipe book settings.
"""
class PlayerRecipeBookSettingsChangeEvent(PlayerEvent):
    handlers: HandlerList

    def __init__(self, player: Player, recipeBookType: 'RecipeBookType', open: bool, filtering: bool) -> None:
        super().__init__(player)
        ...

    """
    Gets the type of recipe book the player is changing the settings for.

    @return: the type of recipe book
    """
        def getRecipeBookType(self) -> 'RecipeBookType':
        ...

    """
    Checks if the recipe book is being opened or closed.

    @return: true if opening
    """
    def isOpen(self) -> bool:
        ...

    """
    Checks if the recipe book filter is being enabled or disabled.

    @return: true if enabling
    """
    def isFiltering(self) -> bool:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

"""
Enum representing the various types of recipe book.
Different types of recipe book are shown in different GUIs.
"""
class RecipeBookType:
    CRAFTING: Literal['CRAFTING']
    FURNACE: Literal['FURNACE']
    BLAST_FURNACE: Literal['BLAST_FURNACE']
    SMOKER: Literal['SMOKER']