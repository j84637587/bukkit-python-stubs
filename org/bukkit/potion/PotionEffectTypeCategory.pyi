from enum import Enum

class PotionEffectTypeCategory(Enum):
    """
    Represents a category of {@link PotionEffectType} and its effect on an entity.
    """
    BENEFICIAL = "BENEFICIAL"
    """
    Beneficial effects that positively impact an entity, such as Regeneration,
    Absorption, or Fire Resistance.
    """
    
    HARMFUL = "HARMFUL"
    """
    Harmful effects that negatively impact an entity, such as Blindness, Wither,
    or Levitation.
    """
    
    NEUTRAL = "NEUTRAL"
    """
    Neutral effects that have neither a positive nor negative effect on an
    entity, such as Glowing or Bad Omen.
    """