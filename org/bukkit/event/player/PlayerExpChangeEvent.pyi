from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.jetbrains.annotations import NotNull

class PlayerExpChangeEvent(PlayerEvent):
    """
    Called when a players experience changes naturally
    """

    handlers: HandlerList = HandlerList()
    exp: int

    def __init__(self, player: Player, exp_amount: int) -> None:
        """
        Initialize the PlayerExpChangeEvent.

        :param player: The player whose experience is changing.
        :param exp_amount: The amount of experience to set.
        """
        super().__init__(player)
        self.exp = exp_amount

    def get_amount(self) -> int:
        """
        Get the amount of experience the player will receive.

        :return: The amount of experience.
        """
        return self.exp

    def set_amount(self, amount: int) -> None:
        """
        Set the amount of experience the player will receive.

        :param amount: The amount of experience to set.
        """
        self.exp = amount

        def get_handlers(self) -> HandlerList:
        return self.handlers

        @staticmethod
    def get_handler_list() -> HandlerList:
        return PlayerExpChangeEvent.handlers