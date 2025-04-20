from typing import Optional

class Nameable:
    """
    Represents a block, entity, or other object that may receive a custom name.
    """
    def getCustomName(self) -> Optional[str]:
        """
        Gets the custom name on a mob or block. If there is no name this method
        will return null.
        This value has no effect on players, they will always use their real
        name.
        
        :return: name of the mob/block or null
        """
        ...

    def setCustomName(self, name: Optional[str]) -> None:
        """
        Sets a custom name on a mob or block. This name will be used in death
        messages and can be sent to the client as a nameplate over the mob.
        Setting the name to null or an empty string will clear it.
        This value has no effect on players, they will always use their real
        name.
        
        :param name: the name to set
        """
        ...