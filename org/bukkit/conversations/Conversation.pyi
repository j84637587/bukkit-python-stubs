from typing import List, Dict, Optional

from org.bukkit.plugin import Plugin
from org.jetbrains.annotations import NotNull, Nullable
from org.bukkit.conversations import Conversable, Prompt, ConversationContext, ConversationPrefix, ConversationCanceller, ConversationAbandonedListener, ConversationAbandonedEvent, ManuallyAbandonedConversationCanceller

class Conversation:
    """
    The Conversation class is responsible for tracking the current state of a
    conversation, displaying prompts to the user, and dispatching the user's
    response to the appropriate place. Conversation objects are not typically
    instantiated directly. Instead a {@link ConversationFactory} is used to
    construct identical conversations on demand.
    <p>
    Conversation flow consists of a directed graph of {@link Prompt} objects.
    Each time a prompt gets input from the user, it must return the next prompt
    in the graph. Since each Prompt chooses the next Prompt, complex
    conversation trees can be implemented where the nature of the player's
    response directs the flow of the conversation.
    <p>
    Each conversation has a {@link ConversationPrefix} that prepends all output
    from the conversation to the player. The ConversationPrefix can be used to
    display the plugin name or conversation status as the conversation evolves.
    <p>
    Each conversation has a timeout measured in the number of inactive seconds
    to wait before abandoning the conversation. If the inactivity timeout is
    reached, the conversation is abandoned and the user's incoming and outgoing
    chat is returned to normal.
    <p>
    You should not construct a conversation manually. Instead, use the {@link
    ConversationFactory} for access to all available options.
    """

    def __init__(self, plugin: Optional[Plugin], for_whom: NotNull[Conversable], first_prompt: Optional[Prompt]) -> None:
        """
        Initializes a new Conversation.

        @param plugin The plugin that owns this conversation.
        @param forWhom The entity for whom this conversation is mediating.
        @param firstPrompt The first prompt in the conversation graph.
        """
        ...

    def __init__(self, plugin: Optional[Plugin], for_whom: NotNull[Conversable], first_prompt: Optional[Prompt], initial_session_data: NotNull[Dict[object, object]]) -> None:
        """
        Initializes a new Conversation.

        @param plugin The plugin that owns this conversation.
        @param forWhom The entity for whom this conversation is mediating.
        @param firstPrompt The first prompt in the conversation graph.
        @param initialSessionData Any initial values to put in the conversation
            context sessionData map.
        """
        ...

        def get_for_whom(self) -> Conversable:
        """
        Gets the entity for whom this conversation is mediating.

        @return The entity.
        """
        ...

    def is_modal(self) -> bool:
        """
        Gets the modality of this conversation. If a conversation is modal, all
        messages directed to the player are suppressed for the duration of the
        conversation.

        @return The conversation modality.
        """
        ...

    def set_modal(self, modal: bool) -> None:
        """
        Sets the modality of this conversation. If a conversation is modal,
        all messages directed to the player are suppressed for the duration of
        the conversation.

        @param modal The new conversation modality.
        """
        ...

    def is_local_echo_enabled(self) -> bool:
        """
        Gets the status of local echo for this conversation. If local echo is
        enabled, any text submitted to a conversation gets echoed back into the
        submitter's chat window.

        @return The status of local echo.
        """
        ...

    def set_local_echo_enabled(self, local_echo_enabled: bool) -> None:
        """
        Sets the status of local echo for this conversation. If local echo is
        enabled, any text submitted to a conversation gets echoed back into the
        submitter's chat window.

        @param localEchoEnabled The status of local echo.
        """
        ...

        def get_prefix(self) -> ConversationPrefix:
        """
        Gets the {@link ConversationPrefix} that prepends all output from this
        conversation.

        @return The ConversationPrefix in use.
        """
        ...

    def set_prefix(self, prefix: NotNull[ConversationPrefix]) -> None:
        """
        Sets the {@link ConversationPrefix} that prepends all output from this
        conversation.

        @param prefix The ConversationPrefix to use.
        """
        ...

    def add_conversation_canceller(self, canceller: NotNull[ConversationCanceller]) -> None:
        """
        Adds a {@link ConversationCanceller} to the cancellers collection.

        @param canceller The {@link ConversationCanceller} to add.
        """
        ...

        def get_cancellers(self) -> List[ConversationCanceller]:
        """
        Gets the list of {@link ConversationCanceller}s

        @return The list.
        """
        ...

        def get_context(self) -> ConversationContext:
        """
        Returns the Conversation's {@link ConversationContext}.

        @return The ConversationContext.
        """
        ...

    def begin(self) -> None:
        """
        Displays the first prompt of this conversation and begins redirecting
        the user's chat responses.
        """
        ...

        def get_state(self) -> 'ConversationState':
        """
        Returns Returns the current state of the conversation.

        @return The current state of the conversation.
        """
        ...

    def accept_input(self, input: NotNull[str]) -> None:
        """
        Passes player input into the current prompt. The next prompt (as
        determined by the current prompt) is then displayed to the user.

        @param input The user's chat text.
        """
        ...

    def add_conversation_abandoned_listener(self, listener: NotNull[ConversationAbandonedListener]) -> None:
        """
        Adds a {@link ConversationAbandonedListener}.

        @param listener The listener to add.
        """
        ...

    def remove_conversation_abandoned_listener(self, listener: NotNull[ConversationAbandonedListener]) -> None:
        """
        Removes a {@link ConversationAbandonedListener}.

        @param listener The listener to remove.
        """
        ...

    def abandon(self) -> None:
        """
        Abandons and resets the current conversation. Restores the user's
        normal chat behavior.
        """
        ...

    def abandon(self, details: NotNull[ConversationAbandonedEvent]) -> None:
        """
        Abandons and resets the current conversation. Restores the user's
        normal chat behavior.

        @param details Details about why the conversation was abandoned
        """
        ...

    def output_next_prompt(self) -> None:
        """
        Displays the next user prompt and abandons the conversation if the next
        prompt is null.
        """
        ...

    class ConversationState:
        UNSTARTED = ...
        STARTED = ...
        ABANDONED = ...