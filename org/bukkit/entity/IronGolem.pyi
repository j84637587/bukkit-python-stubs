from org.bukkit.entity import Golem

class IronGolem(Golem):
    """
    An iron Golem that protects Villages.
    """

    def is_player_created(self) -> bool:
        """
        Gets whether this iron golem was built by a player.

        :return: Whether this iron golem was built by a player
        """
        ...

    def set_player_created(self, player_created: bool) -> None:
        """
        Sets whether this iron golem was built by a player or not.

        :param player_created: true if you want to set the iron golem as being
            player created, false if you want it to be a natural village golem.
        """
        ...