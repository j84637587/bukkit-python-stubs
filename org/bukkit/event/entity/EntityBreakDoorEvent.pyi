from org.bukkit.Material import Material
from org.bukkit.block.Block import Block
from org.bukkit.entity.Entity import Entity
from org.bukkit.entity.LivingEntity import LivingEntity
from org.bukkit.event.entity.EntityChangeBlockEvent import EntityChangeBlockEvent
from typing import Any

class EntityBreakDoorEvent(EntityChangeBlockEvent):
    """
    Called when an {@link Entity} breaks a door
    <p>
    Cancelling the event will cause the event to be delayed
    """

    def __init__(self, entity: LivingEntity, target_block: Block) -> None:
        ...

    def get_entity(self) -> LivingEntity:
        ...