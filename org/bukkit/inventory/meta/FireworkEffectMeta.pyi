from org.bukkit import FireworkEffect
from org.bukkit.inventory.meta import ItemMeta
from typing import Optional

class FireworkEffectMeta(ItemMeta):
    """
    Represents a meta that can store a single FireworkEffect. An example
    includes {@link Material#FIREWORK_STAR}.
    """

    def set_effect(self, effect: Optional[FireworkEffect]) -> None:
        """
        Sets the firework effect for this meta.

        :param effect: the effect to set, or None to indicate none.
        """
        ...

    def has_effect(self) -> bool:
        """
        Checks if this meta has an effect.

        :return: true if this meta has an effect, false otherwise
        """
        ...

    def get_effect(self) -> Optional[FireworkEffect]:
        """
        Gets the firework effect for this meta.

        :return: the current effect, or None if none
        """
        ...

    def clone(self) -> 'FireworkEffectMeta':
        ...