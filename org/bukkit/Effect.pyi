from typing import ClassVar, Dict, Optional, Type
from enum import Enum

class Effect(Enum):
    """
    A list of effects that the server is able to send to players.
    """
    CLICK2 = (1000, "SOUND")
    CLICK1 = (1001, "SOUND")
    BOW_FIRE = (1002, "SOUND")
    DOOR_TOGGLE = (1006, "SOUND")
    IRON_DOOR_TOGGLE = (1005, "SOUND")
    TRAPDOOR_TOGGLE = (1007, "SOUND")
    IRON_TRAPDOOR_TOGGLE = (1037, "SOUND")
    FENCE_GATE_TOGGLE = (1008, "SOUND")
    DOOR_CLOSE = (1012, "SOUND")
    IRON_DOOR_CLOSE = (1011, "SOUND")
    TRAPDOOR_CLOSE = (1013, "SOUND")
    IRON_TRAPDOOR_CLOSE = (1036, "SOUND")
    FENCE_GATE_CLOSE = (1014, "SOUND")
    EXTINGUISH = (1009, "SOUND")
    RECORD_PLAY = (1010, "SOUND", Material)
    GHAST_SHRIEK = (1015, "SOUND")
    GHAST_SHOOT = (1016, "SOUND")
    BLAZE_SHOOT = (1018, "SOUND")
    ZOMBIE_CHEW_WOODEN_DOOR = (1019, "SOUND")
    ZOMBIE_CHEW_IRON_DOOR = (1020, "SOUND")
    ZOMBIE_DESTROY_DOOR = (1021, "SOUND")
    SMOKE = (2000, "VISUAL", BlockFace)
    STEP_SOUND = (2001, "SOUND", Material)
    POTION_BREAK = (2002, "VISUAL", Color)
    INSTANT_POTION_BREAK = (2007, "VISUAL", Color)
    ENDER_SIGNAL = (2003, "VISUAL")
    MOBSPAWNER_FLAMES = (2004, "VISUAL")
    BREWING_STAND_BREW = (1035, "SOUND")
    CHORUS_FLOWER_GROW = (1033, "SOUND")
    CHORUS_FLOWER_DEATH = (1034, "SOUND")
    PORTAL_TRAVEL = (1032, "SOUND")
    ENDEREYE_LAUNCH = (1003, "SOUND")
    FIREWORK_SHOOT = (1004, "SOUND")
    VILLAGER_PLANT_GROW = (2005, "VISUAL", int)
    DRAGON_BREATH = (2006, "VISUAL")
    ANVIL_BREAK = (1029, "SOUND")
    ANVIL_USE = (1030, "SOUND")
    ANVIL_LAND = (1031, "SOUND")
    ENDERDRAGON_SHOOT = (1017, "SOUND")
    WITHER_BREAK_BLOCK = (1022, "SOUND")
    WITHER_SHOOT = (1024, "SOUND")
    ZOMBIE_INFECT = (1026, "SOUND")
    ZOMBIE_CONVERTED_VILLAGER = (1027, "SOUND")
    BAT_TAKEOFF = (1025, "SOUND")
    END_GATEWAY_SPAWN = (3000, "VISUAL")
    ENDERDRAGON_GROWL = (3001, "SOUND")
    PHANTOM_BITE = (1039, "SOUND")
    ZOMBIE_CONVERTED_TO_DROWNED = (1040, "SOUND")
    HUSK_CONVERTED_TO_ZOMBIE = (1041, "SOUND")
    GRINDSTONE_USE = (1042, "SOUND")
    BOOK_PAGE_TURN = (1043, "SOUND")
    SMITHING_TABLE_USE = (1044, "SOUND")
    POINTED_DRIPSTONE_LAND = (1045, "SOUND")
    POINTED_DRIPSTONE_DRIP_LAVA_INTO_CAULDRON = (1046, "SOUND")
    POINTED_DRIPSTONE_DRIP_WATER_INTO_CAULDRON = (1047, "SOUND")
    SKELETON_CONVERTED_TO_STRAY = (1048, "SOUND")
    COMPOSTER_FILL_ATTEMPT = (1500, "VISUAL", bool)
    LAVA_INTERACT = (1501, "VISUAL")
    REDSTONE_TORCH_BURNOUT = (1502, "VISUAL")
    END_PORTAL_FRAME_FILL = (1503, "VISUAL")
    DRIPPING_DRIPSTONE = (1504, "VISUAL")
    BONE_MEAL_USE = (1505, "VISUAL", int)
    ENDER_DRAGON_DESTROY_BLOCK = (2008, "VISUAL")
    SPONGE_DRY = (2009, "VISUAL")
    ELECTRIC_SPARK = (3002, "VISUAL", Axis)
    COPPER_WAX_ON = (3003, "VISUAL")
    COPPER_WAX_OFF = (3004, "VISUAL")
    OXIDISED_COPPER_SCRAPE = (3005, "VISUAL")

    id: int
    type: str
    data: Optional[Type] = None
    BY_ID: ClassVar[Dict[int, 'Effect']] = {}

    def __init__(self, id: int, type: str, data: Optional[Type] = None) -> None:
        self.id = id
        self.type = type
        self.data = data

    def getId(self) -> int:
        """
        Gets the ID for this effect.
        """
        return self.id

    def getType(self) -> str:
        """
        Gets the type of the effect.
        """
        return self.type

    def getData(self) -> Optional[Type]:
        """
        Gets the class which represents data for this effect, or null if none.
        """
        return self.data

    @staticmethod
    def getById(id: int) -> Optional['Effect']:
        """
        Gets the Effect associated with the given ID.
        """
        return Effect.BY_ID.get(id)

    class Type(Enum):
        """
        Represents the type of an effect.
        """
        SOUND = "SOUND"
        VISUAL = "VISUAL"