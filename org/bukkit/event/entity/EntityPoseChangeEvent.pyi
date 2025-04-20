from org.bukkit.entity import Entity
from org.bukkit.entity import Pose
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityPoseChangeEvent(EntityEvent):
    """
    Called when an entity changes its pose.

    @see Entity#getPose()
    """

    handlers: HandlerList = HandlerList()
    pose: Pose

    def __init__(self: "EntityPoseChangeEvent", who: Entity, pose: Pose) -> None:
        """
        Initializes the event with the entity and its new pose.

        :param who: The entity that changed its pose.
        :param pose: The new pose of the entity.
        """
        ...

    def getPose(self: "EntityPoseChangeEvent") -> Pose:
        """
        Gets the entity's new pose.

        :return: the new pose
        """
        ...

    def getHandlers(self: "EntityPoseChangeEvent") -> HandlerList:
        """
        Gets the handlers for this event.

        :return: the handler list
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: the handler list
        """
        ...