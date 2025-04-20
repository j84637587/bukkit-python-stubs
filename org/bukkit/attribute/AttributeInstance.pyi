from typing import Collection
from org.bukkit.attribute import Attribute
from org.bukkit.attribute import AttributeModifier

class AttributeInstance:
    """
    Represents a mutable instance of an attribute and its associated modifiers
    and values.
    """

    def get_attribute(self) -> Attribute:
        """
        The attribute pertaining to this instance.

        @return: the attribute
        """
        ...

    def get_base_value(self) -> float:
        """
        Base value of this instance before modifiers are applied.

        @return: base value
        """
        ...

    def set_base_value(self, value: float) -> None:
        """
        Set the base value of this instance.

        @param value: new base value
        """
        ...

    def get_modifiers(self) -> Collection[AttributeModifier]:
        """
        Get all modifiers present on this instance.

        @return: a copied collection of all modifiers
        """
        ...

    def add_modifier(self, modifier: AttributeModifier) -> None:
        """
        Add a modifier to this instance.

        @param modifier: to add
        """
        ...

    def remove_modifier(self, modifier: AttributeModifier) -> None:
        """
        Remove a modifier from this instance.

        @param modifier: to remove
        """
        ...

    def get_value(self) -> float:
        """
        Get the value of this instance after all associated modifiers have been
        applied.

        @return: the total attribute value
        """
        ...

    def get_default_value(self) -> float:
        """
        Gets the default value of the Attribute attached to this instance.

        @return: server default value
        """
        ...
