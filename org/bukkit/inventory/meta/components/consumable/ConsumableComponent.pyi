from typing import List, Optional
from org.bukkit import Sound
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory.meta.components.consumable.effects import ConsumableEffect
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

class ConsumableComponent(ConfigurationSerializable):
    """
    Represents a component which item can be consumed on use.
    """

    def get_consume_seconds(self) -> float:
        """
        Gets the time in seconds it will take for this item to be consumed.

        @return consume time
        """
        ...

    def set_consume_seconds(self, consume_seconds: float) -> None:
        """
        Sets the time in seconds it will take for this item to be consumed.

        @param consume_seconds new consume time
        """
        ...

        def get_animation(self) -> 'Animation':
        """
        Gets the animation used during consumption of the item.

        @return animation
        """
        ...

    def set_animation(self, animation: 'Animation') -> None:
        """
        Sets the animation used during consumption of the item.

        @param animation the new animation
        """
        ...

        def get_sound(self) -> Optional[Sound]:
        """
        Gets the sound to play during and on completion of the item's
        consumption.

        @return the sound
        """
        ...

    def set_sound(self, sound: Optional[Sound]) -> None:
        """
        Sets the sound to play during and on completion of the item's
        consumption.

        @param sound sound or null for current default
        """
        ...

    def has_consume_particles(self) -> bool:
        """
        Gets whether consumption particles are emitted while consuming this item.

        @return true for particles emitted while consuming, false otherwise
        """
        ...

    def set_consume_particles(self, consume_particles: bool) -> None:
        """
        Sets whether consumption particles are emitted while consuming this item.

        @param consume_particles if particles need to be emitted while consuming
        the item
        """
        ...

        def get_effects(self) -> List[ConsumableEffect]:
        """
        Gets the effects which may be applied by this item when consumed.

        @return consumable effects
        """
        ...

    def set_effects(self, effects: List[ConsumableEffect]) -> None:
        """
        Sets the effects which may be applied by this item when consumed.

        @param effects new effects
        """
        ...

        def add_effect(self, effect: ConsumableEffect) -> ConsumableEffect:
        """
        Adds an effect which may be applied by this item when consumed.

        @param effect the effect
        @return the added effect
        """
        ...

    class Animation:
        """
        Represents the animations for an item being consumed.
        """
        DRINK = ...
        EAT = ...
        NONE = ...
        BLOCK = ...
        BOW = ...
        BRUSH = ...
        CROSSBOW = ...
        SPEAR = ...
        SPYGLASS = ...
        TOOT_HORN = ...