from typing import Collection
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from org.bukkit import Warning

class PlayerChatTabCompleteEvent(PlayerEvent):
    """
    Called when a player attempts to tab-complete a chat message.

    @deprecated This event is no longer fired due to client changes
    """
    
    handlers: HandlerList = HandlerList()
    message: str
    last_token: str
    completions: Collection[str]

    def __init__(self, who: Player, message: str, completions: Collection[str]) -> None:
        """
        Initializes the PlayerChatTabCompleteEvent.

        :param who: The player who initiated the event.
        :param message: The chat message being tab-completed.
        :param completions: The collection of possible completions.
        """
        ...

    def get_chat_message(self) -> str:
        """
        Gets the chat message being tab-completed.

        :return: the chat message
        """
        ...

    def get_last_token(self) -> str:
        """
        Gets the last 'token' of the message being tab-completed.
        
        The token is the substring starting with the character after the last
        space in the message.

        :return: The last token for the chat message
        """
        ...

    def get_tab_completions(self) -> Collection[str]:
        """
        This is the collection of completions for this event.

        :return: the current completions
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Returns the handler list for this event.

        :return: the handler list
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Returns the static handler list for this event.

        :return: the static handler list
        """
        ...