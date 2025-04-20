from org.bukkit.entity import Entity
from org.bukkit.GameEvent import GameEvent
from org.bukkit.enchantments import Enchantment
from org.jetbrains.annotations import Nullable

"""
Represents an instance of a lightning strike. May or may not do damage.
"""
class LightningStrike(Entity):

    """
    Returns whether the strike is an effect that does no damage.

    @return whether the strike is an effect
    """
    def is_effect(self) -> bool: ...

    """
    Get the amount of flashes that will occur before the lightning is
    removed. By default this value is between 1 and 3.

    @return the flashes
    """
    def get_flashes(self) -> int: ...

    """
    Set the amount of flashes that will occur before the lightning is
    removed. One flash will occur after this lightning strike's life
    has reduced below 0.

    @param flashes the flashes
    """
    def set_flashes(self, flashes: int) -> None: ...

    """
    Get the amount of ticks this lightning strike will inflict damage
    upon its hit entities.
    <p>
    When life ticks are negative, there is a random chance that another
    flash will be initiated and life ticks reset to 1.

    @return the life ticks
    """
    def get_life_ticks(self) -> int: ...

    """
    Get the amount of ticks this lightning strike will inflict damage
    upon its hit entities.
    <p>
    When life ticks are negative, there is a random chance that another
    flash will be initiated and life ticks reset to 1. Additionally, if
    life ticks are set to 2 (the default value when a lightning strike
    has been spawned), a list of events will occur:
    <ul>
      <li>Impact sound effects will be played
      <li>Fire will be spawned (dependent on difficulty)
      <li>Lightning rods will be powered (if hit)
      <li>Copper will be stripped (if hit)
      <li>{@link GameEvent#LIGHTNING_STRIKE} will be dispatched
    </ul>

    @param ticks the life ticks
    """
    def set_life_ticks(self, ticks: int) -> None: ...

    """
    Get the {@link Player} that caused this lightning to strike. This
    will occur naturally if a trident enchanted with
    {@link Enchantment#CHANNELING Channeling} were thrown at an entity
    during a storm.

    @return the player
    """
        def get_causing_player(self) -> 'Player': ...

    """
    Set the {@link Player} that caused this lightning to strike.

    @param player the player
    """
    def set_causing_player(self, player: 'Player') -> None: ...