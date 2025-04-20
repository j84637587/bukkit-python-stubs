from typing import Collection, Optional

class Advancement:
    pass

class AdvancementProgress:
    """
    The individual status of an advancement for a player. This class is not
    reference safe as the underlying advancement may be reloaded.
    """

    def get_advancement(self) -> Advancement:
        """
        The advancement this progress is concerning.

        :return: the relevant advancement
        """
        ...

    def is_done(self) -> bool:
        """
        Check if all criteria for this advancement have been met.

        :return: true if this advancement is done
        """
        ...

    def award_criteria(self, criteria: str) -> bool:
        """
        Mark the specified criteria as awarded at the current time.

        :param criteria: the criteria to mark
        :return: true if awarded, false if criteria does not exist or already awarded.
        """
        ...

    def revoke_criteria(self, criteria: str) -> bool:
        """
        Mark the specified criteria as uncompleted.

        :param criteria: the criteria to mark
        :return: true if removed, false if criteria does not exist or not awarded
        """
        ...

    def get_date_awarded(self, criteria: str) -> Optional[Date]:
        """
        Get the date the specified criteria was awarded.

        :param criteria: the criteria to check
        :return: date awarded or None if unawarded or criteria does not exist
        """
        ...

    def get_remaining_criteria(self) -> Collection[str]:
        """
        Get the criteria which have not been awarded.

        :return: unmodifiable copy of criteria remaining
        """
        ...

    def get_awarded_criteria(self) -> Collection[str]:
        """
        Gets the criteria which have been awarded.

        :return: unmodifiable copy of criteria awarded
        """
        ...