from org.bukkit.entity import AbstractHorse

class SkeletonHorse(AbstractHorse):
    """
    Represents a SkeletonHorse - variant of {@link AbstractHorse}.
    """

    def is_trapped(self) -> bool:
        """
        Returns whether this skeleton horse is trapped.
        <p>
        When a horse is trapped and a player comes within 10 blocks of a trapped
        horse, lightning will strike the horse. When struck, the skeleton trap
        will activate, turning the horse into a skeleton horseman as well as
        spawning three additional horsemen nearby.

        @return: true if trapped
        """
        ...

    def set_trapped(self, trapped: bool) -> None:
        """
        Sets if this skeleton horse is trapped.

        @param trapped: new trapped state
        """
        ...

    def get_trap_time(self) -> int:
        """
        Returns the horse's current trap time in ticks.

        Trap time is incremented every tick when {@link #isTrapped()} is true.
        The horse automatically despawns when it reaches 18000 ticks.

        @return: current trap time
        """
        ...

    def set_trap_time(self, trap_time: int) -> None:
        """
        Sets the trap time for the horse.

        Values greater than 18000 will cause the horse to despawn on the next
        tick.

        @param trap_time: new trap time
        """
        ...