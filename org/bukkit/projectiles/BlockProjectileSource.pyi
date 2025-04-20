from org.bukkit.block import Block
from org.jetbrains.annotations import NotNull
from org.bukkit.projectiles import ProjectileSource

class BlockProjectileSource(ProjectileSource):
    """
    Interface for a block projectile source.
    """

        def get_block(self) -> Block:
        """
        Gets the block this projectile source belongs to.

        :return: Block for the projectile source
        """
        ...