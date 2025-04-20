"""
Represents an entity body pose.
"""
from enum import Enum

class Pose(Enum):
    """
    Entity is standing normally.
    """
    STANDING = "STANDING"
    
    """
    Entity is gliding.
    """
    FALL_FLYING = "FALL_FLYING"
    
    """
    Entity is sleeping.
    """
    SLEEPING = "SLEEPING"
    
    """
    Entity is swimming.
    """
    SWIMMING = "SWIMMING"
    
    """
    Entity is riptiding with a trident.
    """
    SPIN_ATTACK = "SPIN_ATTACK"
    
    """
    Entity is sneaking.
    """
    SNEAKING = "SNEAKING"
    
    """
    Entity is long jumping.
    """
    LONG_JUMPING = "LONG_JUMPING"
    
    """
    Entity is dead.
    """
    DYING = "DYING"
    
    """
    Entity is croaking.
    """
    CROAKING = "CROAKING"
    
    """
    Entity is using its tongue.
    """
    USING_TONGUE = "USING_TONGUE"
    
    """
    Entity is sitting.
    """
    SITTING = "SITTING"
    
    """
    Entity is roaring.
    """
    ROARING = "ROARING"
    
    """
    Entity is sniffing.
    """
    SNIFFING = "SNIFFING"
    
    """
    Entity is emerging.
    """
    EMERGING = "EMERGING"
    
    """
    Entity is digging.
    """
    DIGGING = "DIGGING"
    
    """
    Entity is sliding.
    """
    SLIDING = "SLIDING"
    
    """
    Entity is shooting.
    """
    SHOOTING = "SHOOTING"
    
    """
    Entity is inhaling.
    """
    INHALING = "INHALING"