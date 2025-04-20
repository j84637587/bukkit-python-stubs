from org.bukkit.ChatColor import ChatColor
from org.jetbrains.annotations import NotNull, Nullable
from org.bukkit.conversations import Prompt, ConversationContext

"""
ValidatingPrompt is the base class for any prompt that requires validation.
ValidatingPrompt will keep replaying the prompt text until the user enters
a valid response.
"""
class ValidatingPrompt(Prompt):
    def __init__(self) -> None:
        super().__init__()

    """
    Accepts and processes input from the user and validates it. If
    validation fails, this prompt is returned for re-execution, otherwise
    the next Prompt in the prompt graph is returned.

    @param context Context information about the conversation.
    @param input The input text from the user.
    @return This prompt or the next Prompt in the prompt graph.
    """
        def accept_input(self, context: ConversationContext, input: str) -> Prompt:
        ...

    """
    Ensures that the prompt waits for the user to provide input.

    @param context Context information about the conversation.
    @return True.
    """
    def blocks_for_input(self, context: ConversationContext) -> bool:
        ...

    """
    Override this method to check the validity of the player's input.

    @param context Context information about the conversation.
    @param input The player's raw console input.
    @return True or false depending on the validity of the input.
    """
    @abstractmethod
    def is_input_valid(self, context: ConversationContext, input: str) -> bool:
        ...

    """
    Override this method to accept and processes the validated input from
    the user. Using the input, the next Prompt in the prompt graph should
    be returned.

    @param context Context information about the conversation.
    @param input The validated input text from the user.
    @return The next Prompt in the prompt graph.
    """
        @abstractmethod
    def accept_validated_input(self, context: ConversationContext, input: str) -> Prompt:
        ...

    """
    Optionally override this method to display an additional message if the
    user enters an invalid input.

    @param context Context information about the conversation.
    @param invalidInput The invalid input provided by the user.
    @return A message explaining how to correct the input.
    """
        def get_failed_validation_text(self, context: ConversationContext, invalid_input: str) -> str:
        ...