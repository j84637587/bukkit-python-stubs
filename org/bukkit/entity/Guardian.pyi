from typing import Protocol

class Guardian(Protocol):
    """
    Interface representing a Guardian entity.
    """

    def set_laser(self, activated: bool) -> bool:
        """
        Sets whether the guardian laser should show or not.

        A target must be present. If no target is present the laser will not show
        and the method will return false.

        Args:
            activated (bool): whether the laser is active

        Returns:
            bool: true if the laser was activated otherwise false
        """
        ...

    def has_laser(self) -> bool:
        """
        Gets whether the guardian laser is active or not.

        Returns:
            bool: true if the laser is active otherwise false
        """
        ...

    def get_laser_duration(self) -> int:
        """
        Get the duration (in ticks) that a laser attack takes.

        Returns:
            int: the laser duration in ticks
        """
        ...

    def set_laser_ticks(self, ticks: int) -> None:
        """
        Set the amount of ticks that have elapsed since this guardian has initiated
        a laser attack. If set to get_laser_duration() or greater, the guardian
        will inflict damage upon its target and the laser attack will complete.

        For this value to have any effect, the guardian must have an active target
        (see set_target(LivingEntity)) and be charging a laser attack (where
        has_laser() is true). The client may display a different animation of
        the guardian laser than the set ticks.

        Args:
            ticks (int): the ticks to set. Must be at least -10
        """
        ...

    def get_laser_ticks(self) -> int:
        """
        Get the amount of ticks that have elapsed since this guardian has initiated
        a laser attack.

        This value may or may not be significant depending on whether or not the guardian
        has an active target (get_target()) and is charging a laser attack
        (has_laser()). This value is not reset after a successful attack nor used
        in the next and will be reset to the minimum value when the guardian initiates a
        new one.

        Returns:
            int: the laser ticks ranging from -10 to get_laser_duration()
        """
        ...

    def is_elder(self) -> bool:
        """
        Check if the Guardian is an elder Guardian.

        Returns:
            bool: true if the Guardian is an Elder Guardian, false if not

        Deprecated:
            should check if instance of ElderGuardian.
        """
        ...

    def set_elder(self, should_be_elder: bool) -> None:
        """
        Args:
            should_be_elder (bool): shouldBeElder

        Deprecated:
            Must spawn a new ElderGuardian.
        """
        ...

    def is_moving(self) -> bool:
        """
        Check whether or not this guardian is moving.

        While moving, the guardian's spikes are retracted and will not inflict thorns
        damage upon entities that attack it. Additionally, a moving guardian cannot
        attack another entity. If stationary (i.e. this method returns false),
        thorns damage is guaranteed and the guardian may initiate laser attacks.

        Returns:
            bool: true if moving, false if stationary
        """
        ...
