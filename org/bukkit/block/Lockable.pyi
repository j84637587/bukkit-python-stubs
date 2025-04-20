from typing import Optional
from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

"""
Represents a block (usually a container) that may be locked. When a lock is
active an item with a name corresponding to the key will be required to open
this block.
"""
class Lockable:

    """
    Checks if the container has a valid (non empty) key.

    @return true if the key is valid.
    """
    def is_locked(self) -> bool: ...

    """
    Gets the key needed to access the container.

    @return the key needed.
    @deprecated locks are not necessarily pure strings
    """
        @Deprecated(since="1.21.2")
    def get_lock(self) -> str: ...

    """
    Sets the key required to access this container. Set to null (or empty
    string) to remove key.

    @param key the key required to access the container.
    @deprecated locks are not necessarily pure strings
    """
    @Deprecated(since="1.21.2")
    def set_lock(self, key: Optional[str]) -> None: ...

    """
    Sets the key required to access this container. All explicit
    modifications to the set key will be required to match on the opening
    key. Set to null to remove key.

    @param key the key required to access the container.
    """
        def set_lock_item(self, key: Optional[ItemStack]) -> None: ...