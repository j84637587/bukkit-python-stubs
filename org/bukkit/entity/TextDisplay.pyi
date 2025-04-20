from org.bukkit.Color import Color
from typing import Optional
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a text display entity.
"""
class TextDisplay(Display):

    """
    Gets the displayed text.

    @return the displayed text.
    """
    def get_text(self) -> Optional[str]: ...

    """
    Sets the displayed text.

    @param text the new text
    """
    def set_text(self, text: Optional[str]) -> None: ...

    """
    Gets the maximum line width before wrapping.

    @return the line width
    """
    def get_line_width(self) -> int: ...

    """
    Sets the maximum line width before wrapping.

    @param width new line width
    """
    def set_line_width(self, width: int) -> None: ...

    """
    Gets the text background color.

    @return the background color
    """
    def get_background_color(self) -> Optional[Color]: ...

    """
    Sets the text background color.

    @param color new background color
    """
    def set_background_color(self, color: Optional[Color]) -> None: ...

    """
    Gets the text opacity.

    @return opacity or -1 if not set
    """
    def get_text_opacity(self) -> int: ...

    """
    Sets the text opacity.

    @param opacity new opacity or -1 if default
    """
    def set_text_opacity(self, opacity: int) -> None: ...

    """
    Gets if the text is shadowed.

    @return shadow status
    """
    def is_shadowed(self) -> bool: ...

    """
    Sets if the text is shadowed.

    @param shadow if shadowed
    """
    def set_shadowed(self, shadow: bool) -> None: ...

    """
    Gets if the text is see through.

    @return see through status
    """
    def is_see_through(self) -> bool: ...

    """
    Sets if the text is see through.

    @param see_through if see through
    """
    def set_see_through(self, see_through: bool) -> None: ...

    """
    Gets if the text has its default background.

    @return default background
    """
    def is_default_background(self) -> bool: ...

    """
    Sets if the text has its default background.

    @param default_background if default
    """
    def set_default_background(self, default_background: bool) -> None: ...

    """
    Gets the text alignment for this display.

    @return text alignment
    """
        def get_alignment(self) -> 'TextAlignment': ...

    """
    Sets the text alignment for this display.

    @param alignment new alignment
    """
    def set_alignment(self, alignment: 'TextAlignment') -> None: ...

    """
    Represents possible text alignments for this display.
    """
    class TextAlignment:
        """
        Center aligned text (default).
        """
        CENTER = ...

        """
        Left aligned text.
        """
        LEFT = ...

        """
        Right aligned text.
        """
        RIGHT = ...