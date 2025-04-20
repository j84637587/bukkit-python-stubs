from typing import Optional, TypeVar, Dict, Any
from collections import defaultdict

# Type variables
B = TypeVar('B')
T = TypeVar('T')

class UnsafeValues:
    """
    This interface provides value conversions that may be specific to a
    runtime, or have arbitrary meaning (read: magic values).
    Their existence and behavior is not guaranteed across future versions. They
    may be poorly named, throw exceptions, have misleading parameters, or any
    other bad programming practice.
    """

    def to_legacy(self, material: 'Material') -> 'Material':
        ...

    def from_legacy(self, material: 'Material') -> 'Material':
        ...

    def from_legacy(self, material: 'MaterialData') -> 'Material':
        ...

    def from_legacy(self, material: 'MaterialData', item_priority: bool) -> 'Material':
        ...

    def from_legacy(self, material: 'Material', data: bytes) -> 'BlockData':
        ...

    def get_material(self, material: str, version: int) -> 'Material':
        ...

    def get_data_version(self) -> int:
        ...

    def modify_item_stack(self, stack: 'ItemStack', arguments: str) -> 'ItemStack':
        ...

    def check_supported(self, pdf: 'PluginDescriptionFile') -> None:
        ...

    def process_class(self, pdf: 'PluginDescriptionFile', path: str, clazz: bytes) -> bytes:
        ...

    def load_advancement(self, key: 'NamespacedKey', advancement: str) -> Optional['Advancement']:
        """
        Load an advancement represented by the specified string into the server.
        The advancement format is governed by Minecraft and has no specified
        layout.
        Loaded advancements will be stored and persisted across server restarts
        and reloads.
        Callers should be prepared for Exception to be thrown.

        :param key: the unique advancement key
        :param advancement: representation of the advancement
        :return: the loaded advancement or null if an error occurred
        """
        ...

    def remove_advancement(self, key: 'NamespacedKey') -> bool:
        """
        Delete an advancement which was loaded and saved by
        load_advancement.
        This method will only remove advancement from persistent storage. It
        should be accompanied by a call to Server.reload_data in order
        to fully remove it from the running instance.

        :param key: the unique advancement key
        :return: true if a file matching this key was found and deleted
        """
        ...

    def get_default_attribute_modifiers(self, material: 'Material', slot: 'EquipmentSlot') -> 'Multimap[Attribute, AttributeModifier]':
        ...

    def get_creative_category(self, material: 'Material') -> 'CreativeCategory':
        ...

    def get_block_translation_key(self, material: 'Material') -> str:
        ...

    def get_item_translation_key(self, material: 'Material') -> str:
        ...

    def get_translation_key(self, entity_type: 'EntityType') -> str:
        ...

    def get_translation_key(self, item_stack: 'ItemStack') -> str:
        ...

    def get_translation_key(self, attribute: 'Attribute') -> str:
        ...

    def get_feature_flag(self, key: 'NamespacedKey') -> Optional['FeatureFlag']:
        ...

    def get_internal_potion_data(self, key: 'NamespacedKey') -> 'PotionType.InternalPotionData':
        """
        Do not use, method will get removed, and the plugin won't run

        :param key: of the potion type
        :return: an internal potion data
        """
        ...

    def get_damage_effect(self, key: str) -> Optional['DamageEffect']:
        ...

    def create_damage_source_builder(self, damage_type: 'DamageType') -> 'DamageSource.Builder':
        """
        Create a new DamageSource.Builder.

        :param damage_type: the DamageType to use
        :return: a DamageSource.Builder
        """
        ...

    def get(self, a_class: type, value: str) -> str:
        ...

    def get(self, registry: 'Registry[B]', key: 'NamespacedKey') -> Optional[B]:
        ...

    def get_custom_biome(self) -> 'Biome':
        ...

    def create_reputation_type(self, key: str) -> 'Villager.ReputationType':
        ...

    def create_reputation_event(self, key: str) -> 'Villager.ReputationEvent':
        ...