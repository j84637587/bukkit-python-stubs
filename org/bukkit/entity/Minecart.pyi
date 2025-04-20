from org.bukkit import GameRule
from org.bukkit.block.data import BlockData
from org.bukkit.material import MaterialData
from org.bukkit.util import Vector
from typing import Optional

"""
Represents a minecart entity.
"""
class Minecart(Vehicle):

    def set_damage(self, damage: float) -> None:
        """
        Sets a minecart's damage.

        :param damage: over 40 to "kill" a minecart
        """
        ...

    def get_damage(self) -> float:
        """
        Gets a minecart's damage.

        :return: The damage
        """
        ...

    def get_max_speed(self) -> float:
        """
        Gets the maximum speed of a minecart. The speed is unrelated to the
        velocity.

        :return: The max speed
        """
        ...

    def set_max_speed(self, speed: float) -> None:
        """
        Sets the maximum speed of a minecart. Must be nonnegative. Default is
        0.4D or {@link GameRule#MINECART_MAX_SPEED}.

        :param speed: The max speed
        """
        ...

    def is_slow_when_empty(self) -> bool:
        """
        Returns whether this minecart will slow down faster without a passenger
        occupying it.

        :return: Whether it decelerates faster
        """
        ...

    def set_slow_when_empty(self, slow: bool) -> None:
        """
        Sets whether this minecart will slow down faster without a passenger
        occupying it.

        :param slow: Whether it will decelerate faster
        """
        ...

    def get_flying_velocity_mod(self) -> Vector:
        """
        Gets the flying velocity modifier. Used for minecarts that are in
        mid-air. A flying minecart's velocity is multiplied by this factor each
        tick.

        :return: The vector factor
        """
        ...

    def set_flying_velocity_mod(self, flying: Vector) -> None:
        """
        Sets the flying velocity modifier. Used for minecarts that are in
        mid-air. A flying minecart's velocity is multiplied by this factor each
        tick.

        :param flying: velocity modifier vector
        """
        ...

    def get_derailed_velocity_mod(self) -> Vector:
        """
        Gets the derailed velocity modifier. Used for minecarts that are on the
        ground, but not on rails.
        A derailed minecart's velocity is multiplied by this factor each tick.

        :return: derailed visible speed
        """
        ...

    def set_derailed_velocity_mod(self, derailed: Vector) -> None:
        """
        Sets the derailed velocity modifier. Used for minecarts that are on the
        ground, but not on rails. A derailed minecart's velocity is multiplied
        by this factor each tick.

        :param derailed: visible speed
        """
        ...

    def set_display_block(self, material: Optional[MaterialData]) -> None:
        """
        Sets the display block for this minecart.
        Passing a null value will set the minecart to have no display block.

        :param material: the material to set as display block.
        """
        ...

    def get_display_block(self) -> MaterialData:
        """
        Gets the display block for this minecart.
        This function will return the type AIR if none is set.

        :return: the block displayed by this minecart.
        """
        ...

    def set_display_block_data(self, block_data: Optional[BlockData]) -> None:
        """
        Sets the display block for this minecart.
        Passing a null value will set the minecart to have no display block.

        :param block_data: the material to set as display block.
        """
        ...

    def get_display_block_data(self) -> BlockData:
        """
        Gets the display block for this minecart.
        This function will return the type AIR if none is set.

        :return: the block displayed by this minecart.
        """
        ...

    def set_display_block_offset(self, offset: int) -> None:
        """
        Sets the offset of the display block.

        :param offset: the block offset to set for this minecart.
        """
        ...

    def get_display_block_offset(self) -> int:
        """
        Gets the offset of the display block.

        :return: the current block offset for this minecart.
        """
        ...