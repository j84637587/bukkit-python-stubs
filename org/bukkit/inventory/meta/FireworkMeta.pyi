from typing import List, Iterable
from org.bukkit import FireworkEffect
from org.bukkit.inventory.meta import ItemMeta

"""
Represents a {@link Material#FIREWORK_ROCKET} and its effects.
"""
class FireworkMeta(ItemMeta):

    """
    Add another effect to this firework.

    @param effect The firework effect to add
    @raises IllegalArgumentException If effect is null
    """
    def add_effect(self, effect: FireworkEffect) -> None:
        ...

    """
    Add several effects to this firework.

    @param effects The firework effects to add
    @raises IllegalArgumentException If effects is null
    @raises IllegalArgumentException If any effect is null (may be thrown
        after changes have occurred)
    """
    def add_effects(self, *effects: FireworkEffect) -> None:
        ...

    """
    Add several firework effects to this firework.

    @param effects An iterable object whose iterator yields the desired
        firework effects
    @raises IllegalArgumentException If effects is null
    @raises IllegalArgumentException If any effect is null (may be thrown
        after changes have occurred)
    """
    def add_effects_iterable(self, effects: Iterable[FireworkEffect]) -> None:
        ...

    """
    Get the effects in this firework.

    @return An immutable list of the firework effects
    """
    def get_effects(self) -> List[FireworkEffect]:
        ...

    """
    Get the number of effects in this firework.

    @return The number of effects
    """
    def get_effects_size(self) -> int:
        ...

    """
    Remove an effect from this firework.

    @param index The index of the effect to remove
    @raises IndexOutOfBoundsException If index {@literal < 0 or index >} {@link
        #getEffectsSize()}
    """
    def remove_effect(self, index: int) -> None:
        ...

    """
    Remove all effects from this firework.
    """
    def clear_effects(self) -> None:
        ...

    """
    Get whether this firework has any effects.

    @return true if it has effects, false if there are no effects
    """
    def has_effects(self) -> bool:
        ...

    """
    Get whether this firework has power set by component.

    @return true if it has power set, false if there are no power set
    """
    def has_power(self) -> bool:
        ...

    """
    Gets the approximate height the firework will fly.
    <br>
    Plugins should check that hasPower() returns <code>true</code>
    before calling this method.

    @return approximate flight height of the firework.
    @see #hasPower()
    """
    def get_power(self) -> int:
        ...

    """
    Sets the approximate power of the firework. Each level of power is half
    a second of flight time.

    @param power the power of the firework, from 0-255
    @raises IllegalArgumentException if {@literal power<0 or power>255}
    """
    def set_power(self, power: int) -> None:
        ...

    """
    @return a clone of this FireworkMeta
    """
    def clone(self) -> 'FireworkMeta':
        ...