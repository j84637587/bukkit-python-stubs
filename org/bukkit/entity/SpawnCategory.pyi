from enum import Enum

class SpawnCategory(Enum):
    """
    Represents groups of entities with shared spawn behaviors and mob caps.

    @see <a href="https://minecraft.wiki/w/Spawn#Java_Edition_mob_cap">Minecraft Wiki</a>
    """
    
    MONSTER = ...
    """Entities related to Monsters, eg: Witch, Zombie, Creeper, etc."""
    
    ANIMAL = ...
    """Entities related to Animals, eg: Strider, Cow, Turtle, etc."""
    
    WATER_ANIMAL = ...
    """Entities related to Water Animals, eg: Squid or Dolphin."""
    
    WATER_AMBIENT = ...
    """Entities related to Water Ambient, eg: Cod, PufferFish, Tropical Fish,
    Salmon, etc."""
    
    WATER_UNDERGROUND_CREATURE = ...
    """Entities related to Water Underground, eg: Glow Squid."""
    
    AMBIENT = ...
    """Entities related to Ambient, eg: Bat."""
    
    AXOLOTL = ...
    """All the Axolotl are represented by this Category."""
    
    MISC = ...
    """Entities not related to a mob, eg: Player, ArmorStand, Boat, etc."""