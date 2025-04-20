from typing import Literal

class DeathMessageType:
    """
    Represents a type of death message used by a {@link DamageSource}.
    """
    
    DEFAULT: Literal['DEFAULT']
    FALL_VARIANTS: Literal['FALL_VARIANTS']
    INTENTIONAL_GAME_DESIGN: Literal['INTENTIONAL_GAME_DESIGN']