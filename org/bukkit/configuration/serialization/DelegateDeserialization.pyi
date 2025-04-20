from typing import Type
from org.bukkit.configuration.serialization import ConfigurationSerializable

class DelegateDeserialization:
    """
    Applies to a :class:`ConfigurationSerializable` that will delegate all
    deserialization to another :class:`ConfigurationSerializable`.
    """

    def value(self) -> Type[ConfigurationSerializable]:
        """
        Which class should be used as a delegate for this class's
        deserialization.

        :return: Delegate class
        """
        ...