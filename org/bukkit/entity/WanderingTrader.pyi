from org.bukkit.entity import AbstractVillager

class WanderingTrader(AbstractVillager):
    """
    Represents a wandering trader NPC
    """

    def get_despawn_delay(self) -> int:
        """
        Gets the despawn delay before this {@link WanderingTrader} is forcibly
        despawned.

        If this is less than or equal to 0, then the trader will not be
        despawned.

        @return The despawn delay before this {@link WanderingTrader} is forcibly
        despawned
        """
        ...

    def set_despawn_delay(self, despawn_delay: int) -> None:
        """
        Sets the despawn delay before this {@link WanderingTrader} is forcibly
        despawned.

        If this is less than or equal to 0, then the trader will not be
        despawned.

        @param despawn_delay The new despawn delay before this
        {@link WanderingTrader} is forcibly despawned
        """
        ...