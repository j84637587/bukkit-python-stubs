from typing import List, Dict, Optional, TypeVar, Any
from org.bukkit.entity import Player
from org.bukkit.plugin import Plugin
from org.bukkit.conversations import Conversation, ConversationPrefix, Prompt, ConversationCanceller, ConversationAbandonedListener, Conversable
from org.jetbrains.annotations import NotNull, Nullable

T = TypeVar('T')

class ConversationFactory:
    """
    A ConversationFactory is responsible for creating a {@link Conversation}
    from a predefined template. A ConversationFactory is typically created when
    a plugin is instantiated and builds a Conversation each time a user
    initiates a conversation with the plugin. Each Conversation maintains its
    own state and calls back as needed into the plugin.
    <p>
    The ConversationFactory implements a fluid API, allowing parameters to be
    set as an extension to the constructor.
    """

    def __init__(self, plugin: Plugin) -> None:
        """
        Constructs a ConversationFactory.

        @param plugin The plugin that owns the factory.
        """
        ...

        def with_modality(self, modal: bool) -> 'ConversationFactory':
        """
        Sets the modality of all {@link Conversation}s created by this factory.
        If a conversation is modal, all messages directed to the player are
        suppressed for the duration of the conversation.
        <p>
        The default is True.

        @param modal The modality of all conversations to be created.
        @return This object.
        """
        ...

        def with_local_echo(self, local_echo_enabled: bool) -> 'ConversationFactory':
        """
        Sets the local echo status for all {@link Conversation}s created by
        this factory. If local echo is enabled, any text submitted to a
        conversation gets echoed back into the submitter's chat window.

        @param localEchoEnabled The status of local echo.
        @return This object.
        """
        ...

        def with_prefix(self, prefix: ConversationPrefix) -> 'ConversationFactory':
        """
        Sets the {@link ConversationPrefix} that prepends all output from all
        generated conversations.
        <p>
        The default is a {@link NullConversationPrefix};

        @param prefix The ConversationPrefix to use.
        @return This object.
        """
        ...

        def with_timeout(self, timeout_seconds: int) -> 'ConversationFactory':
        """
        Sets the number of inactive seconds to wait before automatically
        abandoning all generated conversations.
        <p>
        The default is 600 seconds (5 minutes).

        @param timeoutSeconds The number of seconds to wait.
        @return This object.
        """
        ...

        def with_first_prompt(self, first_prompt: Optional[Prompt]) -> 'ConversationFactory':
        """
        Sets the first prompt to use in all generated conversations.
        <p>
        The default is Prompt.END_OF_CONVERSATION.

        @param firstPrompt The first prompt.
        @return This object.
        """
        ...

        def with_initial_session_data(self, initial_session_data: Dict[object, object]) -> 'ConversationFactory':
        """
        Sets any initial data with which to populate the conversation context
        sessionData map.

        @param initialSessionData The conversation context's initial
            sessionData.
        @return This object.
        """
        ...

        def with_escape_sequence(self, escape_sequence: str) -> 'ConversationFactory':
        """
        Sets the player input that, when received, will immediately terminate
        the conversation.

        @param escapeSequence Input to terminate the conversation.
        @return This object.
        """
        ...

        def with_conversation_canceller(self, canceller: ConversationCanceller) -> 'ConversationFactory':
        """
        Adds a {@link ConversationCanceller} to constructed conversations.

        @param canceller The {@link ConversationCanceller} to add.
        @return This object.
        """
        ...

        def that_excludes_non_players_with_message(self, player_only_message: Optional[str]) -> 'ConversationFactory':
        """
        Prevents this factory from creating a conversation for non-player
        {@link Conversable} objects.

        @param playerOnlyMessage The message to return to a non-play in lieu of
            starting a conversation.
        @return This object.
        """
        ...

        def add_conversation_abandoned_listener(self, listener: ConversationAbandonedListener) -> 'ConversationFactory':
        """
        Adds a {@link ConversationAbandonedListener} to all conversations
        constructed by this factory.

        @param listener The listener to add.
        @return This object.
        """
        ...

        def build_conversation(self, for_whom: Conversable) -> Conversation:
        """
        Constructs a {@link Conversation} in accordance with the defaults set
        for this factory.

        @param forWhom The entity for whom the new conversation is mediating.
        @return A new conversation.
        """
        ...

    class NotPlayerMessagePrompt(Prompt):
        """
        A prompt that displays a message when a non-player attempts to start a conversation.
        """

                def get_prompt_text(self, context: 'ConversationContext') -> str:
            ...

                def get_next_prompt(self, context: 'ConversationContext') -> Optional[Prompt]:
            ...