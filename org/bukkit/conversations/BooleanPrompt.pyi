from typing import Set, Optional
from google.common.collect import ImmutableSet
from org.bukkit.conversations import ValidatingPrompt, ConversationContext, Prompt

class BooleanPrompt(ValidatingPrompt):
    """
    BooleanPrompt is the base class for any prompt that requires a boolean
    response from the user.
    """

    TRUE_INPUTS: Set[str] = ImmutableSet.of("true", "on", "yes", "y", "1", "right", "correct", "valid")
    FALSE_INPUTS: Set[str] = ImmutableSet.of("false", "off", "no", "n", "0", "wrong", "incorrect", "invalid")
    VALID_INPUTS: Set[str] = ImmutableSet.builder().addAll(TRUE_INPUTS).addAll(FALSE_INPUTS).build()

    def __init__(self) -> None:
        super().__init__()

    def is_input_valid(self, context: ConversationContext, input: str) -> bool:
        """
        @param context: Context information about the conversation.
        @param input: The user's input.
        @return: True if the input is valid, False otherwise.
        """
        return input.lower() in self.VALID_INPUTS

    def accept_validated_input(self, context: ConversationContext, input: str) -> Optional[Prompt]:
        """
        @param context: Context information about the conversation.
        @param input: The user's boolean response.
        @return: The next Prompt in the prompt graph.
        """
        return self.accept_validated_input(context, input.lower() in self.TRUE_INPUTS)

    def accept_validated_input(self, context: ConversationContext, input: bool) -> Optional[Prompt]:
        """
        Override this method to perform some action with the user's boolean
        response.

        @param context: Context information about the conversation.
        @param input: The user's boolean response.
        @return: The next Prompt in the prompt graph.
        """
        ...