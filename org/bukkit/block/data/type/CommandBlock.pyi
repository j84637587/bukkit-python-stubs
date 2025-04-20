from org.bukkit.block.data import Directional

"""
'conditional' denotes whether this command block is conditional or not, i.e.
will only execute if the preceeding command block also executed successfully.
"""
class CommandBlock(Directional):
    """
    Gets the value of the 'conditional' property.

    @return the 'conditional' value
    """
    def is_conditional(self) -> bool: ...

    """
    Sets the value of the 'conditional' property.

    @param conditional the new 'conditional' value
    """
    def set_conditional(self, conditional: bool) -> None: ...