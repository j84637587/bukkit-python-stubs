from collections import OrderedDict
from typing import Dict, Optional
from org.bukkit.plugin import Plugin
from org.bukkit.permissions import Permissible, Permission
from org.bukkit.permissions import PermissionRemovedExecutor
from org.jetbrains.annotations import NotNull, Nullable

"""
Holds information about a permission attachment on a {@link Permissible}
object
"""
class PermissionAttachment:
    def __init__(self, plugin: Plugin, permissible: Permissible) -> None:
        ...

    """
    Gets the plugin responsible for this attachment

    @return Plugin responsible for this permission attachment
    """
        def get_plugin(self) -> Plugin:
        ...

    """
    Sets an object to be called for when this attachment is removed from a
    {@link Permissible}. May be null.

    @param ex Object to be called when this is removed
    """
    def set_removal_callback(self, ex: Optional[PermissionRemovedExecutor]) -> None:
        ...

    """
    Gets the class that was previously set to be called when this
    attachment was removed from a {@link Permissible}. May be null.

    @return Object to be called when this is removed
    """
        def get_removal_callback(self) -> Optional[PermissionRemovedExecutor]:
        ...

    """
    Gets the Permissible that this is attached to

    @return Permissible containing this attachment
    """
        def get_permissible(self) -> Permissible:
        ...

    """
    Gets a copy of all set permissions and values contained within this
    attachment.
    <p>
    This map may be modified but will not affect the attachment, as it is a
    copy.

    @return Copy of all permissions and values expressed by this attachment
    """
        def get_permissions(self) -> Dict[str, bool]:
        ...

    """
    Sets a permission to the given value, by its fully qualified name

    @param name Name of the permission
    @param value New value of the permission
    """
    def set_permission(self, name: str, value: bool) -> None:
        ...

    """
    Sets a permission to the given value

    @param perm Permission to set
    @param value New value of the permission
    """
    def set_permission(self, perm: Permission, value: bool) -> None:
        ...

    """
    Removes the specified permission from this attachment.
    <p>
    If the permission does not exist in this attachment, nothing will
    happen.

    @param name Name of the permission to remove
    """
    def unset_permission(self, name: str) -> None:
        ...

    """
    Removes the specified permission from this attachment.
    <p>
    If the permission does not exist in this attachment, nothing will
    happen.

    @param perm Permission to remove
    """
    def unset_permission(self, perm: Permission) -> None:
        ...

    """
    Removes this attachment from its registered {@link Permissible}

    @return true if the permissible was removed successfully, false if it
        did not exist
    """
    def remove(self) -> bool:
        ...