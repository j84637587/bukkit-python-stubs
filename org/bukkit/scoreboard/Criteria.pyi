from typing import Type
from org.bukkit import Bukkit
from org.bukkit import Material
from org.bukkit import Statistic
from org.bukkit.entity import EntityType
from org.jetbrains.annotations import NotNull

class Criteria:
    """
    Represents a scoreboard criteria, either custom or built-in to the Minecraft server, used to
    keep track of and manually or automatically change scores on a scoreboard.
    <p>
    While this class outlines constants for standard criteria, see {@link #statistic(Statistic)}
    (and its overloads) to create instances for statistically-backed criteria.
    """

    DUMMY: Criteria = Bukkit.getScoreboardCriteria("dummy")
    TRIGGER: Criteria = Bukkit.getScoreboardCriteria("trigger")
    DEATH_COUNT: Criteria = Bukkit.getScoreboardCriteria("deathCount")
    PLAYER_KILL_COUNT: Criteria = Bukkit.getScoreboardCriteria("playerKillCount")
    TOTAL_KILL_COUNT: Criteria = Bukkit.getScoreboardCriteria("totalKillCount")
    HEALTH: Criteria = Bukkit.getScoreboardCriteria("health")
    FOOD: Criteria = Bukkit.getScoreboardCriteria("food")
    AIR: Criteria = Bukkit.getScoreboardCriteria("air")
    ARMOR: Criteria = Bukkit.getScoreboardCriteria("armor")
    XP: Criteria = Bukkit.getScoreboardCriteria("xp")
    LEVEL: Criteria = Bukkit.getScoreboardCriteria("level")
    TEAM_KILL_BLACK: Criteria = Bukkit.getScoreboardCriteria("teamkill.black")
    TEAM_KILL_DARK_BLUE: Criteria = Bukkit.getScoreboardCriteria("teamkill.dark_blue")
    TEAM_KILL_DARK_GREEN: Criteria = Bukkit.getScoreboardCriteria("teamkill.dark_green")
    TEAM_KILL_DARK_AQUA: Criteria = Bukkit.getScoreboardCriteria("teamkill.dark_aqua")
    TEAM_KILL_DARK_RED: Criteria = Bukkit.getScoreboardCriteria("teamkill.dark_red")
    TEAM_KILL_DARK_PURPLE: Criteria = Bukkit.getScoreboardCriteria("teamkill.dark_purple")
    TEAM_KILL_GOLD: Criteria = Bukkit.getScoreboardCriteria("teamkill.gold")
    TEAM_KILL_GRAY: Criteria = Bukkit.getScoreboardCriteria("teamkill.gray")
    TEAM_KILL_DARK_GRAY: Criteria = Bukkit.getScoreboardCriteria("teamkill.dark_gray")
    TEAM_KILL_BLUE: Criteria = Bukkit.getScoreboardCriteria("teamkill.blue")
    TEAM_KILL_GREEN: Criteria = Bukkit.getScoreboardCriteria("teamkill.green")
    TEAM_KILL_AQUA: Criteria = Bukkit.getScoreboardCriteria("teamkill.aqua")
    TEAM_KILL_RED: Criteria = Bukkit.getScoreboardCriteria("teamkill.red")
    TEAM_KILL_LIGHT_PURPLE: Criteria = Bukkit.getScoreboardCriteria("teamkill.light_purple")
    TEAM_KILL_YELLOW: Criteria = Bukkit.getScoreboardCriteria("teamkill.yellow")
    TEAM_KILL_WHITE: Criteria = Bukkit.getScoreboardCriteria("teamkill.white")
    KILLED_BY_TEAM_BLACK: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.black")
    KILLED_BY_TEAM_DARK_BLUE: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.dark_blue")
    KILLED_BY_TEAM_DARK_GREEN: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.dark_green")
    KILLED_BY_TEAM_DARK_AQUA: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.dark_aqua")
    KILLED_BY_TEAM_DARK_RED: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.dark_red")
    KILLED_BY_TEAM_DARK_PURPLE: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.dark_purple")
    KILLED_BY_TEAM_GOLD: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.gold")
    KILLED_BY_TEAM_GRAY: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.gray")
    KILLED_BY_TEAM_DARK_GRAY: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.dark_gray")
    KILLED_BY_TEAM_BLUE: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.blue")
    KILLED_BY_TEAM_GREEN: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.green")
    KILLED_BY_TEAM_AQUA: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.aqua")
    KILLED_BY_TEAM_RED: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.red")
    KILLED_BY_TEAM_LIGHT_PURPLE: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.light_purple")
    KILLED_BY_TEAM_YELLOW: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.yellow")
    KILLED_BY_TEAM_WHITE: Criteria = Bukkit.getScoreboardCriteria("killedByTeam.white")

        def getName(self) -> str:
        """
        Get the name of this criteria (its unique id).
        @return: the name
        """
        pass

    def isReadOnly(self) -> bool:
        """
        Get whether or not this criteria is read only. If read only, scoreboards with this criteria
        cannot have their scores changed.
        @return: true if read only, false otherwise
        """
        pass

        def getDefaultRenderType(self) -> 'RenderType':
        """
        Get the {@link RenderType} used by default for this criteria.
        @return: the default render type
        """
        pass

        @staticmethod
    def statistic(statistic: Statistic, material: Material) -> Criteria:
        """
        Get a {@link Criteria} for the specified statistic pertaining to blocks or items.
        <p>
        This method expects a {@link Statistic} of {@link Type#BLOCK} or {@link Type#ITEM} and the
        {@link Material} matching said type (e.g. BLOCK statistics require materials where
        {@link Material#isBlock()} is true). This acts as a convenience to create more complex
        compound criteria such as those that increment on block breaks, or item uses. An example
        would be {@code Criteria.statistic(Statistic.CRAFT_ITEM, Material.STICK)}, returning a
        Criteria representing "minecraft.crafted:minecraft.stick" which will increment when the
        player crafts a stick.
        <p>
        If the provided statistic does not require additional data, {@link #statistic(Statistic)}
        is called and returned instead.
        <p>
        This method provides no guarantee that any given criteria exists on the vanilla server.
        @param statistic: the statistic for which to get a criteria
        @param material: the relevant material
        @return: the criteria
        @raises IllegalArgumentException: if {@link Statistic#getType()} is anything other than
        {@link Type#BLOCK} or {@link Type#ITEM}
        @raises IllegalArgumentException: if {@link Statistic#getType()} is {@link Type#BLOCK}, but
        {@link Material#isBlock()} is false
        @raises IllegalArgumentException: if {@link Statistic#getType()} is {@link Type#ITEM}, but
        {@link Material#isItem()} is false
        """
        pass

        @staticmethod
    def statistic(statistic: Statistic, entityType: EntityType) -> Criteria:
        """
        Get a {@link Criteria} for the specified statistic pertaining to an entity type.
        <p>
        This method expects a {@link Statistic} of {@link Type#ENTITY}. This acts as a convenience
        to create more complex compound criteria such as being killed by a specific entity type.
        An example would be {@code Criteria.statistic(Statistic.KILL_ENTITY, EntityType.CREEPER)},
        returning a Criteria representing "minecraft.killed:minecraft.creeper" which will increment
        when the player kills a creepers.
        <p>
        If the provided statistic does not require additional data, {@link #statistic(Statistic)}
        is called and returned instead.
        <p>
        This method provides no guarantee that any given criteria exists on the vanilla server.
        @param statistic: the statistic for which to get a criteria
        @param entityType: the relevant entity type
        @return: the criteria
        @raises IllegalArgumentException: if {@link Statistic#getType()} is not {@link Type#ENTITY}
        """
        pass

        @staticmethod
    def statistic(statistic: Statistic) -> Criteria:
        """
        Get a {@link Criteria} for the specified statistic.
        <p>
        An example would be {@code Criteria.statistic(Statistic.FLY_ONE_CM)}, returning a Criteria
        representing "minecraft.custom:minecraft.aviate_one_cm" which will increment when the player
        flies with an elytra.
        <p>
        This method provides no guarantee that any given criteria exists on the vanilla server. All
        statistics are accepted, however some may not operate as expected if additional data is
        required. For block/item-related statistics, see {@link #statistic(Statistic, Material)},
        and for entity-related statistics, see {@link #statistic(Statistic, EntityType)}
        @param statistic: the statistic for which to get a criteria
        @return: the criteria
        """
        pass

        @staticmethod
    def create(name: str) -> Criteria:
        """
        Get (or create) a new {@link Criteria} by its name.
        @param name: the criteria name
        @return: the created criteria
        """
        pass