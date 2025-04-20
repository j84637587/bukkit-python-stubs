from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable
from typing import Literal

class Bell(Directional, Powerable):
    """
    'attachment' denotes how the bell is attached to its block.
    """

    def get_attachment(self) -> Attachment:
        """
        Gets the value of the 'attachment' property.

        Returns:
            the 'attachment' value
        """
        ...

    def set_attachment(self, attachment: Attachment) -> None:
        """
        Sets the value of the 'attachment' property.

        Args:
            attachment: the new 'attachment' value
        """
        ...


class Attachment:
    """
    What the bell is attached to.
    """
    FLOOR: Literal['FLOOR']
    CEILING: Literal['CEILING']
    SINGLE_WALL: Literal['SINGLE_WALL']
    DOUBLE_WALL: Literal['DOUBLE_WALL']