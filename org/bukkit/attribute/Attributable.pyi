from typing import Optional

from org.bukkit.attribute import Attribute, AttributeInstance

class Attributable:
    """
    Represents an object which may contain attributes.
    """

    def get_attribute(self, attribute: Attribute) -> Optional[AttributeInstance]:
        """
        Gets the specified attribute instance from the object. This instance will
        be backed directly to the object and any changes will be visible at once.

        :param attribute: the attribute to get
        :return: the attribute instance or None if not applicable to this object
        """
        ...
