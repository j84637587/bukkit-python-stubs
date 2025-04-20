from org.apache.commons.lang3.math import NumberUtils
from org.jetbrains.annotations import NotNull, Nullable
from org.bukkit.conversations import ValidatingPrompt, ConversationContext, Prompt

"""
NumericPrompt is the base class for any prompt that requires a {@link
Number} response from the user.
"""
class NumericPrompt(ValidatingPrompt):
    def __init__(self) -> None:
        super().__init__()

    def isInputValid(self, context: ConversationContext, input: str) -> bool:
        ...

    """
    Override this method to do further validation on the numeric player
    input after the input has been determined to actually be a number.

    @param context Context information about the conversation.
    @param input The number the player provided.
    @return The validity of the player's input.
    """
    def isNumberValid(self, context: ConversationContext, input: Number) -> bool:
        ...

        def acceptValidatedInput(self, context: ConversationContext, input: str) -> Prompt:
        ...

    """
    Override this method to perform some action with the user's integer
    response.

    @param context Context information about the conversation.
    @param input The user's response as a {@link Number}.
    @return The next {@link Prompt} in the prompt graph.
    """
        def acceptValidatedInput(self, context: ConversationContext, input: Number) -> Prompt:
        ...

        def getFailedValidationText(self, context: ConversationContext, invalidInput: str) -> str:
        ...

    """
    Optionally override this method to display an additional message if the
    user enters an invalid number.

    @param context Context information about the conversation.
    @param invalidInput The invalid input provided by the user.
    @return A message explaining how to correct the input.
    """
        def getInputNotNumericText(self, context: ConversationContext, invalidInput: str) -> str:
        ...

    """
    Optionally override this method to display an additional message if the
    user enters an invalid numeric input.

    @param context Context information about the conversation.
    @param invalidInput The invalid input provided by the user.
    @return A message explaining how to correct the input.
    """
        def getFailedValidationText(self, context: ConversationContext, invalidInput: Number) -> str:
        ...