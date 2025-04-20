from org.bukkit.entity import Player

class ServerOperator:
    """
    Represents an object that may become a server operator, such as a {@link
    Player}
    """

    def is_op(self) -> bool:
        """
        Checks if this object is a server operator

        :return: true if this is an operator, otherwise false
        """
        ...

    def set_op(self, value: bool) -> None:
        """
        Sets the operator status of this object

        :param value: New operator value
        """
        ...