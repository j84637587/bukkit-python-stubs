from typing import List, Optional
from org.bukkit.conversations import ValidatingPrompt
from org.jetbrains.annotations import NotNull

class FixedSetPrompt(ValidatingPrompt):
    """
    FixedSetPrompt is the base class for any prompt that requires a fixed set
    response from the user.
    """

    fixedSet: List[str]

    def __init__(self, *fixedSet: str) -> None:
        """
        Creates a FixedSetPrompt from a set of strings.
        <p>
        foo = FixedSetPrompt("bar", "cheese", "panda");
        
        :param fixedSet: A fixed set of strings, one of which the user must
            type.
        """
        ...

    def __init__(self) -> None:
        ...

    def isInputValid(self, context: 'ConversationContext', input: str) -> bool:
        ...
    
    def formatFixedSet(self) -> str:
        """
        Utility function to create a formatted string containing all the
        options declared in the constructor.

        :return: the options formatted like "[bar, cheese, panda]" if bar,
            cheese, and panda were the options used
        """
        ...