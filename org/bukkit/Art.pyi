from typing import Optional, List
from org.bukkit import OldEnum, Keyed, RegistryAware, NamespacedKey, Registry, Bukkit

class Art(OldEnum, Keyed, RegistryAware):
    """
    Represents the art on a painting.
    The arts listed in this interface are present in the default server
    or can be enabled via a FeatureFlag.
    There may be additional arts present in the server, for example from a DataPack
    which can be accessed via Registry.ART.
    """

    KEBAB: Art
    AZTEC: Art
    ALBAN: Art
    AZTEC2: Art
    BOMB: Art
    PLANT: Art
    WASTELAND: Art
    POOL: Art
    COURBET: Art
    SEA: Art
    SUNSET: Art
    CREEBET: Art
    WANDERER: Art
    GRAHAM: Art
    MATCH: Art
    BUST: Art
    STAGE: Art
    VOID: Art
    SKULL_AND_ROSES: Art
    WITHER: Art
    FIGHTERS: Art
    POINTER: Art
    PIGSCENE: Art
    BURNING_SKULL: Art
    SKELETON: Art
    DONKEY_KONG: Art
    EARTH: Art
    WIND: Art
    WATER: Art
    FIRE: Art
    BAROQUE: Art
    HUMBLE: Art
    MEDITATIVE: Art
    PRAIRIE_RIDE: Art
    UNPACKED: Art
    BACKYARD: Art
    BOUQUET: Art
    CAVEBIRD: Art
    CHANGING: Art
    COTAN: Art
    ENDBOSS: Art
    FERN: Art
    FINDING: Art
    LOWMIST: Art
    ORB: Art
    OWLEMONS: Art
    PASSAGE: Art
    POND: Art
    SUNFLOWERS: Art
    TIDES: Art

    def getBlockWidth(self) -> int:
        """
        Gets the width of the painting, in blocks
        """
        ...

    def getBlockHeight(self) -> int:
        """
        Gets the height of the painting, in blocks
        """
        ...

    def getKey(self) -> NamespacedKey:
        """
        {@inheritDoc}
        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...

    def getId(self) -> int:
        """
        Get the ID of this painting.
        @deprecated Magic value
        """
        ...

    @staticmethod
    def getById(id: int) -> Optional[Art]:
        """
        Get a painting by its numeric ID
        @deprecated Magic value
        """
        ...

    @staticmethod
    def getByName(name: str) -> Optional[Art]:
        """
        Get a painting by its unique name
        This ignores capitalization
        @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
        """
        ...

    @staticmethod
    def valueOf(name: str) -> Art:
        """
        @param name of the art.
        @return the art with the given name.
        @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
        """
        ...

    @staticmethod
    def values() -> List[Art]:
        """
        @return an array of all known arts.
        @deprecated use {@link Registry#iterator()}.
        """
        ...