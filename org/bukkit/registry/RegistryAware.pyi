from org.bukkit import NamespacedKey
from org.bukkit import Registry
from typing import Protocol, Optional

"""
Indicates that instances of a class may be registered to the server and have a key associated with them.

@see Registry
"""
class RegistryAware(Protocol):
    """
    Gets the key of this instance if it is registered otherwise throws an error.
    <br>
    This is a convenience method and plugins should always check {@link #isRegistered()} before using this method.

    @return the key with which this instance is registered.
    @raises IllegalStateException if this instance is not registered.
    @see #isRegistered()
    @see #getKeyOrNull()
    @see Registry
    """
    def get_key_or_throw(self) -> NamespacedKey:
        ...

    """
    Gets the key of this instance if it is registered otherwise returns {@code null}.

    @return the key with which this instance is registered or {@code null} if not registered.
    @see #getKeyOrThrow()
    @see Registry
    """
    def get_key_or_null(self) -> Optional[NamespacedKey]:
        ...

    """
    Returns whether this instance is register in a registry and therefore has a key or not.

    @return true, if this instance is registered. Otherwise, false.
    @see #getKeyOrThrow()
    @see Registry
    """
    def is_registered(self) -> bool:
        ...