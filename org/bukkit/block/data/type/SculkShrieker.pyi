from org.bukkit.block.data import Waterlogged

class SculkShrieker(Waterlogged):
    """
    'can_summon' indicates whether the sculk shrieker can summon the warden.
    <p>
    'shrieking' indicated whether the sculk shrieker is shrieking or not.
    """

    def is_can_summon(self) -> bool:
        """
        Gets the value of the 'can_summon' property.

        @return: the 'can_summon' value
        """
        ...

    def set_can_summon(self, can_summon: bool) -> None:
        """
        Sets the value of the 'can_summon' property.

        @param can_summon: the new 'can_summon' value
        """
        ...

    def is_shrieking(self) -> bool:
        """
        Gets the value of the 'shrieking' property.

        @return: the 'shrieking' value
        """
        ...

    def set_shrieking(self, shrieking: bool) -> None:
        """
        Sets the value of the 'shrieking' property.

        @param shrieking: the new 'shrieking' value
        """
        ...