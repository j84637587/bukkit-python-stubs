from typing import Optional
from .container import Container
from .nameable import Nameable
from .lootable import Lootable
import org.bukkit.block_projectile_source import BlockProjectileSource

class Dispenser(Container, Nameable, Lootable):
    """
    Represents a captured state of a dispenser.
    """

    def get_block_projectile_source(self) -> Optional[BlockProjectileSource]:
        """
        Gets the BlockProjectileSource object for the dispenser.
        <p>
        If the block represented by this state is no longer a dispenser, this
        will return None.

        @return: a BlockProjectileSource if valid, otherwise None
        @raises IllegalStateException: if this block state is not placed
        """
        ...

    def dispense(self) -> bool:
        """
        Attempts to dispense the contents of the dispenser.
        <p>
        If the block represented by this state is no longer a dispenser, this
        will return False.

        @return: true if successful, otherwise false
        @raises IllegalStateException: if this block state is not placed
        """
        ...