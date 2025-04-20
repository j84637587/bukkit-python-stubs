from typing import Optional
from uuid import UUID

class AnimalTamer:
    """
    This is the interface for AnimalTamer.
    """

    def get_name(self) -> Optional[str]:
        """
        This is the name of the specified AnimalTamer.

        Returns:
            The name to reference on tamed animals or None if a name cannot be obtained.
        """
        ...

    def get_unique_id(self) -> UUID:
        """
        This is the UUID of the specified AnimalTamer.

        Returns:
            The UUID to reference on tamed animals.
        """
        ...