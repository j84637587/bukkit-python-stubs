from typing import Protocol, Any

class Conversation(Protocol):
    pass

class ConversationContext(Protocol):
    pass

class ConversationCanceller(Protocol):
    def set_conversation(self, conversation: Conversation) -> None: ...
    def cancel_based_on_input(self, context: ConversationContext, input: str) -> bool: ...
    def clone(self) -> 'ConversationCanceller': ...

class ExactMatchConversationCanceller(ConversationCanceller):
    """
    An ExactMatchConversationCanceller cancels a conversation if the user
    enters an exact input string
    """

    def __init__(self, escape_sequence: str) -> None: ...
    
    def set_conversation(self, conversation: Conversation) -> None: ...
    
    def cancel_based_on_input(self, context: ConversationContext, input: str) -> bool: ...
    
    def clone(self) -> ConversationCanceller: ...