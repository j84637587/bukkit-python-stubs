from typing import Any
from org.bukkit.potion import PotionType

class PotionData:
    """
    @deprecated Upgraded / extended potions are now their own {@link PotionType} use them instead.
    """
    
    def __init__(self, type: PotionType, extended: bool, upgraded: bool) -> None:
        """
        Instantiates a final PotionData object to contain information about a
        Potion

        :param type: the type of the Potion
        :param extended: whether the potion is extended PotionType#isExtendable() must be true
        :param upgraded: whether the potion is upgraded PotionType#isUpgradable() must be true
        """
        ...

    def __init__(self, type: PotionType) -> None:
        """
        Instantiates a final PotionData object to contain information about a
        Potion

        :param type: the type of the Potion
        """
        ...

    def get_type(self) -> PotionType:
        """
        Gets the type of the potion, Type matches up with each kind of craftable
        potion

        :return: the potion type
        """
        ...

    def is_upgraded(self) -> bool:
        """
        Checks if the potion is in an upgraded state. This refers to whether or
        not the potion is Tier 2, such as Potion of Fire Resistance II.

        :return: true if the potion is upgraded;
        """
        ...

    def is_extended(self) -> bool:
        """
        Checks if the potion is in an extended state. This refers to the extended
        duration potions

        :return: true if the potion is extended
        """
        ...

    def __hash__(self) -> int:
        ...
    
    def __eq__(self, obj: Any) -> bool:
        ...