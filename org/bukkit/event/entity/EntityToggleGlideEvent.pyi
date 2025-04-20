from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityToggleGlideEvent(EntityEvent, Cancellable):
    """
    Sent when an entity's gliding status is toggled with an Elytra.
    Examples of when this event would be called:
    <ul>
        <li>Player presses the jump key while in midair and using an Elytra</li>
        <li>Player lands on ground while they are gliding (with an Elytra)</li>
    </ul>
    This can be visually estimated by the animation in which a player turns horizontal.
    """

    handlers: HandlerList

    def __init__(self, who: LivingEntity, is_gliding: bool) -> None:
        """
        Initializes the EntityToggleGlideEvent.

        :param who: The LivingEntity involved in the event.
        :param is_gliding: The gliding state of the entity.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns whether the event is cancelled.

        :return: True if the event is cancelled, otherwise False.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, otherwise False.
        """
        ...

    def isGliding(self) -> bool:
        """
        Returns true if the entity is now gliding or
        false if the entity stops gliding.

        :return: new gliding state
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Returns the handler list for this event.

        :return: The HandlerList for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Returns the static handler list for this event.

        :return: The static HandlerList for this event.
        """
        ...