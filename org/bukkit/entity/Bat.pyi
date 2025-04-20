from org.bukkit.entity import Ambient

class Bat(Ambient):
    """Represents a Bat"""

    def is_awake(self) -> bool:
        """
        Checks the current waking state of this bat.
        This does not imply any persistence of state past the method call.

        @return: true if the bat is awake or false if it is currently hanging
            from a block
        """
        ...

    def set_awake(self, state: bool) -> None:
        """
        This method modifies the current waking state of this bat.
        This does not prevent a bat from spontaneously awaking itself, or from
        reattaching itself to a block.

        @param state: the new state
        """
        ...