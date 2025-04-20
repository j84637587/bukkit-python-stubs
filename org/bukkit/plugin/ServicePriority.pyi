# org/bukkit/plugin/ServicePriority.pyi

"""
Represents various priorities of a provider.
"""
from enum import Enum

class ServicePriority(Enum):
    Lowest: 'ServicePriority'
    Low: 'ServicePriority'
    Normal: 'ServicePriority'
    High: 'ServicePriority'
    Highest: 'ServicePriority'