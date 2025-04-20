from typing import Collection
from org.bukkit.inventory import ItemStack
from org.bukkit.potion import PotionEffect
from org.jetbrains.annotations import NotNull

"""
Represents a thrown potion bottle
"""
class ThrownPotion(ThrowableProjectile):

    """
    Returns the effects that are applied by this potion.

    @return The potion effects
    """
        def getEffects(self) -> Collection[PotionEffect]: ...

    """
    Returns a copy of the ItemStack for this thrown potion.
    <p>
    Altering this copy will not alter the thrown potion directly. If you want
    to alter the thrown potion, you must use the {@link
    #setItem(ItemStack) setItemStack} method.

    @return A copy of the ItemStack for this thrown potion.
    """
        def getItem(self) -> ItemStack: ...

    """
    Set the ItemStack for this thrown potion.
    <p>
    The ItemStack must be of type {@link org.bukkit.Material#SPLASH_POTION}
    or {@link org.bukkit.Material#LINGERING_POTION}, otherwise an exception
    is thrown.

    @param item New ItemStack
    """
    def setItem(self, item: ItemStack) -> None: ...