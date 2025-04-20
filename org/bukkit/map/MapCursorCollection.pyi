from typing import List, Optional
from org.bukkit.map import MapCursor

class MapCursorCollection:
    """
    Represents all the map cursors on a {@link MapCanvas}. Like MapCanvas, a
    MapCursorCollection is linked to a specific {@link MapRenderer}.
    """
    
    def __init__(self) -> None:
        self.cursors: List[MapCursor] = []

    def size(self) -> int:
        """
        Get the amount of cursors in this collection.

        @return: The size of this collection.
        """
        ...

    def get_cursor(self, index: int) -> MapCursor:
        """
        Get a cursor from this collection.

        @param index: The index of the cursor.
        @return: The MapCursor.
        """
        ...

    def remove_cursor(self, cursor: MapCursor) -> bool:
        """
        Remove a cursor from the collection.

        @param cursor: The MapCursor to remove.
        @return: Whether the cursor was removed successfully.
        """
        ...

    def add_cursor(self, cursor: MapCursor) -> MapCursor:
        """
        Add a cursor to the collection.

        @param cursor: The MapCursor to add.
        @return: The MapCursor that was passed.
        """
        ...

    def add_cursor(self, x: int, y: int, direction: bytes) -> MapCursor:
        """
        Add a cursor to the collection.

        @param x: The x coordinate, from -128 to 127.
        @param y: The y coordinate, from -128 to 127.
        @param direction: The facing of the cursor, from 0 to 15.
        @return: The newly added MapCursor.
        """
        ...

    def add_cursor(self, x: int, y: int, direction: bytes, type: bytes) -> MapCursor:
        """
        Add a cursor to the collection.

        @param x: The x coordinate, from -128 to 127.
        @param y: The y coordinate, from -128 to 127.
        @param direction: The facing of the cursor, from 0 to 15.
        @param type: The type (color/style) of the map cursor.
        @return: The newly added MapCursor.
        @deprecated: Magic value
        """
        ...

    def add_cursor(self, x: int, y: int, direction: bytes, type: bytes, visible: bool) -> MapCursor:
        """
        Add a cursor to the collection.

        @param x: The x coordinate, from -128 to 127.
        @param y: The y coordinate, from -128 to 127.
        @param direction: The facing of the cursor, from 0 to 15.
        @param type: The type (color/style) of the map cursor.
        @param visible: Whether the cursor is visible.
        @return: The newly added MapCursor.
        @deprecated: Magic value
        """
        ...

    def add_cursor(self, x: int, y: int, direction: bytes, type: bytes, visible: bool, caption: Optional[str]) -> MapCursor:
        """
        Add a cursor to the collection.

        @param x: The x coordinate, from -128 to 127.
        @param y: The y coordinate, from -128 to 127.
        @param direction: The facing of the cursor, from 0 to 15.
        @param type: The type (color/style) of the map cursor.
        @param visible: Whether the cursor is visible.
        @param caption: banner caption
        @return: The newly added MapCursor.
        @deprecated: Magic value
        """
        ...