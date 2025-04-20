from org.bukkit.event.inventory import InventoryInteractEvent
from org.bukkit.event import HandlerList
from org.bukkit.inventory import Merchant
from org.bukkit.inventory import MerchantInventory
from org.bukkit.inventory.view import MerchantView
from typing import Any

class TradeSelectEvent(InventoryInteractEvent):
    """
    This event is called whenever a player clicks a new trade on the trades
    sidebar.
    <p>
    This event allows the user to get the index of the trade, letting them get
    the MerchantRecipe via the Merchant.
    """

    handlers: HandlerList = HandlerList()
    index: int

    def __init__(self, transaction: MerchantView, newIndex: int) -> None:
        """
        Initialize the TradeSelectEvent.

        :param transaction: The MerchantView transaction
        :param newIndex: The index of the new trade
        """
        super().__init__(transaction)
        self.index = newIndex

    def getIndex(self) -> int:
        """
        Used to get the index of the trade the player clicked on.

        :return: The index of the trade clicked by the player
        """
        return self.index

    def getInventory(self) -> MerchantInventory:
        """
        Override to get the MerchantInventory.

        :return: The MerchantInventory
        """
        return super().getInventory()  # type: ignore

    def getMerchant(self) -> Merchant:
        """
        Get the Merchant involved.

        :return: the Merchant
        """
        return self.getInventory().getMerchant()

    def getView(self) -> MerchantView:
        """
        Override to get the MerchantView.

        :return: The MerchantView
        """
        return super().getView()  # type: ignore

    def getHandlers(self) -> HandlerList:
        """
        Get the HandlerList for this event.

        :return: The HandlerList
        """
        return self.handlers

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Get the static HandlerList.

        :return: The static HandlerList
        """
        return TradeSelectEvent.handlers