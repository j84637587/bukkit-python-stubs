from org.bukkit.plugin import Plugin
from typing import Protocol

class BukkitWorker(Protocol):
    """
    Represents a worker thread for the scheduler. This gives information about
    the Thread object for the task, owner of the task and the taskId.
    <p>
    Workers are used to execute async tasks.
    """

    def get_task_id(self) -> int:
        """
        Returns the taskId for the task being executed by this worker.

        @return: Task id number
        """
        ...

    def get_owner(self) -> Plugin:
        """
        Returns the Plugin that owns this task.

        @return: The Plugin that owns the task
        """
        ...

    def get_thread(self) -> 'Thread':
        """
        Returns the thread for the worker.

        @return: The Thread object for the worker
        """
        ...