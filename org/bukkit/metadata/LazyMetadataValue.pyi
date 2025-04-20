from typing import Callable, Optional, Type
from org.bukkit.plugin import Plugin
from org.bukkit.metadata import MetadataValueAdapter
from org.jetbrains.annotations import NotNull, Nullable

class LazyMetadataValue(MetadataValueAdapter):
    """
    The LazyMetadataValue class implements a type of metadata that is not
    computed until another plugin asks for it.
    <p>
    By making metadata values lazy, no computation is done by the providing
    plugin until absolutely necessary (if ever). Additionally,
    LazyMetadataValue objects cache their values internally unless overridden
    by a {@link CacheStrategy} or invalidated at the individual or plugin
    level. Once invalidated, the LazyMetadataValue will recompute its value
    when asked.
    """

    ACTUALLY_NULL: Type[object]

    def __init__(self,
                 owning_plugin: Plugin,
                 lazy_value: Callable[[], object]) -> None:
        """
        Initialized a LazyMetadataValue object with the default
        CACHE_AFTER_FIRST_EVAL cache strategy.

        @param owningPlugin the {@link Plugin} that created this metadata
            value.
        @param lazyValue the lazy value assigned to this metadata value.
        """
        ...

    def __init__(self,
                 owning_plugin: Plugin,
                 cache_strategy: 'CacheStrategy',
                 lazy_value: Callable[[], object]) -> None:
        """
        Initializes a LazyMetadataValue object with a specific cache strategy.

        @param owningPlugin the {@link Plugin} that created this metadata
            value.
        @param cacheStrategy determines the rules for caching this metadata
            value.
        @param lazyValue the lazy value assigned to this metadata value.
        """
        ...

    def __init__(self,
                 owning_plugin: Plugin) -> None:
        """
        Protected special constructor used by FixedMetadataValue to bypass
        standard setup.

        @param owningPlugin the owning plugin
        """
        ...

        def value(self) -> Optional[object]:
        """
        @return: The evaluated value of this metadata item or None if it is
            not available.
        """
        ...

    def eval(self) -> None:
        """
        Lazily evaluates the value of this metadata item.

        @throws MetadataEvaluationException if computing the metadata value
            fails.
        """
        ...

    def invalidate(self) -> None:
        """
        Invalidates the cached value of this metadata item.
        """
        ...

    class CacheStrategy:
        """
        Describes possible caching strategies for metadata.
        """
        CACHE_AFTER_FIRST_EVAL = ...
        NEVER_CACHE = ...
        CACHE_ETERNALLY = ...