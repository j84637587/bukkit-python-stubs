from typing import List, TypeVar, Protocol
from org.bukkit.persistence import PersistentDataType

P = TypeVar('P')
C = TypeVar('C')

class ListPersistentDataType(Protocol[P, C]):
    """
    The list persistent data represents a data type that is capable of storing a
    list of other data types in a {@link PersistentDataContainer}.

    @param P: the primitive type of the list element.
    @param C: the complex type of the list elements.
    """

    def element_type(self) -> PersistentDataType[P, C]:
        """
        Provides the persistent data type of the elements found in the list.

        @return: the persistent data type.
        """
        ...