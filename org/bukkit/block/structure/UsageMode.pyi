from enum import Enum

class UsageMode(Enum):
    """
    Represents how a :class:`org.bukkit.block.Structure` can be used.
    """
    
    SAVE = 0
    """
    The mode used when saving a structure.
    """
    
    LOAD = 1
    """
    The mode used when loading a structure.
    """
    
    CORNER = 2
    """
    Used when saving a structure for easy size calculation. When using this
    mode, the Structure name MUST match the name in the second Structure
    block that is in :class:`UsageMode.SAVE`.
    """
    
    DATA = 3
    """
    Used to run specific custom functions, which can only be used for certain
    Structures. The structure block is removed after this function completes.
    The data tags (functions) can be found on the
    <a href="https://minecraft.wiki/w/Structure_Block#Data">wiki</a>.
    """