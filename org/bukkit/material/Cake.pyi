from org.bukkit import Material
from org.bukkit.material import MaterialData
from typing import Any

"""
@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Cake(MaterialData):
    def __init__(self) -> None:
        super().__init__(Material.LEGACY_CAKE_BLOCK)

    def __init__(self, type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the number of slices eaten from this cake

    @return The number of slices eaten
    """
    def get_slices_eaten(self) -> int:
        return self.get_data()

    """
    Gets the number of slices remaining on this cake

    @return The number of slices remaining
    """
    def get_slices_remaining(self) -> int:
        return 6 - self.get_data()

    """
    Sets the number of slices eaten from this cake

    @param n The number of slices eaten
    """
    def set_slices_eaten(self, n: int) -> None:
        if n < 6:
            self.set_data(n.to_bytes(1, 'big'))

    """
    Sets the number of slices remaining on this cake

    @param n The number of slices remaining
    """
    def set_slices_remaining(self, n: int) -> None:
        if n > 6:
            n = 6
        self.set_data((6 - n).to_bytes(1, 'big'))

    def __str__(self) -> str:
        return super().__str__() + " " + str(self.get_slices_eaten()) + "/" + str(self.get_slices_remaining()) + " slices eaten/remaining"

    def clone(self) -> 'Cake':
        return super().clone()