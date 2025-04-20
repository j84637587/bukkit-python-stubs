from re import Pattern
from typing import Any
from org.bukkit.conversations import ValidatingPrompt
from org.jetbrains.annotations import NotNull

class RegexPrompt(ValidatingPrompt):
    """
    RegexPrompt is the base class for any prompt that requires an input
    validated by a regular expression.
    """

    def __init__(self, regex: str) -> None:
        ...

    def __init__(self, pattern: Pattern) -> None:
        ...

    def __init__(self) -> None:
        ...

    def is_input_valid(self, context: 'ConversationContext', input: str) -> bool:
        ...