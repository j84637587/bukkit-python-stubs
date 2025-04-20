from typing import Collection, Optional
from org.bukkit import NamespacedKey, Sound, Tag, EntityType
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

"""
Represents a component which can turn any item into equippable armor.
"""
class EquippableComponent(ConfigurationSerializable):

        def get_slot(self) -> EquipmentSlot:
        """Gets the slot the item can be equipped to.

        Returns:
            EquipmentSlot: slot
        """
        ...

    def set_slot(self, slot: EquipmentSlot) -> None:
        """Sets the slot the item can be equipped to.

        Args:
            slot (EquipmentSlot): new slot
        """
        ...

        def get_equip_sound(self) -> Optional[Sound]:
        """Gets the sound to play when the item is equipped.

        Returns:
            Optional[Sound]: the sound
        """
        ...

    def set_equip_sound(self, sound: Optional[Sound]) -> None:
        """Sets the sound to play when the item is equipped.

        Args:
            sound (Optional[Sound]): sound or null for current default
        """
        ...

        def get_model(self) -> Optional[NamespacedKey]:
        """Gets the key of the model to use when equipped.

        Returns:
            Optional[NamespacedKey]: model key
        """
        ...

    def set_model(self, key: Optional[NamespacedKey]) -> None:
        """Sets the key of the model to use when equipped.

        Args:
            key (Optional[NamespacedKey]): model key
        """
        ...

        def get_camera_overlay(self) -> Optional[NamespacedKey]:
        """Gets the key of the camera overlay to use when equipped.

        Returns:
            Optional[NamespacedKey]: camera overlay key
        """
        ...

    def set_camera_overlay(self, key: Optional[NamespacedKey]) -> None:
        """Sets the key of the camera overlay to use when equipped.

        Args:
            key (Optional[NamespacedKey]): camera overlay key
        """
        ...

        def get_allowed_entities(self) -> Optional[Collection[EntityType]]:
        """Gets the entities which can equip this item.

        Returns:
            Optional[Collection[EntityType]]: the entities
        """
        ...

    def set_allowed_entities(self, entities: Optional[EntityType]) -> None:
        """Sets the entities which can equip this item.

        Args:
            entities (Optional[EntityType]): the entity types
        """
        ...

    def set_allowed_entities(self, entities: Optional[Collection[EntityType]]) -> None:
        """Sets the entities which can equip this item.

        Args:
            entities (Optional[Collection[EntityType]]): the entity types
        """
        ...

    def set_allowed_entities(self, tag: Optional[Tag[EntityType]]) -> None:
        """Set the entity types (represented as an entity Tag) which can equip this item.

        Args:
            tag (Optional[Tag[EntityType]]): the entity tag

        Raises:
            IllegalArgumentException: if the passed tag is not an entity tag
        """
        ...

    def is_dispensable(self) -> bool:
        """Gets whether the item can be equipped by a dispenser.

        Returns:
            bool: equippable status
        """
        ...

    def set_dispensable(self, dispensable: bool) -> None:
        """Sets whether the item can be equipped by a dispenser.

        Args:
            dispensable (bool): new equippable status
        """
        ...

    def is_swappable(self) -> bool:
        """Gets if the item is swappable by right clicking.

        Returns:
            bool: swappable status
        """
        ...

    def set_swappable(self, swappable: bool) -> None:
        """Sets if the item is swappable by right clicking.

        Args:
            swappable (bool): new status
        """
        ...

    def is_damage_on_hurt(self) -> bool:
        """Gets if the item will be damaged when the wearing entity is damaged.

        Returns:
            bool: whether the item will be damaged
        """
        ...

    def set_damage_on_hurt(self, damage: bool) -> None:
        """Sets if the item will be damaged when the wearing entity is damaged.

        Args:
            damage (bool): whether the item will be damaged
        """
        ...

    def is_equip_on_interact(self) -> bool:
        """Gets if the item will be equipped on interact.

        Returns:
            bool: whether the item will be equipped
        """
        ...

    def set_equip_on_interact(self, equip: bool) -> None:
        """Sets if the item will be equipped on interact.

        Args:
            equip (bool): whether the item will be equipped
        """
        ...