from typing import Optional
from org.bukkit.map import MapView, MapCursorCollection, MapFont
from java.awt import Color, Image

"""
Represents a canvas for drawing to a map. Each canvas is associated with a
specific {@link MapRenderer} and represents that renderer's layer on the
map.
"""
class MapCanvas:

    """
    Get the map this canvas is attached to.

    @return The MapView this canvas is attached to.
    """
    def get_map_view(self) -> MapView:
        ...

    """
    Get the cursor collection associated with this canvas.

    @return The MapCursorCollection associated with this canvas.
    """
    def get_cursors(self) -> MapCursorCollection:
        ...

    """
    Set the cursor collection associated with this canvas. This does not
    usually need to be called since a MapCursorCollection is already
    provided.

    @param cursors The MapCursorCollection to associate with this canvas.
    """
    def set_cursors(self, cursors: MapCursorCollection) -> None:
        ...

    """
    Draw a pixel to the canvas.
    <p>
    The provided color might be converted to another color,
    which is in the map color range. This means, that
    {@link #getPixelColor(int, int)} might return another
    color than set.

    If null is used as color, then the color returned by
    {@link #getBasePixelColor(int, int)} is shown on the map.

    @param x The x coordinate, from 0 to 127.
    @param y The y coordinate, from 0 to 127.
    @param color The color.
    """
    def set_pixel_color(self, x: int, y: int, color: Optional[Color]) -> None:
        ...

    """
    Get a pixel from the canvas.

    If no color is set at the given position for this canvas, then null is
    returned and the color returned by {@link #getBasePixelColor(int, int)}
    is shown on the map.

    @param x The x coordinate, from 0 to 127.
    @param y The y coordinate, from 0 to 127.
    @return The color, or null if no color is set.
    """
    def get_pixel_color(self, x: int, y: int) -> Optional[Color]:
        ...

    """
    Get a pixel from the layers below this canvas.

    @param x The x coordinate, from 0 to 127.
    @param y The y coordinate, from 0 to 127.
    @return The color.
    """
    def get_base_pixel_color(self, x: int, y: int) -> Color:
        ...

    """
    Draw a pixel to the canvas.

    @param x The x coordinate, from 0 to 127.
    @param y The y coordinate, from 0 to 127.
    @param color The color. See {@link MapPalette}.
    @deprecated Magic value, use {@link #setPixelColor(int, int, Color)}
    """
    def set_pixel(self, x: int, y: int, color: int) -> None:
        ...

    """
    Get a pixel from the canvas.

    @param x The x coordinate, from 0 to 127.
    @param y The y coordinate, from 0 to 127.
    @return The color. See {@link MapPalette}.
    @deprecated Magic value, use {@link #getPixelColor(int, int)}
    """
    def get_pixel(self, x: int, y: int) -> int:
        ...

    """
    Get a pixel from the layers below this canvas.

    @param x The x coordinate, from 0 to 127.
    @param y The y coordinate, from 0 to 127.
    @return The color. See {@link MapPalette}.
    @deprecated Magic value, use {@link #getBasePixelColor(int, int)}
    """
    def get_base_pixel(self, x: int, y: int) -> int:
        ...

    """
    Draw an image to the map. The image will be clipped if necessary.

    @param x The x coordinate of the image.
    @param y The y coordinate of the image.
    @param image The Image to draw.
    """
    def draw_image(self, x: int, y: int, image: Image) -> None:
        ...

    """
    Render text to the map using fancy formatting. Newline (\n) characters
    will move down one line and return to the original column, and the text
    color can be changed using sequences such as "§12;", replacing 12 with
    the palette index of the color (see {@link MapPalette}).

    @param x The column to start rendering on.
    @param y The row to start rendering on.
    @param font The font to use.
    @param text The formatted text to render.
    """
    def draw_text(self, x: int, y: int, font: MapFont, text: str) -> None:
        ...