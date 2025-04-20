from org.bukkit.conversations import Conversation
from org.bukkit.conversations import ConversationCanceller
from org.bukkit.conversations import ConversationContext
from typing import Protocol

class ManuallyAbandonedConversationCanceller(ConversationCanceller):
    """
    The ManuallyAbandonedConversationCanceller is only used as part of a {@link
    ConversationAbandonedEvent} to indicate that the conversation was manually
    abandoned by programmatically calling the abandon() method on it.
    """

    def set_conversation(self, conversation: Conversation) -> None:
        """Sets the conversation."""
        raise NotImplementedError

    def cancel_based_on_input(self, context: ConversationContext, input: str) -> bool:
        """Cancels based on input."""
        raise NotImplementedError

    def clone(self) -> ConversationCanceller:
        """Clones the canceller."""
        raise NotImplementedError