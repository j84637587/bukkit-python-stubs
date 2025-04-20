from org.bukkit.permissions import PermissionAttachment
from typing import Protocol

class PermissionRemovedExecutor(Protocol):
    """Represents a class which is to be notified when a `PermissionAttachment` is removed from a `Permissible`."""

    def attachment_removed(self, attachment: PermissionAttachment) -> None:
        """Called when a `PermissionAttachment` is removed from a `Permissible`.

        Args:
            attachment: Attachment which was removed.
        """