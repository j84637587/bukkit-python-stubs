from org.bukkit.attribute import Attribute
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.util import Vector
from typing import Type
from org.jetbrains.annotations import NotNull

"""
Called when a living entity receives knockback.
"""
class EntityKnockbackEvent(EntityEvent, Cancellable):

    handlers: Type[HandlerList] = HandlerList()
    cause: 'KnockbackCause'
    force: float
    rawKnockback: Vector
    knockback: Vector
    cancelled: bool

    def __init__(self, entity: LivingEntity, cause: 'KnockbackCause', force: float, rawKnockback: Vector, knockback: Vector) -> None:
        ...

        def getEntity(self) -> LivingEntity:
        ...

    """
    Gets the cause of the knockback.

    @return the cause of the knockback
    """
        def getCause(self) -> 'KnockbackCause':
        ...

    """
    Gets the raw force of the knockback. <br>
    This value is based on factors such as the {@link Enchantment#KNOCKBACK}
    level of an attacker and the
    {@link Attribute#KNOCKBACK_RESISTANCE} of the entity.

    @return the knockback force
    """
    def getForce(self) -> float:
        ...

    """
    Gets the raw knockback force that will be applied to the entity. <br>
    This value is read-only, changes made to it <b>will not</b> have any
    effect on the final knockback received.

    @return the raw knockback
    @see #getFinalKnockback()
    """
        def getKnockback(self) -> Vector:
        ...

    """
    Gets the force that will be applied to the entity. <br>
    In contrast to {@link EntityKnockbackEvent#getKnockback()} this value is
    affected by the entities current velocity and whether they are touching
    the ground.
    <p>
    <b>Note:</b> this method returns a copy, changes must be applied with
    {@link #setFinalKnockback(Vector)}.

    @return the final knockback
    """
        def getFinalKnockback(self) -> Vector:
        ...

    """
    Sets the force that will be applied to the entity.

    @param knockback the force to apply
    """
        def setFinalKnockback(self, knockback: Vector) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    """
    An enum to specify the cause of the knockback.
    """
    class KnockbackCause:
        """
        Knockback caused by non-entity damage.
        """
        DAMAGE = ...

        """
        Knockback caused by an attacking entity.
        """
        ENTITY_ATTACK = ...

        """
        Knockback caused by an explosion.
        """
        EXPLOSION = ...

        """
        Knockback caused by the target blocking with a shield.
        """
        SHIELD_BLOCK = ...

        """
        Knockback caused by a sweeping attack.
        """
        SWEEP_ATTACK = ...

        """
        Knockback with an unknown cause.
        """
        UNKNOWN = ...