from typing import Dict, Any, Optional
from org.bukkit import Bukkit, Color, NamespacedKey, Registry
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from org.bukkit.entity import LivingEntity
from org.bukkit.potion import PotionEffectType
from java.util import Map
from java.util import NoSuchElementException

@SerializableAs("PotionEffect")
class PotionEffect(ConfigurationSerializable):
    """
    Represents a potion effect, that can be added to a {@link LivingEntity}. A
    potion effect has a duration that it will last for, an amplifier that will
    enhance its effects, and a {@link PotionEffectType}, that represents its
    effect on an entity.
    """
    
    INFINITE_DURATION: int = -1

    def __init__(self, type: PotionEffectType, duration: int, amplifier: int, ambient: bool, particles: bool, icon: bool) -> None:
        """
        Creates a potion effect.
        
        :param type: effect type
        :param duration: measured in ticks, see {@link PotionEffect#getDuration()}
        :param amplifier: the amplifier, see {@link PotionEffect#getAmplifier()}
        :param ambient: the ambient status, see {@link PotionEffect#isAmbient()}
        :param particles: the particle status, see {@link PotionEffect#hasParticles()}
        :param icon: the icon status, see {@link PotionEffect#hasIcon()}
        """
        ...

    def __init__(self, type: PotionEffectType, duration: int, amplifier: int, ambient: bool, particles: bool) -> None:
        """
        Creates a potion effect with no defined color.
        
        :param type: effect type
        :param duration: measured in ticks, see {@link PotionEffect#getDuration()}
        :param amplifier: the amplifier, see {@link PotionEffect#getAmplifier()}
        :param ambient: the ambient status, see {@link PotionEffect#isAmbient()}
        :param particles: the particle status, see {@link PotionEffect#hasParticles()}
        """
        ...

    def __init__(self, type: PotionEffectType, duration: int, amplifier: int, ambient: bool) -> None:
        """
        Creates a potion effect. Assumes that particles are visible
        
        :param type: effect type
        :param duration: measured in ticks, see {@link PotionEffect#getDuration()}
        :param amplifier: the amplifier, see {@link PotionEffect#getAmplifier()}
        :param ambient: the ambient status, see {@link PotionEffect#isAmbient()}
        """
        ...

    def __init__(self, type: PotionEffectType, duration: int, amplifier: int) -> None:
        """
        Creates a potion effect. Assumes ambient is true.
        
        :param type: Effect type
        :param duration: measured in ticks
        :param amplifier: the amplifier for the effect
        """
        ...

    def __init__(self, map: Map[str, Any]) -> None:
        """
        Constructor for deserialization.
        
        :param map: the map to deserialize from
        """
        ...

    @staticmethod
    def getEffectType(map: Map[Any, Any]) -> PotionEffectType:
        ...

    @staticmethod
    def getInt(map: Map[Any, Any], key: Any) -> int:
        ...

    @staticmethod
    def getBool(map: Map[Any, Any], key: Any, def_value: bool) -> bool:
        ...

    def serialize(self) -> Dict[str, Any]:
        ...

    def apply(self, entity: LivingEntity) -> bool:
        """
        Attempts to add the effect represented by this object to the given
        {@link LivingEntity}.
        
        :param entity: The entity to add this effect to
        :return: Whether the effect could be added
        """
        ...

    def equals(self, obj: Any) -> bool:
        ...

    def getAmplifier(self) -> int:
        """
        Returns the amplifier of this effect. A higher amplifier means the
        potion effect happens more often over its duration and in some cases
        has more effect on its target.
        
        :return: The effect amplifier
        """
        ...

    def getDuration(self) -> int:
        """
        Returns the duration (in ticks) that this effect will run for when
        applied to a {@link LivingEntity}.
        
        :return: The duration of the effect, or {@value #INFINITE_DURATION} if
        this effect is infinite
        """
        ...

    def isInfinite(self) -> bool:
        """
        Returns whether or not this potion effect has an infinite duration. Potion
        effects with infinite durations will display an infinite symbol and never
        expire unless manually removed.
        
        :return: whether this duration is infinite or not
        """
        ...

    def isShorterThan(self, other: PotionEffect) -> bool:
        """
        Returns whether or not this potion effect has a shorter duration than the
        provided potion effect.
        
        :param other: the other effect
        :return: true if this effect is shorter than the other, false if longer or equal
        """
        ...

    def getType(self) -> PotionEffectType:
        """
        Returns the {@link PotionEffectType} of this effect.
        
        :return: The potion type of this effect
        """
        ...

    def isAmbient(self) -> bool:
        """
        Makes potion effect produce more, translucent, particles.
        
        :return: if this effect is ambient
        """
        ...

    def hasParticles(self) -> bool:
        """
        @return: whether this effect has particles or not
        """
        ...

    def getColor(self) -> Optional[Color]:
        """
        @return: color of this potion's particles. May be null if the potion has no particles or defined color.
        @deprecated: color is not part of potion effects
        """
        ...

    def hasIcon(self) -> bool:
        """
        @return: whether this effect has an icon or not
        """
        ...

    def hashCode(self) -> int:
        ...

    def toString(self) -> str:
        ...