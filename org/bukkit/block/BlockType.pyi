from typing import TypeVar, Callable, Generic, Type, Optional

B = TypeVar('B', bound='BlockData')

class BlockType(Generic[B]):
    """
    While this API is in a public interface, it is not intended for use by
    plugins until further notice. The purpose of these types is to make
    Material more maintenance friendly, but will in due time be the
    official replacement for the aforementioned enum. Entirely incompatible
    changes may occur. Do not use this API in plugins.
    """

    @staticmethod
    def get_block_type(key: str) -> B:
        """
        Cast instead of using BlockType#typed, since block type can be a mock during testing and would return null.
        """
        ...

    def typed(self) -> 'BlockType.Typed[BlockData]':
        """
        Yields this block type as a typed version of itself with a plain BlockData representing it.
        """
        ...

    def typed(self, block_data_type: Type[B]) -> 'BlockType.Typed[B]':
        """
        Yields this block type as a typed version of itself with a specific BlockData representing it.
        """
        ...

    def has_item_type(self) -> bool:
        """
        Returns true if this BlockType has a corresponding ItemType.
        """
        ...

    def get_item_type(self) -> 'ItemType':
        """
        Returns the corresponding ItemType for the given BlockType.
        """
        ...

    def get_block_data_class(self) -> Type[B]:
        """
        Gets the BlockData class of this BlockType.
        """
        ...

    def create_block_data(self) -> 'BlockData':
        """
        Creates a new BlockData instance for this block type, with all properties initialized to unspecified defaults.
        """
        ...

    def create_block_data(self, data: Optional[str]) -> 'BlockData':
        """
        Creates a new BlockData instance for this block type, with all properties initialized to unspecified defaults, except for those provided in data.
        """
        ...

    def is_solid(self) -> bool:
        """
        Check if the block type is solid (can be built upon).
        """
        ...

    def is_flammable(self) -> bool:
        """
        Check if the block type can catch fire.
        """
        ...

    def is_burnable(self) -> bool:
        """
        Check if the block type can burn away.
        """
        ...

    def is_occluding(self) -> bool:
        """
        Check if the block type occludes light in the lighting engine.
        """
        ...

    def has_gravity(self) -> bool:
        """
        @return True if this block type is affected by gravity.
        """
        ...

    def is_interactable(self) -> bool:
        """
        Checks if this block type can be interacted with.
        """
        ...

    def get_hardness(self) -> float:
        """
        Obtains the block's hardness level (also known as "strength").
        """
        ...

    def get_blast_resistance(self) -> float:
        """
        Obtains the blast resistance value (also known as block "durability").
        """
        ...

    def get_slipperiness(self) -> float:
        """
        Returns a value that represents how 'slippery' the block is.
        """
        ...

    def is_air(self) -> bool:
        """
        Check if the block type is an air block.
        """
        ...

    def is_enabled_by_feature(self, world: 'World') -> bool:
        """
        Gets if the BlockType is enabled by the features in a world.
        """
        ...

    def get_key(self) -> 'NamespacedKey':
        """
        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use #getKeyOrThrow() instead.
        """
        ...

    def as_material(self) -> Optional['Material']:
        """
        Tries to convert this BlockType into a Material.
        @deprecated only for internal use.
        """
        ...

    class Typed(Generic[B]):
        """
        Typed represents a subtype of BlockTypes that have a known block data type at compile time.
        """

        def get_block_data_class(self) -> Type[B]:
            """
            Gets the BlockData class of this BlockType.
            """
            ...

        def create_block_data(self, consumer: Optional[Callable[[B], None]] = None) -> B:
            """
            Creates a new BlockData instance for this block type, with all properties initialized to unspecified defaults.
            """
            ...

        def create_block_data(self) -> B:
            """
            Creates a new BlockData instance for this block type, with all properties initialized to unspecified defaults.
            """
            ...

        def create_block_data(self, data: Optional[str]) -> B:
            """
            Creates a new BlockData instance for this block type, with all properties initialized to unspecified defaults, except for those provided in data.
            """
            ...