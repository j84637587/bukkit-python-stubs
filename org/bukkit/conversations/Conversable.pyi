from typing import Protocol, Optional
from uuid import UUID
from org.bukkit.conversations import Conversation, ConversationAbandonedEvent

class Conversable(Protocol):
    """
    The Conversable interface is used to indicate objects that can have
    conversations.
    """

    def is_conversing(self) -> bool:
        """
        Tests to see if a Conversable object is actively engaged in a
        conversation.

        Returns:
            True if a conversation is in progress
        """
        ...

    def accept_conversation_input(self, input: str) -> None:
        """
        Accepts input into the active conversation. If no conversation is in
        progress, this method does nothing.

        Args:
            input: The input message into the conversation
        """
        ...

    def begin_conversation(self, conversation: Conversation) -> bool:
        """
        Enters into a dialog with a Conversation object.

        Args:
            conversation: The conversation to begin

        Returns:
            True if the conversation should proceed, false if it has been
            enqueued
        """
        ...

    def abandon_conversation(self, conversation: Conversation) -> None:
        """
        Abandons an active conversation.

        Args:
            conversation: The conversation to abandon
        """
        ...

    def abandon_conversation_with_details(self, conversation: Conversation, details: ConversationAbandonedEvent) -> None:
        """
        Abandons an active conversation.

        Args:
            conversation: The conversation to abandon
            details: Details about why the conversation was abandoned
        """
        ...

    def send_raw_message(self, message: str) -> None:
        """
        Sends this sender a message raw

        Args:
            message: Message to be displayed
        """
        ...

    def send_raw_message_with_sender(self, sender: Optional[UUID], message: str) -> None:
        """
        Sends this sender a message raw

        Args:
            message: Message to be displayed
            sender: The sender of this message
        """
        ...