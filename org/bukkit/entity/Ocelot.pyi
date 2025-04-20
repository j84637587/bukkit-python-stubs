from typing import Optional, Type as TypingType

class Ocelot(Animals):
    """
    A wild tameable cat
    """

    def is_trusting(self) -> bool:
        """
        Checks if this ocelot trusts players.

        :return: true if it trusts players
        """
        ...

    def set_trusting(self, trust: bool) -> None:
        """
        Sets if this ocelot trusts players.

        :param trust: true if it trusts players
        """
        ...

    @Deprecated(since="1.19.4")
    def get_cat_type(self) -> 'Ocelot.Type':
        """
        Gets the current type of this cat.

        :return: Type of the cat.
        :deprecated: Cats are now a separate entity.
        """
        ...

    @Deprecated(since="1.19.4")
    def set_cat_type(self, type: 'Ocelot.Type') -> None:
        """
        Sets the current type of this cat.

        :param type: New type of this cat.
        :deprecated: Cats are now a separate entity.
        """
        ...


    class Type:
        """
        Represents the various different cat types there are.
        :deprecated: Cats are now a separate entity.
        """
        WILD_OCELOT = 0
        BLACK_CAT = 1
        RED_CAT = 2
        SIAMESE_CAT = 3

        @staticmethod
        @Deprecated(since="1.6.2")
        def get_id() -> int:
            """
            Gets the ID of this cat type.

            :return: Type ID.
            :deprecated: Magic value
            """
            ...

        @staticmethod
        @Deprecated(since="1.6.2")
        def get_type(id: int) -> Optional['Ocelot.Type']:
            """
            Gets a cat type by its ID.

            :param id: ID of the cat type to get.
            :return: Resulting type, or None if not found.
            :deprecated: Magic value
            """
            ...