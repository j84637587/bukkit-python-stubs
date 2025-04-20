from org.bukkit.plugin import Plugin
from org.bukkit.conversations import Conversation, ConversationCanceller, ConversationContext, ConversationAbandonedEvent
from typing import Optional

class InactivityConversationCanceller(ConversationCanceller):
    """
    An InactivityConversationCanceller will cancel a {@link Conversation} after
    a period of inactivity by the user.
    """

    def __init__(self, plugin: Plugin, timeout_seconds: int) -> None:
        """
        Creates an InactivityConversationCanceller.

        :param plugin: The owning plugin.
        :param timeout_seconds: The number of seconds of inactivity to wait.
        """
        ...

    def set_conversation(self, conversation: Conversation) -> None:
        ...
    
    def cancel_based_on_input(self, context: ConversationContext, input: str) -> bool:
        ...
    
    def clone(self) -> ConversationCanceller:
        ...
    
    def start_timer(self) -> None:
        ...
    
    def stop_timer(self) -> None:
        ...
    
    def cancelling(self, conversation: Conversation) -> None:
        ...