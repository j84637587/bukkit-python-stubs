from typing import Protocol, Any
from org.bukkit.conversations import Conversation, ConversationContext

class ConversationCanceller(Protocol):
    """
    A ConversationCanceller is a class that cancels an active {@link
    Conversation}. A Conversation can have more than one ConversationCanceller.
    """

    def set_conversation(self, conversation: Conversation) -> None:
        """
        Sets the conversation this ConversationCanceller can optionally cancel.

        :param conversation: A conversation.
        """
        ...

    def cancel_based_on_input(self, context: ConversationContext, input: str) -> bool:
        """
        Cancels a conversation based on user input.

        :param context: Context information about the conversation.
        :param input: The input text from the user.
        :return: True to cancel the conversation, False otherwise.
        """
        ...

    def clone(self) -> 'ConversationCanceller':
        """
        Allows the {@link ConversationFactory} to duplicate this
        ConversationCanceller when creating a new {@link Conversation}.
        <p>
        Implementing this method should reset any internal object state.

        :return: A clone.
        """
        ...