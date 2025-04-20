from org.bukkit.conversations import ValidatingPrompt, ConversationContext, Prompt
from org.bukkit.entity import Player
from org.bukkit.plugin import Plugin
from typing import Optional

class PlayerNamePrompt(ValidatingPrompt):
    """
    PlayerNamePrompt is the base class for any prompt that requires the player
    to enter another player's name.
    """

    def __init__(self, plugin: Plugin) -> None:
        ...

    def is_input_valid(self, context: ConversationContext, input: str) -> bool:
        ...

    def accept_validated_input(self, context: ConversationContext, input: str) -> Optional[Prompt]:
        ...

    def accept_validated_input(self, context: ConversationContext, input: Player) -> Optional[Prompt]:
        """
        Override this method to perform some action with the user's player name
        response.

        :param context: Context information about the conversation.
        :param input: The user's player name response.
        :return: The next {@link Prompt} in the prompt graph.
        """
        ...