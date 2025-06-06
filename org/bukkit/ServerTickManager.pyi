from org.bukkit.entity import Entity
from typing import Any

"""
Manages ticking within a server.

To learn more about the features surrounding this interface.

@see <a href="https://minecraft.wiki/w/Commands/tick">Tick Command</a>
"""
class ServerTickManager:

    """
    Checks if the server is running normally.

    When the server is running normally it indicates that the server is not
    currently frozen.

    @return true if the server is running normally, otherwise false
    """
    def isRunningNormally(self) -> bool: ...

    """
    Checks if the server is currently stepping.

    @return true if stepping, otherwise false
    """
    def isStepping(self) -> bool: ...

    """
    Checks if the server is currently sprinting.

    @return true if sprinting, otherwise false
    """
    def isSprinting(self) -> bool: ...

    """
    Checks if the server is currently frozen.

    @return true if the server is frozen, otherwise false
    """
    def isFrozen(self) -> bool: ...

    """
    Gets the current tick rate of the server.

    @return the current tick rate of the server
    """
    def getTickRate(self) -> float: ...

    """
    Sets the tick rate of the server.

    The normal tick rate of the server is 20. No tick rate below 1.0F or
    above 10,000 can be applied to the server.

    @param tick the tick rate to set the server to
    @throws IllegalArgumentException if tick rate is too low or too high for
    the server to handle
    """
    def setTickRate(self, tick: float) -> None: ...

    """
    Sets the server to a frozen state that does not tick most things.

    @param frozen true to freeze the server, otherwise false
    """
    def setFrozen(self, frozen: bool) -> None: ...

    """
    Steps the game a certain amount of ticks if the server is currently
    frozen.

    Steps occur when the server is in a frozen state which can be started by
    either using the in game /tick freeze command or the
    {@link #setFrozen(boolean)} method.

    @param ticks the amount of ticks to step the game for
    @return true if the game is now stepping. False if the game is not frozen
    so the request could not be fulfilled.
    """
    def stepGameIfFrozen(self, ticks: int) -> bool: ...

    """
    Stops the current stepping if stepping is occurring.

    @return true if the game is no-longer stepping. False if the server was
    not stepping or was already done stepping.
    """
    def stopStepping(self) -> bool: ...

    """
    Attempts to initiate a sprint, which executes all server ticks at a
    faster rate then normal.

    @param ticks the amount of ticks to sprint for
    @return true if a sprint was already initiated and was stopped, otherwise
    false
    """
    def requestGameToSprint(self, ticks: int) -> bool: ...

    """
    Stops the current sprint if one is currently happening.

    @return true if the game is no-longer sprinting, false if the server was
    not sprinting or was already done sprinting
    """
    def stopSprinting(self) -> bool: ...

    """
    Checks if a given entity is frozen.

    @param entity the entity to check if frozen.
    @return true if the entity is currently frozen otherwise false.
    """
    def isFrozen(self, entity: Entity) -> bool: ...

    """
    Gets the amount of frozen ticks left to run.

    @return the amount of frozen ticks left to run
    """
    def getFrozenTicksToRun(self) -> int: ...