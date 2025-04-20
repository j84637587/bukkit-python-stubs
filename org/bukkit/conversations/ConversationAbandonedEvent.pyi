from typing import Optional
from org.bukkit.conversations import Conversation
from org.bukkit.conversations import ConversationCanceller
from org.bukkit.conversations import ConversationContext
from java.util import EventObject

class ConversationAbandonedEvent(EventObject):
    """
    ConversationAbandonedEvent contains information about an abandoned
    conversation.
    """

    def __init__(self, conversation: Conversation) -> None:
        ...

    def __init__(self, conversation: Conversation, canceller: Optional[ConversationCanceller]) -> None:
        ...

    def get_canceller(self) -> Optional[ConversationCanceller]:
        """
        Gets the object that caused the conversation to be abandoned.

        Returns:
            The object that abandoned the conversation.
        """
        ...

    def get_context(self) -> ConversationContext:
        """
        Gets the abandoned conversation's conversation context.

        Returns:
            The abandoned conversation's conversation context.
        """
        ...

    def graceful_exit(self) -> bool:
        """
        Indicates how the conversation was abandoned - naturally as part of the
        prompt chain or prematurely via a ConversationCanceller.

        Returns:
            True if the conversation is abandoned gracefully by a Prompt
            returning null or the next prompt. False if the conversation is
            abandoned prematurely by a ConversationCanceller.
        """
        ...