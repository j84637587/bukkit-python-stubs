from org.bukkit.block.data import Orientable
from org.jetbrains.annotations import ApiStatus, NotNull
from typing import Literal

class CreakingHeart(Orientable):
    """
    'creaking_heart_state' indicates the current operational phase of the block.
    <br>
    'natural' is whether this is a naturally generated block.
    """

    def is_active(self) -> bool:
        """
        Gets the value of the 'active' property.

        :return: the 'active' value
        :deprecated: use {@link #get_creaking_heart_state()}
        """
        ...

    def set_active(self, active: bool) -> None:
        """
        Sets the value of the 'active' property.

        :param active: the new 'active' value
        :deprecated: use {@link #set_creaking_heart_state(org.bukkit.block.data.type.CreakingHeart.State)}
        """
        ...

    def is_natural(self) -> bool:
        """
        Gets the value of the 'natural' property.

        :return: the 'natural' value
        """
        ...

    def set_natural(self, natural: bool) -> None:
        """
        Sets the value of the 'natural' property.

        :param natural: the new 'natural' value
        """
        ...

        def get_creaking_heart_state(self) -> 'State':
        """
        Gets the value of the 'creaking_heart_state' property.

        :return: the 'creaking_heart_state' value
        """
        ...

    def set_creaking_heart_state(self, state: 'State') -> None:
        """
        Sets the value of the 'creaking_heart_state' property.

        :param state: the new 'creaking_heart_state' value
        """
        ...

class State:
    """
    Enum representing the state of the creaking heart.
    """
    UPROOTED: Literal['UPROOTED'] = 'UPROOTED'
    DORMANT: Literal['DORMANT'] = 'DORMANT'
    AWAKE: Literal['AWAKE'] = 'AWAKE'