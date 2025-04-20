from org.bukkit import Server
from org.bukkit.inventory import InventoryView, Merchant
from org.jetbrains.annotations import ApiStatus, NotNull

"""
An InventoryViewBuilder for creating merchant views

@param V: the type of InventoryView created by this builder
"""
class MerchantInventoryViewBuilder(V: InventoryView):

        def copy(self) -> 'MerchantInventoryViewBuilder[V]':
        ...

        def title(self, title: str) -> 'MerchantInventoryViewBuilder[V]':
        ...

    """
    Adds a merchant to this builder

    @param merchant: the merchant
    @return: this builder
    """
        def merchant(self, merchant: Merchant) -> 'MerchantInventoryViewBuilder[V]':
        ...

    """
    Determines whether or not the server should check if the player can reach
    the location.
    <p>
    Given checkReachable is provided and a virtual merchant is provided to
    the builder from {@link Server#createMerchant(String)} this method will
    have no effect on the actual menu status.

    @param checkReachable: whether or not to check if the view is "reachable"
    @return: this builder
    """
        def check_reachable(self, check_reachable: bool) -> 'MerchantInventoryViewBuilder[V]':
        ...