from org.bukkit.entity import Ageable

class Breedable(Ageable):
    """
    Represents an entity that can age and breed.
    """

    def set_age_lock(self, lock: bool) -> None:
        """
        Lock the age of the animal, setting this will prevent the animal from
        maturing or getting ready for mating.

        :param lock: new lock
        """
        ...

    def get_age_lock(self) -> bool:
        """
        Gets the current agelock.

        :return: the current agelock
        """
        ...

    def can_breed(self) -> bool:
        """
        Return the ability to breed of the animal.

        :return: the ability to breed of the animal
        """
        ...

    def set_breed(self, breed: bool) -> None:
        """
        Set breedability of the animal, if the animal is a baby and set to
        breed it will instantly grow up.

        :param breed: breedability of the animal
        """
        ...