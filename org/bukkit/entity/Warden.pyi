from org.bukkit.entity import Monster
from org.bukkit import Location
from org.jetbrains.annotations import NotNull, Nullable

"""
A Warden.
"""
class Warden(Monster):

    """
    Gets the anger level of this warden.

    Anger is an integer from 0 to 150. Once a Warden reaches 80 anger at a
    target it will actively pursue it.

    @return anger level
    """
    def get_anger(self) -> int: ...

    """
    Gets the anger level of this warden.

    Anger is an integer from 0 to 150. Once a Warden reaches 80 anger at a
    target it will actively pursue it.

    @param entity target entity
    @return anger level
    """
    def get_anger(self, entity: NotNull['Entity']) -> int: ...

    """
    Increases the anger level of this warden.

    Anger is an integer from 0 to 150. Once a Warden reaches 80 anger at a
    target it will actively pursue it.

    @param entity target entity
    @param increase number to increase by
    @see #getAnger(org.bukkit.entity.Entity)
    """
    def increase_anger(self, entity: NotNull['Entity'], increase: int) -> None: ...

    """
    Sets the anger level of this warden.

    Anger is an integer from 0 to 150. Once a Warden reaches 80 anger at a
    target it will actively pursue it.

    @param entity target entity
    @param anger new anger level
    @see #getAnger(org.bukkit.entity.Entity)
    """
    def set_anger(self, entity: NotNull['Entity'], anger: int) -> None: ...

    """
    Clears the anger level of this warden.

    @param entity target entity
    """
    def clear_anger(self, entity: NotNull['Entity']) -> None: ...

    """
    Gets the {@link LivingEntity} at which this warden is most angry.

    @return The target {@link LivingEntity} or null
    """
        def get_entity_angry_at(self) -> 'LivingEntity': ...

    """
    Make the warden sense a disturbance in the force at the location given.

    @param location location of the disturbance
    """
    def set_disturbance_location(self, location: NotNull[Location]) -> None: ...

    """
    Get the level of anger of this warden.

    @return The level of anger
    """
        def get_anger_level(self) -> 'AngerLevel': ...

    class AngerLevel:
        """
        Anger level 0-39.
        """
        CALM: 'AngerLevel'

        """
        Anger level 40-79.
        """
        AGITATED: 'AngerLevel'

        """
        Anger level 80 or above.
        """
        ANGRY: 'AngerLevel'