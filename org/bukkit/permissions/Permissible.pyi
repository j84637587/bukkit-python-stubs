from typing import Set, Optional
from org.bukkit.plugin import Plugin
from org.bukkit.permissions import Permission, PermissionAttachment, PermissionAttachmentInfo

"""
Represents an object that may be assigned permissions
"""
class Permissible(ServerOperator):

    """
    Checks if this object contains an override for the specified
    permission, by fully qualified name

    @param name Name of the permission
    @return true if the permission is set, otherwise false
    """
    def is_permission_set(self, name: str) -> bool: ...

    """
    Checks if this object contains an override for the specified Permission

    @param perm Permission to check
    @return true if the permission is set, otherwise false
    """
    def is_permission_set(self, perm: Permission) -> bool: ...

    """
    Gets the value of the specified permission, if set.
    <p>
    If a permission override is not set on this object, the default value
    of the permission will be returned.

    @param name Name of the permission
    @return Value of the permission
    """
    def has_permission(self, name: str) -> bool: ...

    """
    Gets the value of the specified permission, if set.
    <p>
    If a permission override is not set on this object, the default value
    of the permission will be returned

    @param perm Permission to get
    @return Value of the permission
    """
    def has_permission(self, perm: Permission) -> bool: ...

    """
    Adds a new PermissionAttachment with a single permission by
    name and value

    @param plugin Plugin responsible for this attachment, may not be null
        or disabled
    @param name Name of the permission to attach
    @param value Value of the permission
    @return The PermissionAttachment that was just created
    """
    def add_attachment(self, plugin: Plugin, name: str, value: bool) -> PermissionAttachment: ...

    """
    Adds a new empty PermissionAttachment to this object

    @param plugin Plugin responsible for this attachment, may not be null
        or disabled
    @return The PermissionAttachment that was just created
    """
    def add_attachment(self, plugin: Plugin) -> PermissionAttachment: ...

    """
    Temporarily adds a new PermissionAttachment with a single
    permission by name and value

    @param plugin Plugin responsible for this attachment, may not be null
        or disabled
    @param name Name of the permission to attach
    @param value Value of the permission
    @param ticks Amount of ticks to automatically remove this attachment
        after
    @return The PermissionAttachment that was just created
    """
    def add_attachment(self, plugin: Plugin, name: str, value: bool, ticks: int) -> Optional[PermissionAttachment]: ...

    """
    Temporarily adds a new empty PermissionAttachment to this
    object

    @param plugin Plugin responsible for this attachment, may not be null
        or disabled
    @param ticks Amount of ticks to automatically remove this attachment
        after
    @return The PermissionAttachment that was just created
    """
    def add_attachment(self, plugin: Plugin, ticks: int) -> Optional[PermissionAttachment]: ...

    """
    Removes the given PermissionAttachment from this object

    @param attachment Attachment to remove
    @throws IllegalArgumentException Thrown when the specified attachment
        isn't part of this object
    """
    def remove_attachment(self, attachment: PermissionAttachment) -> None: ...

    """
    Recalculates the permissions for this object, if the attachments have
    changed values.
    <p>
    This should very rarely need to be called from a plugin.
    """
    def recalculate_permissions(self) -> None: ...

    """
    Gets a set containing all of the permissions currently in effect by
    this object

    @return Set of currently effective permissions
    """
    def get_effective_permissions(self) -> Set[PermissionAttachmentInfo]: ...