from org.bukkit.Material import Material
from org.bukkit.Warning import Warning
from org.bukkit.entity.Fish import Fish
from org.bukkit.entity.Player import Player
from org.bukkit.inventory.EquipmentSlot import EquipmentSlot
from org.bukkit.inventory.ItemStack import ItemStack
from org.jetbrains.annotations import NotNull

"""
This event is called whenever a player attempts to put a fish in a bucket.

@deprecated Use the more generic {@link PlayerBucketEntityEvent}
"""
@Deprecated(since="1.16.5")
@Warning(False)
class PlayerBucketFishEvent(PlayerBucketEntityEvent):
    def __init__(self: "PlayerBucketFishEvent", player: Player, fish: Fish, water_bucket: ItemStack, fish_bucket: ItemStack, hand: EquipmentSlot) -> None:
        super().__init__(player, fish, water_bucket, fish_bucket, hand)

    """
    Gets the fish involved with this event.

    @return The fish involved with this event
    """
        def get_entity(self: "PlayerBucketFishEvent") -> Fish:
        ...

    """
    Gets the bucket used.

    This refers to the bucket clicked with, ie {@link Material#WATER_BUCKET}.

    @return The used bucket
    @deprecated Use {@link #getOriginalBucket()}
    """
        @Deprecated(since="1.16.5")
    def get_water_bucket(self: "PlayerBucketFishEvent") -> ItemStack:
        ...

    """
    Gets the bucket that the fish will be put into.

    This refers to the bucket with the fish, ie
    {@link Material#PUFFERFISH_BUCKET}.

    @return The bucket that the fish will be put into
    @deprecated Use {@link #getEntityBucket()}
    """
        @Deprecated(since="1.16.5")
    def get_fish_bucket(self: "PlayerBucketFishEvent") -> ItemStack:
        ...