from org.bukkit.entity import Entity

class ExperienceOrb(Entity):
    """
    Represents an Experience Orb.
    """

    def get_experience(self) -> int:
        """
        Gets how much experience is contained within this orb

        :return: Amount of experience
        """
        ...

    def set_experience(self, value: int) -> None:
        """
        Sets how much experience is contained within this orb

        :param value: Amount of experience
        """
        ...