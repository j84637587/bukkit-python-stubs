from typing import Protocol

class Creature(Protocol):
    pass

class Ageable(Creature, Protocol):
    """
    Represents an entity that can age.
    """

    def get_age(self) -> int:
        """
        Gets the age of this mob.

        @return Age
        """
        ...

    def set_age(self, age: int) -> None:
        """
        Sets the age of this mob.

        @param age New age
        """
        ...

    def set_age_lock(self, lock: bool) -> None:
        """
        Lock the age of the animal, setting this will prevent the animal from
        maturing or getting ready for mating.

        @param lock new lock
        @deprecated see {@link Breedable#setAgeLock(boolean)}
        """
        ...

    def get_age_lock(self) -> bool:
        """
        Gets the current agelock.

        @return the current agelock
        @deprecated see {@link Breedable#getAgeLock()}
        """
        ...

    def set_baby(self) -> None:
        """
        Sets the age of the mob to a baby
        """
        ...

    def set_adult(self) -> None:
        """
        Sets the age of the mob to an adult
        """
        ...

    def is_adult(self) -> bool:
        """
        Returns true if the mob is an adult.

        @return return true if the mob is an adult
        """
        ...

    def can_breed(self) -> bool:
        """
        Return the ability to breed of the animal.

        @return the ability to breed of the animal
        @deprecated see {@link Breedable#canBreed()}
        """
        ...

    def set_breed(self, breed: bool) -> None:
        """
        Set breedability of the animal, if the animal is a baby and set to
        breed it will instantly grow up.

        @param breed breedability of the animal
        @deprecated see {@link Breedable#setBreed(boolean)}
        """
        ...