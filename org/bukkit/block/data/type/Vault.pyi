from org.bukkit.block.data import Directional
from typing import Literal

class Vault(Directional):
    """
    'vault_state' indicates the current operational phase of the vault block.
    <br>
    'ominous' indicates if the block has ominous effects.
    """

    def get_vault_state(self) -> 'State':
        """
        Gets the value of the 'vault_state' property.

        Returns:
            State: the 'vault_state' value
        """
        ...

    def get_trial_spawner_state(self) -> 'State':
        """
        Gets the value of the 'vault_state' property.

        Returns:
            State: the 'vault_state' value

        Deprecated:
            see get_vault_state()
        """
        ...

    def set_vault_state(self, state: 'State') -> None:
        """
        Sets the value of the 'vault_state' property.

        Args:
            state (State): the new 'vault_state' value
        """
        ...

    def set_trial_spawner_state(self, state: 'State') -> None:
        """
        Sets the value of the 'vault_state' property.

        Args:
            state (State): the new 'vault_state' value

        Deprecated:
            see set_vault_state(State)
        """
        ...

    def is_ominous(self) -> bool:
        """
        Gets the value of the 'ominous' property.

        Returns:
            bool: the 'ominous' value
        """
        ...

    def set_ominous(self, ominous: bool) -> None:
        """
        Sets the value of the 'ominous' property.

        Args:
            ominous (bool): the new 'ominous' value
        """
        ...

class State:
    """
    Enum for the vault state.
    """
    INACTIVE: Literal['INACTIVE'] = 'INACTIVE'
    ACTIVE: Literal['ACTIVE'] = 'ACTIVE'
    UNLOCKING: Literal['UNLOCKING'] = 'UNLOCKING'
    EJECTING: Literal['EJECTING'] = 'EJECTING'