# weather_type.pyi

"""
An enum of all current weather types
"""

from enum import Enum

class WeatherType(Enum):
    """
    An enum of all current weather types
    """
    DOWNFALL = ...
    """
    Raining or snowing depending on biome.
    """
    
    CLEAR = ...
    """
    Clear weather, clouds but no rain.
    """