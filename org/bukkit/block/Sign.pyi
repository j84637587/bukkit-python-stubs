from typing import List, Optional
from org.bukkit import DyeColor
from org.bukkit.block.sign import Side, SignSide
from org.bukkit.entity import Player
from org.bukkit.material import Colorable

class Sign(Colorable):
    """
    Represents a captured state of either a SignPost or a WallSign.
    """

    def get_lines(self) -> List[str]:
        """
        Gets all the lines of text currently on the {@link Side#FRONT} of this sign.

        @return Array of Strings containing each line of text
        @deprecated  A sign may have multiple writable sides now. Use {@link Sign#getSide(Side)} and {@link SignSide#getLines()}.
        """
        ...

    def get_line(self, index: int) -> str:
        """
        Gets the line of text at the specified index.
        <p>
        For example, getLine(0) will return the first line of text on the {@link Side#FRONT}.

        @param index Line number to get the text from, starting at 0
        @return Text on the given line
        @throws IndexOutOfBoundsException Thrown when the line does not exist
        @deprecated A sign may have multiple writable sides now. Use {@link #getSide(Side)} and {@link SignSide#getLine(int)}.
        """
        ...

    def set_line(self, index: int, line: str) -> None:
        """
        Sets the line of text at the specified index.
        <p>
        For example, setLine(0, "Line One") will set the first line of text to
        "Line One".

        @param index Line number to set the text at, starting from 0
        @param line New text to set at the specified index
        @throws IndexOutOfBoundsException If the index is out of the range 0..3
        @deprecated A sign may have multiple writable sides now. Use {@link #getSide(Side)} and {@link SignSide#setLine(int, String)}.
        """
        ...

    def is_editable(self) -> bool:
        """
        Marks whether this sign can be edited by players.

        @return if this sign is currently editable
        @deprecated use {@link #isWaxed()} instead
        """
        ...

    def set_editable(self, editable: bool) -> None:
        """
        Marks whether this sign can be edited by players.

        @param editable if this sign is currently editable
        @deprecated use {@link #setWaxed(boolean)} instead
        """
        ...

    def is_waxed(self) -> bool:
        """
        Gets whether or not this sign has been waxed. If a sign has been waxed, it
        cannot be edited by a player.

        @return if this sign is waxed
        """
        ...

    def set_waxed(self, waxed: bool) -> None:
        """
        Sets whether or not this sign has been waxed. If a sign has been waxed, it
        cannot be edited by a player.

        @param waxed if this sign is waxed
        """
        ...

    def is_glowing_text(self) -> bool:
        """
        Gets whether this sign has glowing text. Only affects the {@link Side#FRONT}.

        @return if this sign has glowing text
        @deprecated A sign may have multiple writable sides now. Use {@link #getSide(Side)} and {@link SignSide#isGlowingText()}.
        """
        ...

    def set_glowing_text(self, glowing: bool) -> None:
        """
        Sets whether this sign has glowing text. Only affects the {@link Side#FRONT}.

        @param glowing if this sign has glowing text
        @deprecated A sign may have multiple writable sides now. Use {@link #getSide(Side)} and {@link SignSide#setGlowingText(boolean)}.
        """
        ...

    def get_color(self) -> DyeColor:
        """
        {@inheritDoc}

        @deprecated A sign may have multiple writable sides now. Use {@link #getSide(Side)} and {@link SignSide#getColor()}.
        """
        ...

    def set_color(self, color: DyeColor) -> None:
        """
        {@inheritDoc}

        @deprecated A sign may have multiple writable sides now. Use {@link #getSide(Side)} and {@link SignSide#setColor(org.bukkit.DyeColor)}.
        """
        ...

    def get_side(self, side: Side) -> SignSide:
        """
        Return the side of the sign.

        @param side the side of the sign
        @return the selected side of the sign
        """
        ...

    def get_target_side(self, player: Player) -> SignSide:
        """
        Gets the side of this sign the given player is currently standing on.

        @param player the player
        @return the side the player is standing on
        """
        ...

    def get_allowed_editor(self) -> Optional[Player]:
        """
        Gets the player that is currently allowed to edit this sign. <br>
        Edits from other players will be rejected if this value is not null.

        @return the player allowed to edit this sign, or null
        """
        ...