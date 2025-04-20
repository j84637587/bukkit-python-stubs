from org.bukkit.Raid import Raid
from org.bukkit.Sound import Sound
from org.bukkit.block.Block import Block
from typing import Optional

class Raider(Monster):
    """
    Interface representing a Raider entity.
    """

    def set_raid(self, raid: Optional[Raid]) -> None:
        """
        Set the {@link Raid} that this raider is participating in.

        :param raid: the raid to set
        """
        ...

    def get_raid(self) -> Optional[Raid]:
        """
        Get the {@link Raid} that this raider is participating in, if any.

        :return: the raid, or None if not participating in a raid
        """
        ...

    def get_wave(self) -> int:
        """
        Get the raid wave that this raider spawned as part of.

        :return: the raid wave, or 0 if not participating in a raid
        """
        ...

    def set_wave(self, wave: int) -> None:
        """
        Set the raid wave that this raider was spawned as part of.

        :param wave: the raid wave to set. Must be >= 0
        """
        ...

    def get_patrol_target(self) -> Optional[Block]:
        """
        Gets the block the raider is targeting to patrol.

        :return: target block or None
        """
        ...

    def set_patrol_target(self, block: Optional[Block]) -> None:
        """
        Sets the block the raider is targeting to patrol.

        :param block: target block or None. Must be in same world as the entity
        """
        ...

    def is_patrol_leader(self) -> bool:
        """
        Gets whether this entity is a patrol leader.

        :return: patrol leader status
        """
        ...

    def set_patrol_leader(self, leader: bool) -> None:
        """
        Sets whether this entity is a patrol leader.

        :param leader: patrol leader status
        """
        ...

    def is_can_join_raid(self) -> bool:
        """
        Gets whether this mob can join an active raid.

        :return: CanJoinRaid status
        """
        ...

    def set_can_join_raid(self, join: bool) -> None:
        """
        Sets whether this mob can join an active raid.

        :param join: CanJoinRaid status
        """
        ...

    def get_ticks_outside_raid(self) -> int:
        """
        Get the amount of ticks that this mob has exited the bounds of a village
        as a raid participant.
        <p>
        This value is increased only when the mob has had no action for 2,400 ticks
        (according to {@link #get_no_action_ticks()}). Once both the no action ticks have
        reached that value and the ticks outside a raid exceeds 30, the mob will be
        expelled from the raid.

        :return: the ticks outside of a raid
        """
        ...

    def set_ticks_outside_raid(self, ticks: int) -> None:
        """
        Set the amount of ticks that this mob has exited the bounds of a village
        as a raid participant.
        <p>
        This value is considered only when the mob has had no action for 2,400 ticks
        (according to {@link #get_no_action_ticks()}). Once both the no action ticks have
        reached that value and the ticks outside a raid exceeds 30, the mob will be
        expelled from the raid.

        :param ticks: the ticks outside of a raid
        """
        ...

    def is_celebrating(self) -> bool:
        """
        Check whether or not this raider is celebrating a raid victory.

        :return: true if celebrating, false otherwise
        """
        ...

    def set_celebrating(self, celebrating: bool) -> None:
        """
        Set whether or not this mob is celebrating a raid victory.

        :param celebrating: whether or not to celebrate
        """
        ...

    def get_celebration_sound(self) -> Sound:
        """
        Get the {@link Sound} this entity will play when celebrating.

        :return: the celebration sound
        """
        ...