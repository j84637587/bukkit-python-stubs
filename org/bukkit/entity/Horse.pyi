from org.bukkit.inventory import HorseInventory
from typing import Literal, Protocol, runtime_checkable

@runtime_checkable
class Horse(Protocol):
    """
    Represents a Horse.
    """

    class Variant:
        """
        @deprecated different variants are differing classes
        """

        HORSE: Literal["HORSE"]
        DONKEY: Literal["DONKEY"]
        MULE: Literal["MULE"]
        UNDEAD_HORSE: Literal["UNDEAD_HORSE"]
        SKELETON_HORSE: Literal["SKELETON_HORSE"]
        LLAMA: Literal["LLAMA"]
        CAMEL: Literal["CAMEL"]

    class Color:
        """
        Represents the base color that the horse has.
        """

        WHITE: Literal["WHITE"]
        CREAMY: Literal["CREAMY"]
        CHESTNUT: Literal["CHESTNUT"]
        BROWN: Literal["BROWN"]
        BLACK: Literal["BLACK"]
        GRAY: Literal["GRAY"]
        DARK_BROWN: Literal["DARK_BROWN"]

    class Style:
        """
        Represents the style, or markings, that the horse has.
        """

        NONE: Literal["NONE"]
        WHITE: Literal["WHITE"]
        WHITEFIELD: Literal["WHITEFIELD"]
        WHITE_DOTS: Literal["WHITE_DOTS"]
        BLACK_DOTS: Literal["BLACK_DOTS"]

    def getColor(self) -> Color:
        """
        Gets the horse's color.
        <p>
        Colors only apply to horses, not to donkeys, mules, skeleton horses
        or undead horses.
        <p>
        @return a {@link Color} representing the horse's group
        """

    def setColor(self, color: Color) -> None:
        """
        Sets the horse's color.
        <p>
        Attempting to set a color for any donkey, mule, skeleton horse or
        undead horse will not result in a change.
        <p>
        @param color a {@link Color} for this horse
        """

    def getStyle(self) -> Style:
        """
        Gets the horse's style.
        Styles determine what kind of markings or patterns a horse has.
        <p>
        Styles only apply to horses, not to donkeys, mules, skeleton horses
        or undead horses.
        <p>
        @return a {@link Style} representing the horse's style
        """

    def setStyle(self, style: Style) -> None:
        """
        Sets the style of this horse.
        Styles determine what kind of markings or patterns a horse has.
        <p>
        Attempting to set a style for any donkey, mule, skeleton horse or
        undead horse will not result in a change.
        <p>
        @param style a {@link Style} for this horse
        """

    def isCarryingChest(self) -> bool:
        """
        @return carrying chest status
        @deprecated see {@link ChestedHorse}
        """

    def setCarryingChest(self, chest: bool) -> None:
        """
        @param chest chest
        @deprecated see {@link ChestedHorse}
        """

    def getInventory(self) -> HorseInventory:
        """
        @return HorseInventory
        """
