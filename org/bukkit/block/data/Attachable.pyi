from typing import Protocol

class BlockData(Protocol):
    pass

class Attachable(BlockData):
    """
    'attached' denotes whether a tripwire hook or string forms a complete
    tripwire circuit and is ready to trigger.
    <br>
    Updating the property on a tripwire hook will change the texture to indicate
    a connected string, but will not have any effect when used on the tripwire
    string itself. It may however still be used to check whether the string forms
    a circuit.
    """

    def is_attached(self) -> bool:
        """
        Gets the value of the 'attached' property.

        Returns:
            bool: the 'attached' value
        """
        ...

    def set_attached(self, attached: bool) -> None:
        """
        Sets the value of the 'attached' property.

        Args:
            attached (bool): the new 'attached' value
        """
        ...