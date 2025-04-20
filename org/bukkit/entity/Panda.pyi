from typing import Protocol, Literal

class Gene(Protocol):
    """
    Gene enumeration for Panda.
    """
    NORMAL: Literal[False]
    LAZY: Literal[False]
    WORRIED: Literal[False]
    PLAYFUL: Literal[False]
    BROWN: Literal[True]
    WEAK: Literal[True]
    AGGRESSIVE: Literal[False]

    def is_recessive(self) -> bool:
        """
        Gets whether this gene is recessive, i.e. required in both parents to
        propagate to children.

        :return: recessive status
        """

class Panda(Protocol):
    """
    Panda entity.
    """

    def get_main_gene(self) -> Gene:
        """
        Gets this Panda's main gene.

        :return: main gene
        """

    def set_main_gene(self, gene: Gene) -> None:
        """
        Sets this Panda's main gene.

        :param gene: main gene
        """

    def get_hidden_gene(self) -> Gene:
        """
        Gets this Panda's hidden gene.

        :return: hidden gene
        """

    def set_hidden_gene(self, gene: Gene) -> None:
        """
        Sets this Panda's hidden gene.

        :param gene: hidden gene
        """

    def is_rolling(self) -> bool:
        """
        Gets whether the Panda is rolling.

        :return: Whether the Panda is rolling
        """

    def set_rolling(self, flag: bool) -> None:
        """
        Sets whether the Panda is rolling.

        :param flag: Whether the Panda is rolling
        """

    def is_sneezing(self) -> bool:
        """
        Gets whether the Panda is sneezing.

        :return: Whether the Panda is sneezing
        """

    def set_sneezing(self, flag: bool) -> None:
        """
        Sets whether the Panda is sneezing.

        :param flag: Whether the Panda is sneezing
        """

    def is_on_back(self) -> bool:
        """
        Gets whether the Panda is on its back.

        :return: Whether the Panda is on its back
        """

    def set_on_back(self, flag: bool) -> None:
        """
        Sets whether the Panda is on its back.

        :param flag: Whether the Panda is on its back
        """

    def is_eating(self) -> bool:
        """
        Gets whether the Panda is eating.

        :return: Whether the Panda is eating
        """

    def set_eating(self, flag: bool) -> None:
        """
        Sets the Panda's eating status. The panda must be holding food for this to work.

        :param flag: Whether the Panda is eating
        """

    def is_scared(self) -> bool:
        """
        Gets whether the Panda is scared.

        :return: Whether the Panda is scared
        """

    def get_unhappy_ticks(self) -> int:
        """
        Gets how many ticks the panda will be unhappy for.

        :return: The number of ticks the panda will be unhappy for
        """