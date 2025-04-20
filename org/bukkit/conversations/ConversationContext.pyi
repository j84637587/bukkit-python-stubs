from typing import Dict, Optional, Any
from org.bukkit.plugin import Plugin
from org.bukkit.conversations import Conversable

class ConversationContext:
    """
    A ConversationContext provides continuity between nodes in the prompt graph
    by giving the developer access to the subject of the conversation and a
    generic map for storing values that are shared between all {@link Prompt}
    invocations.
    """

    def __init__(self, plugin: Optional[Plugin], for_whom: Conversable, initial_session_data: Dict[object, object]) -> None:
        """
        Initializes a new ConversationContext.

        :param plugin: The owning plugin.
        :param for_whom: The subject of the conversation.
        :param initial_session_data: Any initial values to put in the sessionData
            map.
        """
        ...

    def get_plugin(self) -> Optional[Plugin]:
        """
        Gets the plugin that owns this conversation.

        :return: The owning plugin.
        """
        ...

    def get_for_whom(self) -> Conversable:
        """
        Gets the subject of the conversation.

        :return: The subject of the conversation.
        """
        ...

    def get_all_session_data(self) -> Dict[object, object]:
        """
        Gets the underlying sessionData map.

        May be directly modified to manipulate session data.

        :return: The full sessionData map.
        """
        ...

    def get_session_data(self, key: object) -> Optional[object]:
        """
        Gets session data shared between all {@link Prompt} invocations. Use
        this as a way to pass data through each Prompt as the conversation
        develops.

        :param key: The session data key.
        :return: The requested session data.
        """
        ...

    def set_session_data(self, key: object, value: Optional[object]) -> None:
        """
        Sets session data shared between all {@link Prompt} invocations. Use
        this as a way to pass data through each prompt as the conversation
        develops.

        :param key: The session data key.
        :param value: The session data value.
        """
        ...