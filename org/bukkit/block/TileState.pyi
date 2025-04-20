from typing import Protocol
from .persistent_data_container import PersistentDataContainer
from .persistent_data_holder import PersistentDataHolder

class TileState(Protocol[PersistentDataHolder]):
    """
    Represents a block state that also hosts a tile entity at the given location.

    This interface alone is merely a marker that does not provide any data.

    Data about the tile entities is provided by the respective interface for each
    tile entity type.

    After modifying the data provided by a TileState, `update()` needs to
    be called to store the data.
    """

    def get_persistent_data_container(self) -> PersistentDataContainer:
        """
        Returns a custom tag container capable of storing tags on the object.

        Note that the tags stored on this container are all stored under their
        own custom namespace therefore modifying default tags using this
        `PersistentDataHolder` is impossible.
        
        This `PersistentDataHolder` is only linked to the snapshot instance
        stored by the `BlockState`.

        When storing changes on the `PersistentDataHolder`, the updated
        content will only be applied to the actual tile entity after one of the
        `update()` methods is called.

        @return: the custom tag container
        """
        ...