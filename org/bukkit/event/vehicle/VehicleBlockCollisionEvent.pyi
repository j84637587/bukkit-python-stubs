from org.bukkit.block import Block
from org.bukkit.entity import Vehicle
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import VehicleCollisionEvent
from typing import Any

class VehicleBlockCollisionEvent(VehicleCollisionEvent):
    """
    Raised when a vehicle collides with a block.
    """

    handlers: HandlerList = HandlerList()
    block: Block

    def __init__(self, vehicle: Vehicle, block: Block) -> None:
        super().__init__(vehicle)
        self.block = block

    """
    Gets the block the vehicle collided with

    @return: the block the vehicle collided with
    """
    def getBlock(self) -> Block:
        ...

    @Override
    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...