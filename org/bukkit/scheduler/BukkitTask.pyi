from org.bukkit.plugin import Plugin
from typing import Protocol

class BukkitTask(Protocol):
    """
    Represents a task being executed by the scheduler
    """

    def get_task_id(self) -> int:
        """
        Returns the taskId for the task.

        Returns:
            Task id number
        """
        ...

    def get_owner(self) -> Plugin:
        """
        Returns the Plugin that owns this task.

        Returns:
            The Plugin that owns the task
        """
        ...

    def is_sync(self) -> bool:
        """
        Returns true if the Task is a sync task.

        Returns:
            true if the task is run by main thread
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Returns true if this task has been cancelled.

        Returns:
            true if the task has been cancelled
        """
        ...

    def cancel(self) -> None:
        """
        Will attempt to cancel this task.
        """
        ...