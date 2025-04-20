from org.bukkit import Material
from org.bukkit.inventory import ItemStack
from typing import Any

"""
Handles specific metadata for certain items or blocks

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class MaterialData:
    type: Material
    data: int

    def __init__(self: "MaterialData", type: Material) -> None:
        """
        :param type: the type
        """
        ...

    """
    @param type: the type
    @param data: the raw data value
    @deprecated Magic value
    """
    @deprecated(since="1.6.2")
    def __init__(self: "MaterialData", type: Material, data: int) -> None:
        ...

    """
    Gets the raw data in this material

    :return: Raw data
    @deprecated Magic value
    """
    @deprecated(since="1.6.2")
    def get_data(self: "MaterialData") -> int:
        ...

    """
    Sets the raw data of this material

    :param data: New raw data
    @deprecated Magic value
    """
    @deprecated(since="1.6.2")
    def set_data(self: "MaterialData", data: int) -> None:
        ...

    """
    Gets the Material that this MaterialData represents

    :return: Material represented by this MaterialData
    """
    def get_item_type(self: "MaterialData") -> Material:
        ...

    """
    Creates a new ItemStack based on this MaterialData

    :return: New ItemStack containing a copy of this MaterialData
    @deprecated this method creates an ItemStack of size 0 which is not
    generally useful. Consider {@link #toItemStack(int)}.
    """
    @deprecated(since="1.12")
    def to_item_stack(self: "MaterialData") -> ItemStack:
        ...

    """
    Creates a new ItemStack based on this MaterialData

    :param amount: The stack size of the new stack
    :return: New ItemStack containing a copy of this MaterialData
    """
    def to_item_stack(self: "MaterialData", amount: int) -> ItemStack:
        ...

    def __str__(self: "MaterialData") -> str:
        ...

    def __hash__(self: "MaterialData") -> int:
        ...

    def __eq__(self: "MaterialData", obj: Any) -> bool:
        ...

    def clone(self: "MaterialData") -> "MaterialData":
        ...