from typing import List, Optional
from org.bukkit import World
from org.bukkit.inventory.meta import MapMeta
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a map item.
"""
class MapView:

    class Scale:
        CLOSEST: 'Scale'
        CLOSE: 'Scale'
        NORMAL: 'Scale'
        FAR: 'Scale'
        FARTHEST: 'Scale'

        def __init__(self, value: int) -> None:
            ...

        @staticmethod
        @Deprecated(since="1.6.2")
        def value_of(value: bytes) -> Optional['Scale']:
            ...

        @Deprecated(since="1.6.2")
        def get_value(self) -> bytes:
            ...

    def get_id(self) -> int:
        """
        Get the ID of this map item for use with {@link MapMeta}.

        @return The ID of the map.
        """
        ...

    def is_virtual(self) -> bool:
        """
        Check whether this map is virtual. A map is virtual if its lowermost
        MapRenderer is plugin-provided.

        @return Whether the map is virtual.
        """
        ...

        def get_scale(self) -> 'MapView.Scale':
        """
        Get the scale of this map.

        @return The scale of the map.
        """
        ...

    def set_scale(self, scale: 'MapView.Scale') -> None:
        """
        Set the scale of this map.

        @param scale The scale to set.
        """
        ...

    def get_center_x(self) -> int:
        """
        Get the center X position of this map.

        @return The center X position.
        """
        ...

    def get_center_z(self) -> int:
        """
        Get the center Z position of this map.

        @return The center Z position.
        """
        ...

    def set_center_x(self, x: int) -> None:
        """
        Set the center X position of this map.

        @param x The center X position.
        """
        ...

    def set_center_z(self, z: int) -> None:
        """
        Set the center Z position of this map.

        @param z The center Z position.
        """
        ...

        def get_world(self) -> Optional[World]:
        """
        Get the world that this map is associated with. Primarily used by the
        internal renderer, but may be used by external renderers. May return
        null if the world the map is associated with is not loaded.

        @return The World this map is associated with.
        """
        ...

    def set_world(self, world: 'World') -> None:
        """
        Set the world that this map is associated with. The world is used by
        the internal renderer, and may also be used by external renderers.

        @param world The World to associate this map with.
        """
        ...

        def get_renderers(self) -> List['MapRenderer']:
        """
        Get a list of MapRenderers currently in effect.

        @return A {@code List<MapRenderer>} containing each map renderer.
        """
        ...

    def add_renderer(self, renderer: 'MapRenderer') -> None:
        """
        Add a renderer to this map.

        @param renderer The MapRenderer to add.
        """
        ...

    def remove_renderer(self, renderer: Optional['MapRenderer']) -> bool:
        """
        Remove a renderer from this map.

        @param renderer The MapRenderer to remove.
        @return True if the renderer was successfully removed.
        """
        ...

    def is_tracking_position(self) -> bool:
        """
        Gets whether a position cursor should be shown when the map is near its
        center.

        @return tracking status
        """
        ...

    def set_tracking_position(self, tracking_position: bool) -> None:
        """
        Sets whether a position cursor should be shown when the map is near its
        center.

        @param tracking_position tracking status
        """
        ...

    def is_unlimited_tracking(self) -> bool:
        """
        Whether the map will show a smaller position cursor (true), or no
        position cursor (false) when cursor is outside of map's range.

        @return unlimited tracking state
        """
        ...

    def set_unlimited_tracking(self, unlimited: bool) -> None:
        """
        Whether the map will show a smaller position cursor (true), or no
        position cursor (false) when cursor is outside of map's range.

        @param unlimited tracking state
        """
        ...

    def is_locked(self) -> bool:
        """
        Gets whether the map is locked or not.

        A locked map may not be explored further.

        @return lock status
        """
        ...

    def set_locked(self, locked: bool) -> None:
        """
        Gets whether the map is locked or not.

        A locked map may not be explored further.

        @param locked status
        """
        ...