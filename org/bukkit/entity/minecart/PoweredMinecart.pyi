from org.bukkit.entity import Minecart

class PoweredMinecart(Minecart):
    """
    Represents a powered minecart. A powered minecart moves on its own when a
    player deposits {@link org.bukkit.Material#COAL fuel}.
    """

    def get_fuel(self) -> int:
        """
        Get the number of ticks until the minecart runs out of fuel.

        @return: Number of ticks until the minecart runs out of fuel
        """
        ...

    def set_fuel(self, fuel: int) -> None:
        """
        Set the number of ticks until the minecart runs out of fuel.

        @param fuel: Number of ticks until the minecart runs out of fuel
        """
        ...