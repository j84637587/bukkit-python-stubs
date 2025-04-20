from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

"""
Called when a vault in a trial chamber is about to display an item.
"""
class VaultDisplayItemEvent(BlockEvent, Cancellable):

    handlers: HandlerList = HandlerList()
    cancelled: bool
    display_item: ItemStack

    def __init__(self, the_block: Block, display_item: Nullable[ItemStack]) -> None:
        ...

    """
    Gets the item that will be displayed inside the vault.

    @return: the item to be displayed
    """
    def get_display_item(self) -> Nullable[ItemStack]:
        ...

    """
    Sets the item that will be displayed inside the vault.

    @param display_item: the item to be displayed
    """
    def set_display_item(self, display_item: Nullable[ItemStack]) -> None:
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancelled: bool) -> None:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...