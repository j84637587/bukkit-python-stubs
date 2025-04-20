from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any

class PlayerRiptideEvent(PlayerEvent):
    """
    This event is fired when the player activates the riptide enchantment, using
    their trident to propel them through the air.
    <br>
    N.B. the riptide action is currently performed client side, so manipulating
    the player in this event may have undesired effects.
    """

    handlers: HandlerList = HandlerList()
    item: ItemStack
    velocity: Vector

    def __init__(self, who: Player, item: ItemStack, velocity: Vector) -> None:
        super().__init__(who)
        self.item = item
        self.velocity = velocity

    def __init__(self, who: Player, item: ItemStack) -> None:
        self.__init__(who, item, Vector())

    /**
     * Gets the item containing the used enchantment.
     *
     * @return held enchanted item
     */
    def getItem(self) -> ItemStack:
        return self.item

    /**
     * Get the velocity applied to the player as a result of this riptide.
     *
     * @return the riptide velocity
     */
    def getVelocity(self) -> Vector:
        return self.velocity.clone()

    def getHandlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def getHandlerList() -> HandlerList:
        return handlers