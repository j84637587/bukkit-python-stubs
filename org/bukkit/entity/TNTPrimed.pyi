from typing import Optional
from org.bukkit.entity import Explosive, Entity
from org.bukkit import Location

class TNTPrimed(Explosive):
    """Represents a Primed TNT."""

    def set_fuse_ticks(self, fuse_ticks: int) -> None:
        """Set the number of ticks until the TNT blows up after being primed.

        Args:
            fuse_ticks: The fuse ticks
        """
        ...

    def get_fuse_ticks(self) -> int:
        """Retrieve the number of ticks until the explosion of this TNTPrimed entity.

        Returns:
            The number of ticks until this TNTPrimed explodes
        """
        ...

    def get_source(self) -> Optional[Entity]:
        """Gets the source of this primed TNT. The source is the entity
        responsible for the creation of this primed TNT. (I.E. player ignites
        TNT with flint and steel.) Take note that this can be null if there is
        no suitable source. (created by the {@link
        org.bukkit.World#spawn(Location, Class)} method, for example.)
        <p>
        The source will become null if the chunk this primed TNT is in is
        unloaded then reloaded. The source entity may be invalid if for example
        it has since died or been unloaded. Callers should check
        {@link Entity#isValid()}.

        Returns:
            The source of this primed TNT
        """
        ...

    def set_source(self, source: Optional[Entity]) -> None:
        """Sets the source of this primed TNT.

        The source is the entity responsible for the creation of this primed TNT.
        <p>
        Must be instance of {@link org.bukkit.entity.LivingEntity} otherwise will
        be set to null. The parameter is typed {@link
        org.bukkit.entity.Entity} to be consistent with {@link
        org.bukkit.entity.TNTPrimed#getSource()} method.

        Args:
            source: The source of this primed TNT
        """
        ...