from org.bukkit.permissions import Permission
from org.bukkit.permissions import PermissionDefault
from org.jetbrains.annotations import NotNull

class CommandPermissions:
    ROOT: str = "bukkit.command"
    PREFIX: str = ROOT + "."

    def __init__(self) -> None:
        """Private constructor to prevent instantiation."""
        ...

    @staticmethod
        def register_permissions(parent: Permission) -> Permission:
        """Registers permissions for CraftBukkit commands.

        Args:
            parent (Permission): The parent permission.

        Returns:
            Permission: The registered permission.
        """
        ...