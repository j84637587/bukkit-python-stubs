from typing import Literal
from org.bukkit.advancement.chat_color import ChatColor

class AdvancementDisplayType:
    """
    Advancements are displayed in different ways depending on their display type.

    This enum contains information about these types and how they are
    represented.
    """

    TASK: Literal["TASK"] = "TASK"
    """
    Task or normal icons have a square icon frame.
    """

    CHALLENGE: Literal["CHALLENGE"] = "CHALLENGE"
    """
    Challenge icons have a stylised icon frame.
    """

    GOAL: Literal["GOAL"] = "GOAL"
    """
    Goal icons have a rounded icon frame.
    """

    def __init__(self, color: ChatColor) -> None:
        """
        Initialize the AdvancementDisplayType with a color.

        :param color: The chat color used by this advancement type.
        """
        ...

    def get_color(self) -> ChatColor:
        """
        The chat color used by Minecraft for this advancement.

        :return: The chat color used by this advancement type.
        """
        ...
