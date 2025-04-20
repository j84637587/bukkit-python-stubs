from org.bukkit.block.data import BlockData
from typing import Literal

class TrialSpawner(BlockData):
    """
    'trial_spawner_state' indicates the current operational phase of the spawner.
    <br>
    'ominous' indicates if the block has ominous effects.
    """

    def get_trial_spawner_state(self) -> 'TrialSpawner.State':
        """
        Gets the value of the 'trial_spawner_state' property.

        @return: the 'trial_spawner_state' value
        """
        ...

    def set_trial_spawner_state(self, state: 'TrialSpawner.State') -> None:
        """
        Sets the value of the 'trial_spawner_state' property.

        @param state: the new 'trial_spawner_state' value
        """
        ...

    def is_ominous(self) -> bool:
        """
        Gets the value of the 'ominous' property.

        @return: the 'ominous' value
        """
        ...

    def set_ominous(self, ominous: bool) -> None:
        """
        Sets the value of the 'ominous' property.

        @param ominous: the new 'ominous' value
        """
        ...

    class State:
        """
        Enum representing the states of the TrialSpawner.
        """
        INACTIVE: Literal['INACTIVE']
        WAITING_FOR_PLAYERS: Literal['WAITING_FOR_PLAYERS']
        ACTIVE: Literal['ACTIVE']
        WAITING_FOR_REWARD_EJECTION: Literal['WAITING_FOR_REWARD_EJECTION']
        EJECTING_REWARD: Literal['EJECTING_REWARD']
        COOLDOWN: Literal['COOLDOWN']