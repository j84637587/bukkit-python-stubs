from typing import TYPE_CHECKING
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.inventory import CraftingRecipe, Recipe
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull

class PlayerRecipeBookClickEvent(PlayerEvent):
    """
    Called when a player clicks a recipe in the recipe book.
    """

    handlers: HandlerList = HandlerList()
    originalRecipe: Recipe
    recipe: Recipe
    shiftClick: bool

    def __init__(self: "PlayerRecipeBookClickEvent",
                 player: Player,
                 recipe: Recipe,
                 shiftClick: bool) -> None:
        ...

        def getOriginalRecipe(self: "PlayerRecipeBookClickEvent") -> Recipe:
        """
        Gets the original recipe the player was trying to craft. <br>
        This <em>will not</em> reflect any changes made with {@link setRecipe}.

        @return: the original recipe
        """
        ...

        def getRecipe(self: "PlayerRecipeBookClickEvent") -> Recipe:
        """
        Gets the recipe the player is trying to craft. <br>
        This <em>will</em> reflect changes made with {@link setRecipe}.

        @return: the recipe
        """
        ...

    def setRecipe(self: "PlayerRecipeBookClickEvent",
                  recipe: Recipe) -> None:
        """
        Set the recipe that will be used. <br>
        The game will attempt to move the ingredients for this recipe into the
        appropriate slots.
        <p>
        If the original recipe is a {@link CraftingRecipe} the provided recipe
        must also be a {@link CraftingRecipe}, otherwise the provided recipe must
        be of the same type as the original recipe.

        @param recipe: the recipe to be used
        """
        ...

    def isShiftClick(self: "PlayerRecipeBookClickEvent") -> bool:
        """
        If true the game will attempt to move the ingredients for as many copies
        of this recipe as possible into the appropriate slots, otherwise only 1
        copy will be moved.

        @return: whether as many copies as possible should be moved
        """
        ...

    def setShiftClick(self: "PlayerRecipeBookClickEvent",
                      shiftClick: bool) -> None:
        """
        Sets if the game will attempt to move the ingredients for as many copies
        of this recipe as possible into the appropriate slots.

        @param shiftClick: whether as many copies as possible should be moved
        """
        ...

        def getHandlers(self: "PlayerRecipeBookClickEvent") -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...