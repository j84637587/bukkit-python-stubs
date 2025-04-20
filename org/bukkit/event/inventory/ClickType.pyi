from enum import Enum
from typing import Any

class ClickType(Enum):
    """
    What the client did to trigger this action (not the result).
    """
    LEFT = ...
    """
    The left (or primary) mouse button.
    """
    SHIFT_LEFT = ...
    """
    Holding shift while pressing the left mouse button.
    """
    RIGHT = ...
    """
    The right mouse button.
    """
    SHIFT_RIGHT = ...
    """
    Holding shift while pressing the right mouse button.
    """
    WINDOW_BORDER_LEFT = ...
    """
    Clicking the left mouse button on the grey area around the inventory.
    """
    WINDOW_BORDER_RIGHT = ...
    """
    Clicking the right mouse button on the grey area around the inventory.
    """
    MIDDLE = ...
    """
    The middle mouse button, or a "scrollwheel click".
    """
    NUMBER_KEY = ...
    """
    One of the number keys 1-9, correspond to slots on the hotbar.
    """
    DOUBLE_CLICK = ...
    """
    Pressing the left mouse button twice in quick succession.
    """
    DROP = ...
    """
    The "Drop" key (defaults to Q).
    """
    CONTROL_DROP = ...
    """
    Holding Ctrl while pressing the "Drop" key (defaults to Q).
    """
    CREATIVE = ...
    """
    Any action done with the Creative inventory open.
    """
    SWAP_OFFHAND = ...
    """
    The "swap item with offhand" key (defaults to F).
    """
    UNKNOWN = ...
    """
    A type of inventory manipulation not yet recognized by Bukkit.
    This is only for transitional purposes on a new Minecraft update, and
    should never be relied upon.
    Any ClickType.UNKNOWN is called on a best-effort basis.
    """

    def is_keyboard_click(self) -> bool:
        """
        Gets whether this ClickType represents the pressing of a key on a
        keyboard.

        @return: true if this ClickType represents the pressing of a key
        """
        ...

    def is_mouse_click(self) -> bool:
        """
        Gets whether this ClickType represents the pressing of a mouse button

        @return: true if this ClickType represents the pressing of a mouse button
        """
        ...

    def is_creative_action(self) -> bool:
        """
        Gets whether this ClickType represents an action that can only be
        performed by a Player in creative mode.

        @return: true if this action requires Creative mode
        """
        ...

    def is_right_click(self) -> bool:
        """
        Gets whether this ClickType represents a right click.

        @return: true if this ClickType represents a right click
        """
        ...

    def is_left_click(self) -> bool:
        """
        Gets whether this ClickType represents a left click.

        @return: true if this ClickType represents a left click
        """
        ...

    def is_shift_click(self) -> bool:
        """
        Gets whether this ClickType indicates that the shift key was pressed
        down when the click was made.

        @return: true if the action uses Shift.
        """
        ...