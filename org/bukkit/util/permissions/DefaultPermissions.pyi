from typing import Dict, Optional
from org.bukkit import Bukkit
from org.bukkit.permissions import Permission, PermissionDefault

class DefaultPermissions:
    ROOT: str = "craftbukkit"
    LEGACY_PREFIX: str = "craft"

    def __init__(self) -> None:
        """Private constructor to prevent instantiation."""
        pass

    @staticmethod
    def register_permission(perm: Permission) -> Permission:
        """Register a permission.

        Args:
            perm (Permission): The permission to register.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_permission(perm: Permission, with_legacy: bool) -> Permission:
        """Register a permission with an option for legacy support.

        Args:
            perm (Permission): The permission to register.
            with_legacy (bool): Whether to register the legacy permission.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_permission(perm: Permission, parent: Permission) -> Permission:
        """Register a permission with a parent permission.

        Args:
            perm (Permission): The permission to register.
            parent (Permission): The parent permission.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_permission(name: str, desc: Optional[str]) -> Permission:
        """Register a permission by name and description.

        Args:
            name (str): The name of the permission.
            desc (Optional[str]): The description of the permission.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_permission(name: str, desc: Optional[str], parent: Permission) -> Permission:
        """Register a permission by name, description, and parent permission.

        Args:
            name (str): The name of the permission.
            desc (Optional[str]): The description of the permission.
            parent (Permission): The parent permission.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_permission(name: str, desc: Optional[str], def_: Optional[PermissionDefault]) -> Permission:
        """Register a permission by name, description, and default value.

        Args:
            name (str): The name of the permission.
            desc (Optional[str]): The description of the permission.
            def_ (Optional[PermissionDefault]): The default value of the permission.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_permission(name: str, desc: Optional[str], def_: Optional[PermissionDefault], parent: Permission) -> Permission:
        """Register a permission by name, description, default value, and parent permission.

        Args:
            name (str): The name of the permission.
            desc (Optional[str]): The description of the permission.
            def_ (Optional[PermissionDefault]): The default value of the permission.
            parent (Permission): The parent permission.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_permission(name: str, desc: Optional[str], def_: Optional[PermissionDefault], children: Optional[Dict[str, bool]]) -> Permission:
        """Register a permission by name, description, default value, and children.

        Args:
            name (str): The name of the permission.
            desc (Optional[str]): The description of the permission.
            def_ (Optional[PermissionDefault]): The default value of the permission.
            children (Optional[Dict[str, bool]]): The children permissions.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_permission(name: str, desc: Optional[str], def_: Optional[PermissionDefault], children: Optional[Dict[str, bool]], parent: Permission) -> Permission:
        """Register a permission by name, description, default value, children, and parent permission.

        Args:
            name (str): The name of the permission.
            desc (Optional[str]): The description of the permission.
            def_ (Optional[PermissionDefault]): The default value of the permission.
            children (Optional[Dict[str, bool]]): The children permissions.
            parent (Permission): The parent permission.

        Returns:
            Permission: The registered permission.
        """
        ...

    @staticmethod
    def register_core_permissions() -> None:
        """Register core permissions for CraftBukkit utilities and commands."""
        ...