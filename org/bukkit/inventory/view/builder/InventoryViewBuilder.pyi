from org.bukkit.entity import HumanEntity
from org.bukkit.inventory import InventoryView
from org.jetbrains.annotations import ApiStatus, NotNull
from typing import TypeVar, Generic

V = TypeVar("V", bound=InventoryView)

class InventoryViewBuilder(Generic[V]):
    """
    Generic Builder for InventoryView's with no special attributes or parameters

    @param <V> the type of InventoryView created from this builder
    """

    def copy(self) -> InventoryViewBuilder[V]:
        """
        Makes a copy of this builder

        @return a copy of this builder
        """
        ...

    def title(self, title: str) -> InventoryViewBuilder[V]:
        """
        Sets the title of the builder

        @param title the title
        @return this builder
        """
        ...

    def build(self, player: HumanEntity) -> V:
        """
        Builds this builder into a InventoryView

        @param player the player to assign to the view
        @return the created InventoryView
        """
        ...
