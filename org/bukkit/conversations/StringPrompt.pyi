from org.bukkit.conversations import Prompt
from org.bukkit.conversations import ConversationContext
from typing import Protocol

class StringPrompt(Protocol):
    """
    StringPrompt is the base class for any prompt that accepts an arbitrary
    string from the user.
    """

    def blocks_for_input(self, context: ConversationContext) -> bool:
        """
        Ensures that the prompt waits for the user to provide input.

        :param context: Context information about the conversation.
        :return: True.
        """
        ...