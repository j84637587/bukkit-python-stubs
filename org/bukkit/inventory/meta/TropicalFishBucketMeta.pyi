from org.bukkit.DyeColor import DyeColor
from org.bukkit.entity.TropicalFish import TropicalFish
from typing import Protocol

class TropicalFishBucketMeta(Protocol):
    """
    Represents a bucket of tropical fish.
    """

    def get_pattern_color(self) -> DyeColor:
        """
        Gets the color of the fish's pattern.
        <p>
        Plugins should check that has_variant() returns <code>true</code> before
        calling this method.

        @return: pattern color
        """
        ...

    def set_pattern_color(self, color: DyeColor) -> None:
        """
        Sets the color of the fish's pattern.
        <p>
        Setting this when has_variant() returns <code>false</code> will initialize
        all other values to unspecified defaults.

        @param color: pattern color
        """
        ...

    def get_body_color(self) -> DyeColor:
        """
        Gets the color of the fish's body.
        <p>
        Plugins should check that has_variant() returns <code>true</code> before
        calling this method.

        @return: pattern color
        """
        ...

    def set_body_color(self, color: DyeColor) -> None:
        """
        Sets the color of the fish's body.
        <p>
        Setting this when has_variant() returns <code>false</code> will initialize
        all other values to unspecified defaults.

        @param color: body color
        """
        ...

    def get_pattern(self) -> TropicalFish.Pattern:
        """
        Gets the fish's pattern.
        <p>
        Plugins should check that has_variant() returns <code>true</code> before
        calling this method.

        @return: pattern
        """
        ...

    def set_pattern(self, pattern: TropicalFish.Pattern) -> None:
        """
        Sets the fish's pattern.
        <p>
        Setting this when has_variant() returns <code>false</code> will initialize
        all other values to unspecified defaults.

        @param pattern: new pattern
        """
        ...

    def has_variant(self) -> bool:
        """
        Checks for existence of a variant tag indicating a specific fish will be
        spawned.

        @return: if there is a variant
        """
        ...

    def clone(self) -> TropicalFishBucketMeta:
        ...