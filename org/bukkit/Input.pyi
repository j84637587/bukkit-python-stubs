from typing import Protocol

class Input(Protocol):
    """
    Represents a movement input applied to an entity.
    """

    def isForward(self) -> bool:
        """
        Gets whether a forward input is applied.
        
        :return: forward input
        """
        ...

    def isBackward(self) -> bool:
        """
        Gets whether a backward input is applied.
        
        :return: backward input
        """
        ...

    def isLeft(self) -> bool:
        """
        Gets whether a left input is applied.
        
        :return: left input
        """
        ...

    def isRight(self) -> bool:
        """
        Gets whether a right input is applied.
        
        :return: right input
        """
        ...

    def isJump(self) -> bool:
        """
        Gets whether a jump input is applied.
        
        :return: jump input
        """
        ...

    def isSneak(self) -> bool:
        """
        Gets whether a sneak input is applied.
        
        :return: sneak input
        """
        ...

    def isSprint(self) -> bool:
        """
        Gets whether a sprint input is applied.
        
        :return: sprint input
        """
        ...