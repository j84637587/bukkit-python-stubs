from org.bukkit.Material import Material
from org.bukkit.block.data import BlockData
from typing import Protocol

class FallingBlock(Protocol):
    """Represents a falling block"""

    def get_material(self) -> Material:
        """
        Get the Material of the falling block

        Returns:
            Material of the block
        """
        ...

    def get_block_data(self) -> BlockData:
        """
        Get the data for the falling block

        Returns:
            data of the block
        """
        ...

    def get_drop_item(self) -> bool:
        """
        Get if the falling block will break into an item if it cannot be placed.
        
        Note that if get_cancel_drop() is true, the falling block
        will not drop an item regardless of whether or not the returned value is
        true.

        Returns:
            true if the block will break into an item when obstructed
        """
        ...

    def set_drop_item(self, drop: bool) -> None:
        """
        Set if the falling block will break into an item if it cannot be placed.
        
        Note that if get_cancel_drop() is true, the falling block
        will not drop an item regardless of whether or not the value is set to
        true.

        Args:
            drop: true to break into an item when obstructed
        """
        ...

    def get_cancel_drop(self) -> bool:
        """
        Get if the falling block will not become a block upon landing and not drop
        an item.

        Unlike get_drop_item(), this property will prevent the block from
        forming into a block when it lands, causing it to disappear. If this property
        is true and get_drop_item() is true, an item will NOT be dropped.

        Returns:
            true if the block will disappear
        """
        ...

    def set_cancel_drop(self, cancel_drop: bool) -> None:
        """
        Get if the falling block will not become a block upon landing and not drop
        an item.

        Unlike set_drop_item(boolean), this property will prevent the block
        from forming into a block when it lands, causing it to disappear. If this
        property is true and get_drop_item() is true, an item will
        NOT be dropped.

        Args:
            cancel_drop: true to make the block disappear when landing
        """
        ...

    def can_hurt_entities(self) -> bool:
        """
        Get the HurtEntities state of this block.

        Returns:
            whether entities will be damaged by this block.
        """
        ...

    def set_hurt_entities(self, hurt_entities: bool) -> None:
        """
        Set the HurtEntities state of this block.

        Args:
            hurt_entities: whether entities will be damaged by this block.
        """
        ...

    def get_damage_per_block(self) -> float:
        """
        Get the amount of damage inflicted upon entities multiplied by the distance
        that the block had fallen when this falling block lands on them.

        Returns:
            the damage per block
        """
        ...

    def set_damage_per_block(self, damage: float) -> None:
        """
        Set the amount of damage inflicted upon entities multiplied by the distance
        that the block had fallen when this falling block lands on them.

        If damage is non-zero, this method will automatically call
        set_hurt_entities(true).

        Args:
            damage: the damage per block to set. Must be >= 0.0
        """
        ...

    def get_max_damage(self) -> int:
        """
        Get the maximum amount of damage that can be inflicted upon entities when
        this falling block lands on them.

        Returns:
            the max damage
        """
        ...

    def set_max_damage(self, damage: int) -> None:
        """
        Set the maximum amount of damage that can be inflicted upon entities when
        this falling block lands on them.

        If damage is non-zero, this method will automatically call
        set_hurt_entities(true).

        Args:
            damage: the max damage to set. Must be >= 0
        """
        ...