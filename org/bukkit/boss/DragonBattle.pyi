from typing import Collection, Optional
from org.bukkit.Location import Location
from org.bukkit.entity.EnderCrystal import EnderCrystal
from org.bukkit.entity.EnderDragon import EnderDragon
from org.bukkit.boss.BossBar import BossBar
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a dragon battle state for a world with an end environment.
"""
class DragonBattle:

    """
    Get the {@link EnderDragon} active in this battle.
    <br>
    Will return null if the dragon has been slain.

    @return the ender dragon. null if dead
    """
        def getEnderDragon(self) -> Optional[EnderDragon]: ...

    """
    Get the boss bar to be displayed for this dragon battle.

    @return the boss bar
    """
        def getBossBar(self) -> BossBar: ...

    """
    Get the location of the end portal.
    <br>
    This location will be at the center of the base (bottom) of the portal.

    @return the end portal location or null if not generated
    """
        def getEndPortalLocation(self) -> Optional[Location]: ...

    """
    Generate the end portal.

    @param withPortals whether end portal blocks should be generated

    @return true if generated, false if already present
    """
    def generateEndPortal(self, withPortals: bool) -> bool: ...

    """
    Check whether the first dragon has been killed already.

    @return true if killed before, false otherwise
    """
    def hasBeenPreviouslyKilled(self) -> bool: ...

    """
    Sets whether the first dragon has been killed already.
    <br>
    If the dragon has not previously been killed, a portal will be generated
    when it is finally killed.

    @param previouslyKilled true if the dragon has been killed before, false
    otherwise
    """
    def setPreviouslyKilled(self, previouslyKilled: bool) -> None: ...

    """
    Try to initiate a respawn sequence to summon the dragon as though a player has
    placed 4 end crystals on the portal.
    """
    def initiateRespawn(self) -> None: ...

    """
    Try to initiate a respawn sequence to summon the dragon.

    @param enderCrystals the {@link EnderCrystal EnderCrystals} to use in the
    respawn, or a null or empty list to render the respawn sequence
    uncancellable. null entries or crystals that do not reside in the same
    world as this dragon battle will be ignored.

    @return true if the respawn was initiated, false otherwise.
    """
    def initiateRespawn(self, enderCrystals: Optional[Collection[EnderCrystal]]) -> bool: ...

    """
    Get this battle's current respawn phase.

    @return the current respawn phase.
    """
        def getRespawnPhase(self) -> RespawnPhase: ...

    """
    Set the dragon's respawn phase.
    <br>
    This method will is unsuccessful if a dragon respawn is not in progress.

    @param phase the phase to set

    @return true if successful, false otherwise

    @see #initiateRespawn()
    """
    def setRespawnPhase(self, phase: RespawnPhase) -> bool: ...

    """
    Reset the crystals located on the obsidian pillars (remove their beam
    targets and invulnerability).
    """
    def resetCrystals(self) -> None: ...

    """
    Represents a phase in the dragon respawn process.
    """
    class RespawnPhase:
        """
        The crystal beams are directed upwards into the sky.
        """
        START = ...  # type: RespawnPhase
        """
        The crystal beams remain directed upwards.
        """
        PREPARING_TO_SUMMON_PILLARS = ...  # type: RespawnPhase
        """
        The crystal beams are directed from pillar to pillar, regenerating
        their crystals if necessary.
        """
        SUMMONING_PILLARS = ...  # type: RespawnPhase
        """
        All crystals (including those from the pillars) are aimed towards the
        sky. Shortly thereafter summoning the dragon and destroying the
        crystals used to initiate the dragon's respawn.
        """
        SUMMONING_DRAGON = ...  # type: RespawnPhase
        """
        The end of the respawn sequence. The dragon is actually summoned.
        """
        END = ...  # type: RespawnPhase
        """
        No respawn is in progress.
        """
        NONE = ...  # type: RespawnPhase