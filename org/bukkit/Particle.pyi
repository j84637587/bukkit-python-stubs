from typing import Any, ClassVar, Optional
from org.bukkit import Color, Location, NamespacedKey

class Particle:
    """
    This class represents the Particle enum in the Java code.
    """
    key: Optional[NamespacedKey]
    dataType: ClassVar
    register: bool

    def __init__(self, key: str, data: ClassVar = None, register: bool = True) -> None:
        """
        Constructor for the Particle class.
        """
        pass

    def getDataType(self) -> ClassVar:
        """
        Returns the required data type for the particle.
        """
        pass

    def getKeyOrThrow(self) -> NamespacedKey:
        """
        Returns the key of the particle if it is registered.
        """
        pass

    def getKeyOrNull(self) -> Optional[NamespacedKey]:
        """
        Returns the key of the particle, or None if it is not registered.
        """
        pass

    def isRegistered(self) -> bool:
        """
        Returns whether the particle is registered.
        """
        pass

    def getKey(self) -> NamespacedKey:
        """
        Returns the key of the particle.
        """
        pass

    class DustOptions:
        """
        Options which can be applied to redstone dust particles - a particle color and size.
        """
        color: Color
        size: float

        def __init__(self, color: Color, size: float) -> None:
            """
            Constructor for the DustOptions class.
            """
            pass

        def getColor(self) -> Color:
            """
            Returns the color of the particles to be displayed.
            """
            pass

        def getSize(self) -> float:
            """
            Returns the relative size of the particle.
            """
            pass

    class DustTransition(DustOptions):
        """
        Options which can be applied to a color transitioning dust particles.
        """
        toColor: Color

        def __init__(self, fromColor: Color, toColor: Color, size: float) -> None:
            """
            Constructor for the DustTransition class.
            """
            pass

        def getToColor(self) -> Color:
            """
            Returns the final color of the particles to be displayed.
            """
            pass

    class Trail:
        """
        Options which can be applied to trail particles - a location, color and duration.
        """
        target: Location
        color: Color
        duration: int

        def __init__(self, target: Location, color: Color, duration: int) -> None:
            """
            Constructor for the Trail class.
            """
            pass

        def getTarget(self) -> Location:
            """
            Returns the target of the particles to be displayed.
            """
            pass

        def getColor(self) -> Color:
            """
            Returns the color of the particles to be displayed.
            """
            pass

        def getDuration(self) -> int:
            """
            Returns the duration of the trail to be displayed.
            """
            pass