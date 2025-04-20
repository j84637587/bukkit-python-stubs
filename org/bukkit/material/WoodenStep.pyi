from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import Wood

class WoodenStep(Wood):
    """
    Represents the different types of wooden steps.

    @see Material.LEGACY_WOOD_STEP

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """
    
    DEFAULT_TYPE: Material = Material.LEGACY_WOOD_STEP
    DEFAULT_INVERTED: bool = False

    def __init__(self) -> None:
        """
        Constructs a wooden step.
        """
        ...

    def __init__(self, species: TreeSpecies) -> None:
        """
        Constructs a wooden step of the given tree species.

        @param species the species of the wooden step
        """
        ...

    def __init__(self, species: TreeSpecies, inv: bool) -> None:
        """
        Constructs a wooden step of the given type and tree species, either
        inverted or not.

        @param species the species of the wooden step
        @param inv true the step is at the top of the block
        """
        ...

    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None:
        """
        @param type the type
        @param data the raw data value
        @deprecated Magic value
        """
        ...

    def is_inverted(self) -> bool:
        """
        Test if step is inverted

        @return true if inverted (top half), false if normal (bottom half)
        """
        ...

    def set_inverted(self, inv: bool) -> None:
        """
        Set step inverted state

        @param inv - true if step is inverted (top half), false if step is normal
        (bottom half)
        """
        ...

    def clone(self) -> 'WoodenStep':
        ...
    
    def __str__(self) -> str:
        ...