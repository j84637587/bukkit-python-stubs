from typing import Dict, List, Optional

class PermissionDefault:
    TRUE: 'PermissionDefault'
    FALSE: 'PermissionDefault'
    OP: 'PermissionDefault'
    NOT_OP: 'PermissionDefault'

    names: List[str]
    lookup: Dict[str, 'PermissionDefault']

    def __init__(self, *names: str) -> None:
        """Initializes the PermissionDefault with the given names."""
        ...

    def get_value(self, op: bool) -> bool:
        """
        Calculates the value of this PermissionDefault for the given operator value.

        :param op: If the target is op
        :return: True if the default should be true, or false
        """
        ...

    @staticmethod
    def get_by_name(name: str) -> Optional['PermissionDefault']:
        """
        Looks up a PermissionDefault by name.

        :param name: Name of the default
        :return: Specified value, or None if not found
        """
        ...

    def __str__(self) -> str:
        """Returns the string representation of the PermissionDefault."""
        ...