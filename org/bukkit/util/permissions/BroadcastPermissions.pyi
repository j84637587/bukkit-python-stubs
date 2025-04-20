from org.bukkit.permissions import Permission
from org.bukkit.permissions import PermissionDefault
from org.jetbrains.annotations import NotNull

class BroadcastPermissions:
    ROOT: str = "bukkit.broadcast"
    PREFIX: str = ROOT + "."

    def __init__(self) -> None:
        """Private constructor to prevent instantiation."""
        pass

    @staticmethod
        def register_permissions(parent: Permission) -> Permission:
        """Registers broadcast permissions.

        Args:
            parent (Permission): The parent permission.

        Returns:
            Permission: The permission that allows receiving all broadcast messages.
        """
        broadcasts: Permission = DefaultPermissions.register_permission(
            BroadcastPermissions.ROOT,
            "Allows the user to receive all broadcast messages",
            parent
        )

        DefaultPermissions.register_permission(
            BroadcastPermissions.PREFIX + "admin",
            "Allows the user to receive administrative broadcasts",
            PermissionDefault.OP,
            broadcasts
        )
        DefaultPermissions.register_permission(
            BroadcastPermissions.PREFIX + "user",
            "Allows the user to receive user broadcasts",
            PermissionDefault.TRUE,
            broadcasts
        )

        broadcasts.recalculate_permissibles()

        return broadcasts