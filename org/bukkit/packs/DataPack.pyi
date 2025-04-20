from typing import Set
from org.bukkit import FeatureFlag
from org.bukkit import Keyed
from org.jetbrains.annotations import NotNull

"""
Represents a data pack.

@see <a href="https://minecraft.wiki/w/Data_pack">Minecraft wiki</a>
"""
class DataPack(Keyed):

    """
    Gets the title of the data pack.

    @return the title
    """
        def get_title(self) -> str: ...

    """
    Gets the description of the data pack.

    @return the description
    """
        def get_description(self) -> str: ...

    """
    Gets the pack format.
    <br>
    Pack formats are non-standard and unrelated to the version of Minecraft. For
    a list of known pack versions, see the
    <a href="https://minecraft.wiki/w/Data_pack#Pack_format">Minecraft Wiki</a>.

    @return the pack version
    @see #getMinSupportedPackFormat()
    @see #getMaxSupportedPackFormat()
    """
    def get_pack_format(self) -> int: ...

    """
    Gets the minimum supported pack format. If the data pack does not specify a
    minimum supported format, {@link #getPackFormat()} is returned.
    <br>
    Pack formats are non-standard and unrelated to the version of Minecraft. For
    a list of known pack versions, see the
    <a href="https://minecraft.wiki/w/Data_pack#Pack_format">Minecraft Wiki</a>.

    @return the min pack version supported
    """
    def get_min_supported_pack_format(self) -> int: ...

    """
    Gets the maximum supported pack format. If the data pack does not specify a
    maximum supported format, {@link #getPackFormat()} is returned.
    <br>
    Pack formats are non-standard and unrelated to the version of Minecraft. For
    a list of known pack versions, see the
    <a href="https://minecraft.wiki/w/Data_pack#Pack_format">Minecraft Wiki</a>.

    @return the max pack version supported
    """
    def get_max_supported_pack_format(self) -> int: ...

    """
    Gets if the data pack is enabled on the server.

    @return True if is enabled
    """
    def is_enabled(self) -> bool: ...

    """
    Gets if the data pack is required on the server.

    @return True if is required
    """
    def is_required(self) -> bool: ...

    """
    Gets the compatibility of this data pack with the server.

    @return an enum
    """
        def get_compatibility(self) -> 'Compatibility': ...

    """
    Gets a set of features requested by this data pack.

    @return a set of features
    """
        def get_requested_features(self) -> Set[FeatureFlag]: ...

    """
    Gets the source of this data pack.

    @return the source
    """
        def get_source(self) -> 'Source': ...

    class Compatibility:
        """
        It's newer than the server pack version.
        """
        NEW = ...

        """
        It's older than the server pack version.
        """
        OLD = ...

        """
        Its compatible with the server pack version.
        """
        COMPATIBLE = ...

    class Source:
        DEFAULT = ...
        BUILT_IN = ...
        FEATURE = ...
        WORLD = ...
        SERVER = ...