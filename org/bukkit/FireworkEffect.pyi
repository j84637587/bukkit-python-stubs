from typing import List, Dict, Any
from enum import Enum

class Color:
    pass

class ConfigurationSerializable:
    pass

class FireworkEffect(ConfigurationSerializable):
    """
    Represents a single firework effect.
    """

    class Type(Enum):
        """
        The type or shape of the effect.
        """
        BALL = 0
        BALL_LARGE = 1
        STAR = 2
        BURST = 3
        CREEPER = 4

    class Builder:
        """
        This is a builder for FireworkEffects.
        """
        flicker: bool
        trail: bool
        colors: List[Color]
        fadeColors: List[Color]
        type: Type

        def with_(self, type: Type) -> 'FireworkEffect.Builder':
            """
            Specify the type of the firework effect.
            """
            pass

        def withFlicker(self) -> 'FireworkEffect.Builder':
            """
            Add a flicker to the firework effect.
            """
            pass

        def flicker(self, flicker: bool) -> 'FireworkEffect.Builder':
            """
            Set whether the firework effect should flicker.
            """
            pass

        def withTrail(self) -> 'FireworkEffect.Builder':
            """
            Add a trail to the firework effect.
            """
            pass

        def trail(self, trail: bool) -> 'FireworkEffect.Builder':
            """
            Set whether the firework effect should have a trail.
            """
            pass

        def withColor(self, color: Color) -> 'FireworkEffect.Builder':
            """
            Add a primary color to the firework effect.
            """
            pass

        def withColor(self, colors: List[Color]) -> 'FireworkEffect.Builder':
            """
            Add several primary colors to the firework effect.
            """
            pass

        def withColor(self, colors: List[Any]) -> 'FireworkEffect.Builder':
            """
            Add several primary colors to the firework effect.
            """
            pass

        def withFade(self, color: Color) -> 'FireworkEffect.Builder':
            """
            Add a fade color to the firework effect.
            """
            pass

        def withFade(self, colors: List[Color]) -> 'FireworkEffect.Builder':
            """
            Add several fade colors to the firework effect.
            """
            pass

        def withFade(self, colors: List[Any]) -> 'FireworkEffect.Builder':
            """
            Add several fade colors to the firework effect.
            """
            pass

        def build(self) -> 'FireworkEffect':
            """
            Create a FireworkEffect from the current contents of this builder.
            """
            pass

    @staticmethod
    def builder() -> 'FireworkEffect.Builder':
        """
        Construct a firework effect.
        """
        pass

    def hasFlicker(self) -> bool:
        """
        Get whether the firework effect flickers.
        """
        pass

    def hasTrail(self) -> bool:
        """
        Get whether the firework effect has a trail.
        """
        pass

    def getColors(self) -> List[Color]:
        """
        Get the primary colors of the firework effect.
        """
        pass

    def getFadeColors(self) -> List[Color]:
        """
        Get the fade colors of the firework effect.
        """
        pass

    def getType(self) -> 'FireworkEffect.Type':
        """
        Get the type of the firework effect.
        """
        pass

    @staticmethod
    def deserialize(map: Dict[str, Any]) -> ConfigurationSerializable:
        """
        Deserialize the firework effect.
        """
        pass

    def serialize(self) -> Dict[str, Any]:
        """
        Serialize the firework effect.
        """
        pass

    def __str__(self) -> str:
        pass

    def __hash__(self) -> int:
        pass

    def __eq__(self, obj: Any) -> bool:
        pass