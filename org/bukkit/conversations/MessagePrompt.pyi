from org.bukkit.conversations import Prompt
from org.bukkit.conversations import ConversationContext
from typing import Optional

class MessagePrompt(Prompt):
    """
    MessagePrompt is the base class for any prompt that only displays a message
    to the user and requires no input.
    """

    def __init__(self) -> None:
        super().__init__()

    def blocks_for_input(self, context: ConversationContext) -> bool:
        """
        Message prompts never wait for user input before continuing.

        :param context: Context information about the conversation.
        :return: Always false.
        """
        return False

    def accept_input(self, context: ConversationContext, input: Optional[str]) -> Optional[Prompt]:
        """
        Accepts and ignores any user input, returning the next prompt in the
        prompt graph instead.

        :param context: Context information about the conversation.
        :param input: Ignored.
        :return: The next prompt in the prompt graph.
        """
        return self.get_next_prompt(context)

    def get_next_prompt(self, context: ConversationContext) -> Optional[Prompt]:
        """
        Override this method to return the next prompt in the prompt graph.

        :param context: Context information about the conversation.
        :return: The next prompt in the prompt graph.
        """
        ...