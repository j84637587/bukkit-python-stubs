from org.bukkit.entity import Player
from org.bukkit.map import MapCanvas, MapView
from typing import Optional

class MapRenderer:
    """
    Represents a renderer for a map.
    """

    def __init__(self: "MapRenderer", contextual: Optional[bool] = False) -> None:
        """
        Initialize the map renderer base to be non-contextual. See {@link
        #isContextual()}.
        """
        ...

    def is_contextual(self: "MapRenderer") -> bool:
        """
        Get whether the renderer is contextual, i.e. has different canvases for
        different players.

        @return True if contextual, false otherwise.
        """
        ...

    def initialize(self: "MapRenderer", map: MapView) -> None:
        """
        Initialize this MapRenderer for the given map.

        @param map The MapView being initialized.
        """
        ...

    def render(self: "MapRenderer", map: MapView, canvas: MapCanvas, player: Player) -> None:
        """
        Render to the given map.

        @param map The MapView being rendered to.
        @param canvas The canvas to use for rendering.
        @param player The player who triggered the rendering.
        """
        ...