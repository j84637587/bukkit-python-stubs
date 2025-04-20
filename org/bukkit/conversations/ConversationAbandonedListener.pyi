from typing import Protocol
from org.bukkit.conversations import ConversationAbandonedEvent

class ConversationAbandonedListener(Protocol):
    """ 
    Interface for listening to abandoned conversations.
    """

    def conversation_abandoned(self, abandoned_event: ConversationAbandonedEvent) -> None:
        """
        Called whenever a Conversation is abandoned.

        :param abandoned_event: Contains details about the abandoned conversation.
        """