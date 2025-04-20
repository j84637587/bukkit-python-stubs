from typing import List, Map, Optional, Set, Union
from org.bukkit import Bukkit
from org.bukkit.plugin import PluginManager
from org.jetbrains.annotations import NotNull, Nullable

class Permission:
    DEFAULT_PERMISSION: 'PermissionDefault'

    def __init__(self: 'Permission', name: str, description: Optional[str] = None, defaultValue: Optional['PermissionDefault'] = None, children: Optional[Map[str, bool]] = None) -> None:
        """
        Initializes a new Permission instance.

        :param name: The name of the permission.
        :param description: An optional description of the permission.
        :param defaultValue: An optional default value for the permission.
        :param children: An optional map of child permissions.
        """
        ...

        def getName(self: 'Permission') -> str:
        """
        Returns the unique fully qualified name of this Permission.

        :return: Fully qualified name.
        """
        ...

        def getChildren(self: 'Permission') -> Map[str, bool]:
        """
        Gets the children of this permission.

        :return: Permission children.
        """
        ...

        def getDefault(self: 'Permission') -> 'PermissionDefault':
        """
        Gets the default value of this permission.

        :return: Default value of this permission.
        """
        ...

    def setDefault(self: 'Permission', value: 'PermissionDefault') -> None:
        """
        Sets the default value of this permission.

        :param value: The new default to set.
        """
        ...

        def getDescription(self: 'Permission') -> str:
        """
        Gets a brief description of this permission, may be empty.

        :return: Brief description of this permission.
        """
        ...

    def setDescription(self: 'Permission', value: Optional[str]) -> None:
        """
        Sets the description of this permission.

        :param value: The new description to set.
        """
        ...

        def getPermissibles(self: 'Permission') -> Set['Permissible']:
        """
        Gets a set containing every Permissible that has this permission.

        :return: Set containing permissibles with this permission.
        """
        ...

    def recalculatePermissibles(self: 'Permission') -> None:
        """
        Recalculates all Permissibles that contain this permission.
        """
        ...

        def addParent(self: 'Permission', name: str, value: bool) -> 'Permission':
        """
        Adds this permission to the specified parent permission.

        :param name: Name of the parent permission.
        :param value: The value to set this permission to.
        :return: Parent permission it created or loaded.
        """
        ...

    def addParent(self: 'Permission', perm: 'Permission', value: bool) -> None:
        """
        Adds this permission to the specified parent permission.

        :param perm: Parent permission to register with.
        :param value: The value to set this permission to.
        """
        ...

        @staticmethod
    def loadPermissions(data: Map[Union[str, object], object], error: str, def_: Optional['PermissionDefault']) -> List['Permission']:
        """
        Loads a list of Permissions from a map of data.

        :param data: Map of permissions.
        :param error: An error message to show if a permission is invalid.
        :param def_: Default permission value to use if missing.
        :return: List of Permission objects.
        """
        ...

        @staticmethod
    def loadPermission(name: str, data: Map[str, object]) -> 'Permission':
        """
        Loads a Permission from a map of data.

        :param name: Name of the permission.
        :param data: Map of keys.
        :return: Permission object.
        """
        ...

        @staticmethod
    def loadPermission(name: str, data: Map[Union[str, object], object], def_: Optional['PermissionDefault'], output: Optional[List['Permission']]) -> 'Permission':
        """
        Loads a Permission from a map of data.

        :param name: Name of the permission.
        :param data: Map of keys.
        :param def_: Default permission value to use if not set.
        :param output: A list to append any created child-Permissions to, may be null.
        :return: Permission object.
        """
        ...

        @staticmethod
    def extractChildren(input: Map[Union[str, object], object], name: str, def_: Optional['PermissionDefault'], output: Optional[List['Permission']]) -> Map[str, bool]:
        """
        Extracts children permissions from the input map.

        :param input: Input map containing children permissions.
        :param name: Name of the parent permission.
        :param def_: Default permission value to use if missing.
        :param output: A list to append any created child-Permissions to, may be null.
        :return: Map of child permissions.
        """
        ...