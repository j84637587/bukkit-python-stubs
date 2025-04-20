from typing import List, Map, Set, Optional
from org.bukkit import Bukkit
from org.bukkit.plugin import Plugin
from org.bukkit.permissions import Permissible, Permission, PermissionAttachment, PermissionAttachmentInfo
from org.jetbrains.annotations import NotNull, Nullable

class PermissibleBase(Permissible):
    """
    Base Permissible for use in any Permissible object via proxy or extension
    """

    def __init__(self, opable: Optional['ServerOperator']):
        """
        :param opable: The ServerOperator that this PermissibleBase is associated with.
        """
        ...

    def is_op(self) -> bool:
        """
        :return: True if the opable is an operator, False otherwise.
        """
        ...

    def set_op(self, value: bool) -> None:
        """
        :param value: The value to set for the operator status.
        :raises UnsupportedOperationException: If no ServerOperator is set.
        """
        ...

    def is_permission_set(self, name: str) -> bool:
        """
        :param name: The name of the permission to check.
        :return: True if the permission is set, False otherwise.
        :raises IllegalArgumentException: If the permission name is null.
        """
        ...

    def is_permission_set_perm(self, perm: Permission) -> bool:
        """
        :param perm: The permission to check.
        :return: True if the permission is set, False otherwise.
        :raises IllegalArgumentException: If the permission is null.
        """
        ...

    def has_permission(self, in_name: str) -> bool:
        """
        :param in_name: The name of the permission to check.
        :return: True if the permission is granted, False otherwise.
        :raises IllegalArgumentException: If the permission name is null.
        """
        ...

    def has_permission_perm(self, perm: Permission) -> bool:
        """
        :param perm: The permission to check.
        :return: True if the permission is granted, False otherwise.
        :raises IllegalArgumentException: If the permission is null.
        """
        ...

    def add_attachment(self, plugin: Plugin, name: str, value: bool) -> PermissionAttachment:
        """
        :param plugin: The plugin requesting the attachment.
        :param name: The name of the permission to set.
        :param value: The value of the permission.
        :return: The created PermissionAttachment.
        :raises IllegalArgumentException: If the permission name or plugin is null or if the plugin is disabled.
        """
        ...

    def add_attachment_plugin(self, plugin: Plugin) -> PermissionAttachment:
        """
        :param plugin: The plugin requesting the attachment.
        :return: The created PermissionAttachment.
        :raises IllegalArgumentException: If the plugin is null or if the plugin is disabled.
        """
        ...

    def remove_attachment(self, attachment: PermissionAttachment) -> None:
        """
        :param attachment: The PermissionAttachment to remove.
        :raises IllegalArgumentException: If the attachment is null or not part of this Permissible object.
        """
        ...

    def recalculate_permissions(self) -> None:
        """
        Recalculates the permissions for this PermissibleBase.
        """
        ...

    def clear_permissions(self) -> None:
        """
        Clears all permissions for this PermissibleBase.
        """
        ...

    def calculate_child_permissions(self, children: Map[str, bool], invert: bool, attachment: Optional[PermissionAttachment]) -> None:
        """
        :param children: The child permissions to calculate.
        :param invert: Whether to invert the permission values.
        :param attachment: The PermissionAttachment associated with the permissions.
        """
        ...

    def add_attachment_with_ticks(self, plugin: Plugin, name: str, value: bool, ticks: int) -> Optional[PermissionAttachment]:
        """
        :param plugin: The plugin requesting the attachment.
        :param name: The name of the permission to set.
        :param value: The value of the permission.
        :param ticks: The number of ticks to delay the attachment.
        :return: The created PermissionAttachment, or None if it could not be added.
        :raises IllegalArgumentException: If the permission name or plugin is null or if the plugin is disabled.
        """
        ...

    def add_attachment_with_ticks_plugin(self, plugin: Plugin, ticks: int) -> Optional[PermissionAttachment]:
        """
        :param plugin: The plugin requesting the attachment.
        :param ticks: The number of ticks to delay the attachment.
        :return: The created PermissionAttachment, or None if it could not be added.
        :raises IllegalArgumentException: If the plugin is null or if the plugin is disabled.
        """
        ...

    def get_effective_permissions(self) -> Set[PermissionAttachmentInfo]:
        """
        :return: A set of effective permissions for this PermissibleBase.
        """
        ...

    class RemoveAttachmentRunnable:
        """
        Runnable to remove a PermissionAttachment.
        """

        def __init__(self, attachment: PermissionAttachment):
            """
            :param attachment: The PermissionAttachment to remove.
            """
            ...

        def run(self) -> None:
            """
            Removes the attachment.
            """
            ...