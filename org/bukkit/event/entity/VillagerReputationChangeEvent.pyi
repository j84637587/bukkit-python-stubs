from typing import Optional
from uuid import UUID
from org.bukkit import Bukkit
from org.bukkit.entity import Entity, Villager
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull, Nullable

class VillagerReputationChangeEvent(EntityEvent, Cancellable):
    """
    Called whenever an entity's reputation with a villager changes.
    """

    handlers: HandlerList

    def __init__(self: "VillagerReputationChangeEvent",
                 villager: Villager,
                 target_uuid: UUID,
                 reason: Villager.ReputationEvent,
                 reputation_type: Villager.ReputationType,
                 old_value: int,
                 new_value: int,
                 max_value: int) -> None:
        ...

        def get_target_uuid(self: "VillagerReputationChangeEvent") -> UUID:
        ...

        def get_target(self: "VillagerReputationChangeEvent") -> Optional[Entity]:
        ...

        def get_reason(self: "VillagerReputationChangeEvent") -> Villager.ReputationEvent:
        ...

        def get_reputation_type(self: "VillagerReputationChangeEvent") -> Villager.ReputationType:
        ...

    def get_old_value(self: "VillagerReputationChangeEvent") -> int:
        ...

    def get_new_value(self: "VillagerReputationChangeEvent") -> int:
        ...

    def set_new_value(self: "VillagerReputationChangeEvent", new_value: int) -> None:
        ...

    def get_max_value(self: "VillagerReputationChangeEvent") -> int:
        ...

    def is_cancelled(self: "VillagerReputationChangeEvent") -> bool:
        ...

    def set_cancelled(self: "VillagerReputationChangeEvent", cancel: bool) -> None:
        ...

        def get_entity(self: "VillagerReputationChangeEvent") -> Villager:
        ...

        def get_handlers(self: "VillagerReputationChangeEvent") -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...