from org.bukkit.conversations import ConversationPrefix
from org.bukkit.conversations import ConversationContext
from typing import Any

class NullConversationPrefix(ConversationPrefix):
    """NullConversationPrefix is a {@link ConversationPrefix} implementation that
    displays nothing in front of conversation output.
    """

    def get_prefix(self, context: ConversationContext) -> str:
        """Prepends each conversation message with an empty string.

        Args:
            context: Context information about the conversation.

        Returns:
            An empty string.
        """
        ...