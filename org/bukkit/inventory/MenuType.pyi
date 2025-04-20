from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.entity import HumanEntity
from org.bukkit.inventory.view import AnvilView
from org.bukkit.inventory.view import BeaconView
from org.bukkit.inventory.view import BrewingStandView
from org.bukkit.inventory.view import CrafterView
from org.bukkit.inventory.view import EnchantmentView
from org.bukkit.inventory.view import FurnaceView
from org.bukkit.inventory.view import LecternView
from org.bukkit.inventory.view import LoomView
from org.bukkit.inventory.view import MerchantView
from org.bukkit.inventory.view import StonecutterView
from org.bukkit.inventory.view import InventoryViewBuilder
from org.bukkit.inventory.view import LocationInventoryViewBuilder
from org.bukkit.inventory.view import MerchantInventoryViewBuilder
from org.bukkit.registry import RegistryAware
from org.jetbrains.annotations import ApiStatus
from org.jetbrains.annotations import NotNull
from typing import TypeVar, Generic

V = TypeVar('V', bound='InventoryView')
B = TypeVar('B', bound='InventoryViewBuilder[V]')

class MenuType(Keyed, RegistryAware):
    """
    Represents different kinds of views, also known as menus, which can be
    created and viewed by the player.
    """

    GENERIC_9X1: 'MenuType.Typed[InventoryView, InventoryViewBuilder[InventoryView]]'
    GENERIC_9X2: 'MenuType.Typed[InventoryView, InventoryViewBuilder[InventoryView]]'
    GENERIC_9X3: 'MenuType.Typed[InventoryView, LocationInventoryViewBuilder[InventoryView]]'
    GENERIC_9X4: 'MenuType.Typed[InventoryView, InventoryViewBuilder[InventoryView]]'
    GENERIC_9X5: 'MenuType.Typed[InventoryView, InventoryViewBuilder[InventoryView]]'
    GENERIC_9X6: 'MenuType.Typed[InventoryView, InventoryViewBuilder[InventoryView]]'
    GENERIC_3X3: 'MenuType.Typed[InventoryView, LocationInventoryViewBuilder[InventoryView]]'
    CRAFTER_3X3: 'MenuType.Typed[CrafterView, LocationInventoryViewBuilder[CrafterView]]'
    ANVIL: 'MenuType.Typed[AnvilView, LocationInventoryViewBuilder[AnvilView]]'
    BEACON: 'MenuType.Typed[BeaconView, LocationInventoryViewBuilder[BeaconView]]'
    BLAST_FURNACE: 'MenuType.Typed[FurnaceView, LocationInventoryViewBuilder[FurnaceView]]'
    BREWING_STAND: 'MenuType.Typed[BrewingStandView, LocationInventoryViewBuilder[BrewingStandView]]'
    CRAFTING: 'MenuType.Typed[InventoryView, LocationInventoryViewBuilder[InventoryView]]'
    ENCHANTMENT: 'MenuType.Typed[EnchantmentView, LocationInventoryViewBuilder[EnchantmentView]]'
    FURNACE: 'MenuType.Typed[FurnaceView, LocationInventoryViewBuilder[FurnaceView]]'
    GRINDSTONE: 'MenuType.Typed[InventoryView, LocationInventoryViewBuilder[InventoryView]]'
    HOPPER: 'MenuType.Typed[InventoryView, LocationInventoryViewBuilder[InventoryView]]'
    LECTERN: 'MenuType.Typed[LecternView, LocationInventoryViewBuilder[LecternView]]'
    LOOM: 'MenuType.Typed[LoomView, LocationInventoryViewBuilder[LoomView]]'
    MERCHANT: 'MenuType.Typed[MerchantView, MerchantInventoryViewBuilder[MerchantView]]'
    SHULKER_BOX: 'MenuType.Typed[InventoryView, LocationInventoryViewBuilder[InventoryView]]'
    SMITHING: 'MenuType.Typed[InventoryView, LocationInventoryViewBuilder[InventoryView]]'
    SMOKER: 'MenuType.Typed[FurnaceView, LocationInventoryViewBuilder[FurnaceView]]'
    CARTOGRAPHY_TABLE: 'MenuType.Typed[InventoryView, LocationInventoryViewBuilder[InventoryView]]'
    STONECUTTER: 'MenuType.Typed[StonecutterView, LocationInventoryViewBuilder[StonecutterView]]'

    class Typed(Generic[V, B], MenuType):
        """
        Typed represents a subtype of MenuTypes that have a known
        InventoryView type at compile time.

        @param <V> the generic type of InventoryView that represents the
        view type.
        @param <B> the builder type of InventoryViewBuilder that
        represents the view builder.
        """

                def create(self, player: HumanEntity, title: str) -> V:
            """
            Creates a view of the specified menu type.
            The player provided to create this view must be the player the view
            is opened for. See HumanEntity#openInventory(InventoryView)
            for more information.

            @param player: the player the view belongs to
            @param title: the title of the view
            @return: the created InventoryView
            """
            ...

                def builder(self) -> B:
            """
            Creates a builder for this type of InventoryView.

            @return: the new builder
            """
            ...

        def typed(self) -> 'MenuType.Typed[InventoryView, InventoryViewBuilder[InventoryView]]':
        """
        Yields this MenuType as a typed version of itself with a plain
        InventoryView representing it.

        @return: the typed MenuType.
        """
        ...

        def typed(self, viewClass: type) -> 'MenuType.Typed[V, B]':
        """
        Yields this MenuType as a typed version of itself with a specific
        InventoryView representing it.

        @param viewClass: the class type of the InventoryView to type this
        InventoryView with.
        @param <V>: the generic type of the InventoryView to get this MenuType
        with
        @param <B>: the generic type of the InventoryViewBuilder to get this
        MenuType with
        @return: the typed MenuType
        @raises IllegalArgumentException: if the provided viewClass cannot be
        typed to this MenuType
        """
        ...

        def getInventoryViewClass(self) -> type:
        """
        Gets the InventoryView class of this MenuType.

        @return: the InventoryView class of this MenuType
        """
        ...

        @Deprecated(since="1.21.4")
    def getKey(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see: #getKeyOrThrow()
        @see: #isRegistered()
        """
        ...

    @staticmethod
        def get(key: str) -> 'MenuType':
        """
        @param key: the key to get the MenuType
        @return: the MenuType
        """
        ...