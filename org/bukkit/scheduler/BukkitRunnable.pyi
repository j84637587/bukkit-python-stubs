from org.bukkit import Bukkit
from org.bukkit.plugin import Plugin
from org.jetbrains.annotations import NotNull
from typing import NoReturn

class BukkitRunnable:
    """
    This class is provided as an easy way to handle scheduling tasks.
    """

    def isCancelled(self) -> bool:
        """
        Returns true if this task has been cancelled.

        :return: true if the task has been cancelled
        :raises IllegalStateException: if task was not scheduled yet
        """
        ...

    def cancel(self) -> NoReturn:
        """
        Attempts to cancel this task.

        :raises IllegalStateException: if task was not scheduled yet
        """
        ...

        def runTask(self, plugin: Plugin) -> 'BukkitTask':
        """
        Schedules this in the Bukkit scheduler to run on next tick.

        :param plugin: the reference to the plugin scheduling task
        :return: a BukkitTask that contains the id number
        :raises IllegalArgumentException: if plugin is null
        :raises IllegalStateException: if this was already scheduled
        """
        ...

        def runTaskAsynchronously(self, plugin: Plugin) -> 'BukkitTask':
        """
        Schedules this in the Bukkit scheduler to run asynchronously.

        :param plugin: the reference to the plugin scheduling task
        :return: a BukkitTask that contains the id number
        :raises IllegalArgumentException: if plugin is null
        :raises IllegalStateException: if this was already scheduled
        """
        ...

        def runTaskLater(self, plugin: Plugin, delay: int) -> 'BukkitTask':
        """
        Schedules this to run after the specified number of server ticks.

        :param plugin: the reference to the plugin scheduling task
        :param delay: the ticks to wait before running the task
        :return: a BukkitTask that contains the id number
        :raises IllegalArgumentException: if plugin is null
        :raises IllegalStateException: if this was already scheduled
        """
        ...

        def runTaskLaterAsynchronously(self, plugin: Plugin, delay: int) -> 'BukkitTask':
        """
        Schedules this to run asynchronously after the specified number of
        server ticks.

        :param plugin: the reference to the plugin scheduling task
        :param delay: the ticks to wait before running the task
        :return: a BukkitTask that contains the id number
        :raises IllegalArgumentException: if plugin is null
        :raises IllegalStateException: if this was already scheduled
        """
        ...

        def runTaskTimer(self, plugin: Plugin, delay: int, period: int) -> 'BukkitTask':
        """
        Schedules this to repeatedly run until cancelled, starting after the
        specified number of server ticks.

        :param plugin: the reference to the plugin scheduling task
        :param delay: the ticks to wait before running the task
        :param period: the ticks to wait between runs
        :return: a BukkitTask that contains the id number
        :raises IllegalArgumentException: if plugin is null
        :raises IllegalStateException: if this was already scheduled
        """
        ...

        def runTaskTimerAsynchronously(self, plugin: Plugin, delay: int, period: int) -> 'BukkitTask':
        """
        Schedules this to repeatedly run asynchronously until cancelled,
        starting after the specified number of server ticks.

        :param plugin: the reference to the plugin scheduling task
        :param delay: the ticks to wait before running the task for the first
            time
        :param period: the ticks to wait between runs
        :return: a BukkitTask that contains the id number
        :raises IllegalArgumentException: if plugin is null
        :raises IllegalStateException: if this was already scheduled
        """
        ...

    def getTaskId(self) -> int:
        """
        Gets the task id for this runnable.

        :return: the task id that this runnable was scheduled as
        :raises IllegalStateException: if task was not scheduled yet
        """
        ...

    def checkScheduled(self) -> NoReturn:
        ...

    def checkNotYetScheduled(self) -> NoReturn:
        ...

        def setupTask(self, task: 'BukkitTask') -> 'BukkitTask':
        ...