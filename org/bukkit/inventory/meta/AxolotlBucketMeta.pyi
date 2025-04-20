from org.bukkit.entity import Axolotl
from org.bukkit.inventory.meta import ItemMeta
from typing import Protocol

class AxolotlBucketMeta(Protocol):
    """Represents a bucket of axolotl."""

    def get_variant(self) -> Axolotl.Variant:
        """
        Get the variant of the axolotl in the bucket.
        <p>
        Plugins should check that has_variant() returns <code>true</code> before
        calling this method.
        @return axolotl variant
        """

    def set_variant(self, variant: Axolotl.Variant) -> None:
        """
        Set the variant of this axolotl in the bucket.

        @param variant axolotl variant
        """

    def has_variant(self) -> bool:
        """
        Checks for existence of a variant tag indicating a specific axolotl will be
        spawned.

        @return if there is a variant
        """

    def clone(self) -> AxolotlBucketMeta:
        """Override method to clone the AxolotlBucketMeta instance."""