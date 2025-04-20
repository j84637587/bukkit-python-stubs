from typing import List, Callable, Future, TypeVar, Generic, Optional, Any
from org.bukkit.plugin import Plugin
from org.jetbrains.annotations import NotNull

T = TypeVar('T')

class BukkitScheduler:

    """
    Schedules a once off task to occur after a delay.
    <p>
    This task will be executed by the main server thread.
    
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @param delay Delay in server ticks before executing task
    @return Task id number (-1 if scheduling failed)
    """
    def schedule_sync_delayed_task(self, plugin: Plugin, task: Callable[[], None], delay: int) -> int: ...

    """
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @param delay Delay in server ticks before executing task
    @return Task id number (-1 if scheduling failed)
    @deprecated Use {@link BukkitRunnable#runTaskLater(Plugin, long)}
    """
    def schedule_sync_delayed_task(self, plugin: Plugin, task: 'BukkitRunnable', delay: int) -> int: ...

    """
    Schedules a once off task to occur as soon as possible.
    <p>
    This task will be executed by the main server thread.
    
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @return Task id number (-1 if scheduling failed)
    """
    def schedule_sync_delayed_task(self, plugin: Plugin, task: Callable[[], None]) -> int: ...

    """
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @return Task id number (-1 if scheduling failed)
    @deprecated Use {@link BukkitRunnable#runTask(Plugin)}
    """
    def schedule_sync_delayed_task(self, plugin: Plugin, task: 'BukkitRunnable') -> int: ...

    """
    Schedules a repeating task.
    <p>
    This task will be executed by the main server thread.
    
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @param delay Delay in server ticks before executing first repeat
    @param period Period in server ticks of the task
    @return Task id number (-1 if scheduling failed)
    """
    def schedule_sync_repeating_task(self, plugin: Plugin, task: Callable[[], None], delay: int, period: int) -> int: ...

    """
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @param delay Delay in server ticks before executing first repeat
    @param period Period in server ticks of the task
    @return Task id number (-1 if scheduling failed)
    @deprecated Use {@link BukkitRunnable#runTaskTimer(Plugin, long, long)}
    """
    def schedule_sync_repeating_task(self, plugin: Plugin, task: 'BukkitRunnable', delay: int, period: int) -> int: ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Schedules a once off task to occur after a delay. This task will be
    executed by a thread managed by the scheduler.
    
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @param delay Delay in server ticks before executing task
    @return Task id number (-1 if scheduling failed)
    @deprecated This name is misleading, as it does not schedule "a sync"
        task, but rather, "an async" task
    """
    def schedule_async_delayed_task(self, plugin: Plugin, task: Callable[[], None], delay: int) -> int: ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Schedules a once off task to occur as soon as possible. This task will
    be executed by a thread managed by the scheduler.
    
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @return Task id number (-1 if scheduling failed)
    @deprecated This name is misleading, as it does not schedule "a sync"
        task, but rather, "an async" task
    """
    def schedule_async_delayed_task(self, plugin: Plugin, task: Callable[[], None]) -> int: ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Schedules a repeating task. This task will be executed by a thread
    managed by the scheduler.
    
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @param delay Delay in server ticks before executing first repeat
    @param period Period in server ticks of the task
    @return Task id number (-1 if scheduling failed)
    @deprecated This name is misleading, as it does not schedule "a sync"
        task, but rather, "an async" task
    """
    def schedule_async_repeating_task(self, plugin: Plugin, task: Callable[[], None], delay: int, period: int) -> int: ...

    """
    Calls a method on the main thread and returns a Future object. This
    task will be executed by the main server thread.
    <ul>
    <li>Note: The Future.get() methods must NOT be called from the main
        thread.
    <li>Note2: There is at least an average of 10ms latency until the
        isDone() method returns true.
    </ul>
    @param <T> The callable's return type
    @param plugin Plugin that owns the task
    @param task Task to be executed
    @return Future Future object related to the task
    """
    def call_sync_method(self, plugin: Plugin, task: Callable[[], T]) -> Future[T]: ...

    """
    Removes task from scheduler.
    
    @param taskId Id number of task to be removed
    """
    def cancel_task(self, task_id: int) -> None: ...

    """
    Removes all tasks associated with a particular plugin from the
    scheduler.
    
    @param plugin Owner of tasks to be removed
    """
    def cancel_tasks(self, plugin: Plugin) -> None: ...

    """
    Check if the task currently running.
    <p>
    A repeating task might not be running currently, but will be running in
    the future. A task that has finished, and does not repeat, will not be
    running ever again.
    <p>
    Explicitly, a task is running if there exists a thread for it, and that
    thread is alive.
    
    @param taskId The task to check.
    <p>
    @return If the task is currently running.
    """
    def is_currently_running(self, task_id: int) -> bool: ...

    """
    Check if the task queued to be run later.
    <p>
    If a repeating task is currently running, it might not be queued now
    but could be in the future. A task that is not queued, and not running,
    will not be queued again.
    
    @param taskId The task to check.
    <p>
    @return If the task is queued to be run.
    """
    def is_queued(self, task_id: int) -> bool: ...

    """
    Returns a list of all active workers.
    <p>
    This list contains asynch tasks that are being executed by separate
    threads.
    
    @return Active workers
    """
    def get_active_workers(self) -> List['BukkitWorker']: ...

    """
    Returns a list of all pending tasks. The ordering of the tasks is not
    related to their order of execution.
    
    @return Active workers
    """
    def get_pending_tasks(self) -> List['BukkitTask']: ...

    """
    Returns a task that will run on the next server tick.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task(self, plugin: Plugin, task: Callable[[], None]) -> 'BukkitTask': ...

    """
    Returns a task that will run on the next server tick.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task(self, plugin: Plugin, task: Callable[[BukkitTask], None]) -> None: ...

    """
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    @deprecated Use {@link BukkitRunnable#runTask(Plugin)}
    """
    def run_task(self, plugin: Plugin, task: 'BukkitRunnable') -> 'BukkitTask': ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Returns a task that will run asynchronously.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_asynchronously(self, plugin: Plugin, task: Callable[[], None]) -> 'BukkitTask': ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Returns a task that will run asynchronously.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_asynchronously(self, plugin: Plugin, task: Callable[[BukkitTask], None]) -> None: ...

    """
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    @deprecated Use {@link BukkitRunnable#runTaskAsynchronously(Plugin)}
    """
    def run_task_asynchronously(self, plugin: Plugin, task: 'BukkitRunnable') -> 'BukkitTask': ...

    """
    Returns a task that will run after the specified number of server
    ticks.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_later(self, plugin: Plugin, task: Callable[[], None], delay: int) -> 'BukkitTask': ...

    """
    Returns a task that will run after the specified number of server
    ticks.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_later(self, plugin: Plugin, task: Callable[[BukkitTask], None], delay: int) -> None: ...

    """
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    @deprecated Use {@link BukkitRunnable#runTaskLater(Plugin, long)}
    """
    def run_task_later(self, plugin: Plugin, task: 'BukkitRunnable', delay: int) -> 'BukkitTask': ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Returns a task that will run asynchronously after the specified number
    of server ticks.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_later_asynchronously(self, plugin: Plugin, task: Callable[[], None], delay: int) -> 'BukkitTask': ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Returns a task that will run asynchronously after the specified number
    of server ticks.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_later_asynchronously(self, plugin: Plugin, task: Callable[[BukkitTask], None], delay: int) -> None: ...

    """
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    @deprecated Use {@link BukkitRunnable#runTaskLaterAsynchronously(Plugin, long)}
    """
    def run_task_later_asynchronously(self, plugin: Plugin, task: 'BukkitRunnable', delay: int) -> 'BukkitTask': ...

    """
    Returns a task that will repeatedly run until cancelled, starting after
    the specified number of server ticks.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @param period the ticks to wait between runs
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_timer(self, plugin: Plugin, task: Callable[[], None], delay: int, period: int) -> 'BukkitTask': ...

    """
    Returns a task that will repeatedly run until cancelled, starting after
    the specified number of server ticks.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @param period the ticks to wait between runs
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_timer(self, plugin: Plugin, task: Callable[[BukkitTask], None], delay: int, period: int) -> None: ...

    """
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task
    @param period the ticks to wait between runs
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    @deprecated Use {@link BukkitRunnable#runTaskTimer(Plugin, long, long)}
    """
    def run_task_timer(self, plugin: Plugin, task: 'BukkitRunnable', delay: int, period: int) -> 'BukkitTask': ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Returns a task that will repeatedly run asynchronously until cancelled,
    starting after the specified number of server ticks.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task for the first
        time
    @param period the ticks to wait between runs
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_timer_asynchronously(self, plugin: Plugin, task: Callable[[], None], delay: int, period: int) -> 'BukkitTask': ...

    """
    <b>Asynchronous tasks should never access any API in Bukkit.</b> <b>Great care
    should be taken to assure the thread-safety of asynchronous tasks.</b>
    <p>
    Returns a task that will repeatedly run asynchronously until cancelled,
    starting after the specified number of server ticks.
    
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task for the first
        time
    @param period the ticks to wait between runs
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    """
    def run_task_timer_asynchronously(self, plugin: Plugin, task: Callable[[BukkitTask], None], delay: int, period: int) -> None: ...

    """
    @param plugin the reference to the plugin scheduling task
    @param task the task to be run
    @param delay the ticks to wait before running the task for the first
        time
    @param period the ticks to wait between runs
    @return a BukkitTask that contains the id number
    @throws IllegalArgumentException if plugin is null
    @throws IllegalArgumentException if task is null
    @deprecated Use {@link BukkitRunnable#runTaskTimerAsynchronously(Plugin, long, long)}
    """
    def run_task_timer_asynchronously(self, plugin: Plugin, task: 'BukkitRunnable', delay: int, period: int) -> 'BukkitTask': ...