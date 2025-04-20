from org.bukkit.entity import Golem

class Snowman(Golem):
    """
    Represents a snowman entity
    """

    def is_derp(self) -> bool:
        """
        Gets whether this snowman is in "derp mode", meaning it is not wearing a
        pumpkin.

        :return: True if the snowman is bald, false if it is wearing a pumpkin
        """
        ...

    def set_derp(self, derp_mode: bool) -> None:
        """
        Sets whether this snowman is in "derp mode", meaning it is not wearing a
        pumpkin. NOTE: This value is not persisted to disk and will therefore
        reset when the chunk is reloaded.

        :param derp_mode: True to remove the pumpkin, false to add a pumpkin
        """
        ...