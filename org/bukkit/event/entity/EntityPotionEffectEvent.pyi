from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.potion import PotionEffect, PotionEffectType
from typing import Optional, Type

class EntityPotionEffectEvent(EntityEvent, Cancellable):
    """
    Called when a potion effect is modified on an entity.
    <p>
    If the event is cancelled, no change will be made on the entity.
    """

    handlers: HandlerList

    def __init__(self, living_entity: LivingEntity, old_effect: Optional[PotionEffect], new_effect: Optional[PotionEffect], cause: 'Cause', action: 'Action', override: bool) -> None:
        ...

    @Optional
    def getOldEffect(self) -> Optional[PotionEffect]:
        """
        Gets the old potion effect of the changed type, which will be removed.

        @return The old potion effect or null if the entity did not have the
        changed effect type.
        """
        ...

    @Optional
    def getNewEffect(self) -> Optional[PotionEffect]:
        """
        Gets new potion effect of the changed type to be applied.

        @return The new potion effect or null if the effect of the changed type
        will be removed.
        """
        ...

    def getCause(self) -> 'Cause':
        """
        Gets the cause why the effect has changed.

        @return A Cause value why the effect has changed.
        """
        ...

    def getAction(self) -> 'Action':
        """
        Gets the action which will be performed on the potion effect type.

        @return An action to be performed on the potion effect type.
        """
        ...

    def getModifiedType(self) -> PotionEffectType:
        """
        Gets the modified potion effect type.

        @return The effect type which will be modified on the entity.
        """
        ...

    def isOverride(self) -> bool:
        """
        Returns if the new potion effect will override the old potion effect
        (Only applicable for the CHANGED Action).

        @return If the new effect will override the old one.
        """
        ...

    def setOverride(self, override: bool) -> None:
        """
        Sets if the new potion effect will override the old potion effect (Only
        applicable for the CHANGED action).

        @param override If the new effect will override the old one.
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        ...

class Action:
    """
    An enum to specify the action to be performed.
    """
    ADDED: Type['Action']
    CHANGED: Type['Action']
    CLEARED: Type['Action']
    REMOVED: Type['Action']

class Cause:
    """
    An enum to specify the cause why an effect was changed.
    """
    AREA_EFFECT_CLOUD: Type['Cause']
    ARROW: Type['Cause']
    ATTACK: Type['Cause']
    AXOLOTL: Type['Cause']
    BEACON: Type['Cause']
    COMMAND: Type['Cause']
    CONDUIT: Type['Cause']
    CONVERSION: Type['Cause']
    DEATH: Type['Cause']
    DOLPHIN: Type['Cause']
    EXPIRATION: Type['Cause']
    FOOD: Type['Cause']
    ILLUSION: Type['Cause']
    MILK: Type['Cause']
    PATROL_CAPTAIN: Type['Cause']
    PLUGIN: Type['Cause']
    POTION_DRINK: Type['Cause']
    POTION_SPLASH: Type['Cause']
    SPIDER_SPAWN: Type['Cause']
    TOTEM: Type['Cause']
    TURTLE_HELMET: Type['Cause']
    UNKNOWN: Type['Cause']
    VILLAGER_TRADE: Type['Cause']
    WARDEN: Type['Cause']
    WITHER_ROSE: Type['Cause']