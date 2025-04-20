from org.bukkit.Color import Color
from org.bukkit.UndefinedNullability import UndefinedNullability
from org.bukkit.map.MapView import MapView
from org.bukkit.inventory.meta.ItemMeta import ItemMeta
from typing import Optional

class MapMeta(ItemMeta):
    """
    Represents a map that can be scalable.
    """

    @Deprecated(since="1.13.2")
    def has_map_id(self) -> bool:
        """
        Checks for existence of a map ID number.

        :return: true if this has a map ID number.
        :see: #has_map_view()
        :deprecated: These methods are poor API: They rely on the caller to pass
        in an only an integer property, and have poorly defined implementation
        behavior if that integer is not a valid map (the current implementation
        for example will generate a new map with a different ID). The xxxMapView
        family of methods should be used instead.
        """
        ...

    @Deprecated(since="1.13.2")
    def get_map_id(self) -> int:
        """
        Gets the map ID that is set. This is used to determine what map is
        displayed.
        <p>
        Plugins should check that has_map_id() returns <code>true</code> before
        calling this method.

        :return: the map ID that is set
        :see: #get_map_view()
        :deprecated: These methods are poor API: They rely on the caller to pass
        in an only an integer property, and have poorly defined implementation
        behavior if that integer is not a valid map (the current implementation
        for example will generate a new map with a different ID). The xxxMapView
        family of methods should be used instead.
        """
        ...

    @Deprecated(since="1.13.2")
    def set_map_id(self, id: int) -> None:
        """
        Sets the map ID. This is used to determine what map is displayed.

        :param id: the map id to set
        :see: #set_map_view(org.bukkit.map.MapView)
        :deprecated: These methods are poor API: They rely on the caller to pass
        in an only an integer property, and have poorly defined implementation
        behavior if that integer is not a valid map (the current implementation
        for example will generate a new map with a different ID). The xxxMapView
        family of methods should be used instead.
        """
        ...

    def has_map_view(self) -> bool:
        """
        Checks for existence of an associated map.

        :return: true if this item has an associated map
        """
        ...

        def get_map_view(self) -> Optional[MapView]:
        """
        Gets the map view that is associated with this map item.

        <p>
        Plugins should check that has_map_view() returns <code>true</code> before
        calling this method.

        :return: the map view, or null if the item has_map_view(), but this map does
        not exist on the server
        """
        ...

    def set_map_view(self, map: UndefinedNullability("implementation defined") MapView) -> None:
        """
        Sets the associated map. This is used to determine what map is displayed.

        <p>
        The implementation <b>may</b> allow null to clear the associated map, but
        this is not required and is liable to generate a new (undefined) map when
        the item is first used.

        :param map: the map to set
        """
        ...

    def is_scaling(self) -> bool:
        """
        Checks to see if this map is scaling.

        :return: true if this map is scaling
        """
        ...

    def set_scaling(self, value: bool) -> None:
        """
        Sets if this map is scaling or not.

        :param value: true to scale
        """
        ...

    @Deprecated(since="1.19.4")
    def has_location_name(self) -> bool:
        """
        Checks for existence of a location name.

        :return: true if this has a location name
        :deprecated: This method does not have the expected effect and is
        actually an alias for {@link ItemMeta#hasLocalizedName()}.
        """
        ...

    @Deprecated(since="1.19.4")
        def get_location_name(self) -> Optional[str]:
        """
        Gets the location name that is set.
        <p>
        Plugins should check that has_location_name() returns <code>true</code>
        before calling this method.

        :return: the location name that is set
        :deprecated: This method does not have the expected effect and is
        actually an alias for {@link ItemMeta#getLocalizedName()}.
        """
        ...

    @Deprecated(since="1.19.4")
    def set_location_name(self, name: Optional[str]) -> None:
        """
        Sets the location name.

        :param name: the name to set
        :deprecated: This method does not have the expected effect and is
        actually an alias for {@link ItemMeta#setLocalizedName(String)}.
        """
        ...

    def has_color(self) -> bool:
        """
        Checks for existence of a map color.

        :return: true if this has a custom map color
        """
        ...

        def get_color(self) -> Optional[Color]:
        """
        Gets the map color that is set. A custom map color will alter the display
        of the map in an inventory slot.
        <p>
        Plugins should check that has_color() returns <code>true</code> before
        calling this method.

        :return: the map color that is set
        """
        ...

    def set_color(self, color: Optional[Color]) -> None:
        """
        Sets the map color. A custom map color will alter the display of the map
        in an inventory slot.

        :param color: the color to set
        """
        ...

        def clone(self) -> MapMeta:
        """
        Clone the MapMeta instance.

        :return: a clone of the MapMeta
        """
        ...