from typing import Optional

from org.bukkit.entity import Entity
from org.bukkit.Color import Color
from org.bukkit.util import Transformation
from org.joml import Matrix4f

"""
Represents a display entity which is designed to only have a visual function.
"""
class Display(Entity):

    """
    Gets the transformation applied to this display.

    @return the transformation
    """
    def get_transformation(self) -> Transformation:
        ...

    """
    Sets the transformation applied to this display

    @param transformation the new transformation
    """
    def set_transformation(self, transformation: Transformation) -> None:
        ...

    """
    Sets the raw transformation matrix applied to this display

    @param transformationMatrix the transformation matrix
    """
    def set_transformation_matrix(self, transformation_matrix: Matrix4f) -> None:
        ...

    """
    Gets the interpolation duration of this display.

    @return interpolation duration
    """
    def get_interpolation_duration(self) -> int:
        ...

    """
    Sets the interpolation duration of this display.

    @param duration new duration
    """
    def set_interpolation_duration(self, duration: int) -> None:
        ...

    """
    Gets the teleport duration of this display.
    <ul>
        <li>0 means that updates are applied immediately.</li>
        <li>1 means that the display entity will move from current position to the updated one over one tick.</li>
        <li>Higher values spread the movement over multiple ticks.</li>
    </ul>

    @return teleport duration
    """
    def get_teleport_duration(self) -> int:
        ...

    """
    Sets the teleport duration of this display.

    @param duration new duration
    @throws IllegalArgumentException if duration is not between 0 and 59
    @see #getTeleportDuration()
    """
    def set_teleport_duration(self, duration: int) -> None:
        ...

    """
    Gets the view distance/range of this display.

    @return view range
    """
    def get_view_range(self) -> float:
        ...

    """
    Sets the view distance/range of this display.

    @param range new range
    """
    def set_view_range(self, range: float) -> None:
        ...

    """
    Gets the shadow radius of this display.

    @return radius
    """
    def get_shadow_radius(self) -> float:
        ...

    """
    Sets the shadow radius of this display.

    @param radius new radius
    """
    def set_shadow_radius(self, radius: float) -> None:
        ...

    """
    Gets the shadow strength of this display.

    @return shadow strength
    """
    def get_shadow_strength(self) -> float:
        ...

    """
    Sets the shadow strength of this display.

    @param strength new strength
    """
    def set_shadow_strength(self, strength: float) -> None:
        ...

    """
    Gets the width of this display.

    @return width
    """
    def get_display_width(self) -> float:
        ...

    """
    Sets the width of this display.

    @param width new width
    """
    def set_display_width(self, width: float) -> None:
        ...

    """
    Gets the height of this display.

    @return height
    """
    def get_display_height(self) -> float:
        ...

    """
    Sets the height if this display.

    @param height new height
    """
    def set_display_height(self, height: float) -> None:
        ...

    """
    Gets the amount of ticks before client-side interpolation will commence.

    @return interpolation delay ticks
    """
    def get_interpolation_delay(self) -> int:
        ...

    """
    Sets the amount of ticks before client-side interpolation will commence.

    @param ticks interpolation delay ticks
    """
    def set_interpolation_delay(self, ticks: int) -> None:
        ...

    """
    Gets the billboard setting of this entity.

    The billboard setting controls the automatic rotation of the entity to
    face the player.

    @return billboard setting
    """
    def get_billboard(self) -> 'Display.Billboard':
        ...

    """
    Sets the billboard setting of this entity.

    The billboard setting controls the automatic rotation of the entity to
    face the player.

    @param billboard new setting
    """
    def set_billboard(self, billboard: 'Display.Billboard') -> None:
        ...

    """
    Gets the scoreboard team overridden glow color of this display.

    @return glow color
    """
    def get_glow_color_override(self) -> Optional[Color]:
        ...

    """
    Sets the scoreboard team overridden glow color of this display.

    @param color new color
    """
    def set_glow_color_override(self, color: Optional[Color]) -> None:
        ...

    """
    Gets the brightness override of the entity.

    @return brightness override, if set
    """
    def get_brightness(self) -> Optional['Display.Brightness']:
        ...

    """
    Sets the brightness override of the entity.

    @param brightness new brightness override
    """
    def set_brightness(self, brightness: Optional['Display.Brightness']) -> None:
        ...

    class Billboard:
        """
        Describes the axes/points around which the entity can pivot.
        """
        FIXED = ...
        VERTICAL = ...
        HORIZONTAL = ...
        CENTER = ...

    class Brightness:
        """
        Represents the brightness rendering parameters of the entity.
        """
        def __init__(self, block_light: int, sky_light: int) -> None:
            ...

        """
        Gets the block lighting component of this brightness.

        @return block light, between 0-15
        """
        def get_block_light(self) -> int:
            ...

        """
        Gets the sky lighting component of this brightness.

        @return sky light, between 0-15
        """
        def get_sky_light(self) -> int:
            ...

        def __hash__(self) -> int:
            ...

        def __eq__(self, obj: object) -> bool:
            ...

        def __str__(self) -> str:
            ...