from org.bukkit.permissions import Permissible
from org.bukkit.permissions import PermissionAttachment
from typing import Optional

class PermissionAttachmentInfo:
    """
    Holds information on a permission and which {@link PermissionAttachment}
    provides it
    """

    def __init__(self, permissible: Permissible, permission: str, attachment: Optional[PermissionAttachment], value: bool) -> None:
        """
        Initializes a new PermissionAttachmentInfo instance.

        :param permissible: Permissible this permission is for
        :param permission: Name of the permission
        :param attachment: Attachment providing this permission (may be None)
        :param value: Value of the permission
        """
        ...

    def get_permissible(self) -> Permissible:
        """
        Gets the permissible this is attached to

        :return: Permissible this permission is for
        """
        ...

    def get_permission(self) -> str:
        """
        Gets the permission being set

        :return: Name of the permission
        """
        ...

    def get_attachment(self) -> Optional[PermissionAttachment]:
        """
        Gets the attachment providing this permission. This may be None for
        default permissions (usually parent permissions).

        :return: Attachment
        """
        ...

    def get_value(self) -> bool:
        """
        Gets the value of this permission

        :return: Value of the permission
        """
        ...