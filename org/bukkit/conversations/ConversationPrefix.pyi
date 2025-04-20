from org.jetbrains.annotations import NotNull
from org.bukkit.conversations import ConversationContext

"""
A ConversationPrefix implementation prepends all output from the
conversation to the player. The ConversationPrefix can be used to display
the plugin name or conversation status as the conversation evolves.
"""
class ConversationPrefix:
    """
    Gets the prefix to use before each message to the player.

    @param context: Context information about the conversation.
    @return: The prefix text.
    """
    def get_prefix(self, context: NotNull[ConversationContext]) -> NotNull[str]:
        ...