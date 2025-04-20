from typing import Any
from org.bukkit.inventory.meta.trim import TrimMaterial, TrimPattern

class ArmorTrim:
    """
    Represents an armor trim that may be applied to an item.

    @see ArmorMeta#setTrim(ArmorTrim)
    """

    def __init__(self, material: TrimMaterial, pattern: TrimPattern) -> None:
        """
        Create a new {@link ArmorTrim} given a {@link TrimMaterial} and
        {@link TrimPattern}.

        @param material the material
        @param pattern the pattern
        """
        ...

    def get_material(self) -> TrimMaterial:
        """
        Get the {@link TrimMaterial} for this armor trim.

        @return the material
        """
        ...

    def get_pattern(self) -> TrimPattern:
        """
        Get the {@link TrimPattern} for this armor trim.

        @return the pattern
        """
        ...

    def __hash__(self) -> int:
        ...
    
    def __eq__(self, obj: Any) -> bool:
        ...