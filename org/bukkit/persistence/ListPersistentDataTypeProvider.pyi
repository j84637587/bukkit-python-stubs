from typing import List, TypeVar, Generic
from org.bukkit.persistence import PersistentDataType, PersistentDataContainer, PersistentDataAdapterContext

P = TypeVar('P')
C = TypeVar('C')

class ListPersistentDataTypeProvider:
    """
    A provider for list persistent data types that represent the known primitive
    types exposed by {@link PersistentDataType}.
    """

    BYTE: 'ListPersistentDataType[bytes, bytes]'
    SHORT: 'ListPersistentDataType[bytes, bytes]'
    INTEGER: 'ListPersistentDataType[int, int]'
    LONG: 'ListPersistentDataType[int, int]'
    FLOAT: 'ListPersistentDataType[float, float]'
    DOUBLE: 'ListPersistentDataType[float, float]'
    BOOLEAN: 'ListPersistentDataType[bytes, bool]'
    STRING: 'ListPersistentDataType[str, str]'
    BYTE_ARRAY: 'ListPersistentDataType[bytes, bytes]'
    INTEGER_ARRAY: 'ListPersistentDataType[List[int], List[int]]'
    LONG_ARRAY: 'ListPersistentDataType[List[int], List[int]]'
    DATA_CONTAINER: 'ListPersistentDataType[PersistentDataContainer, PersistentDataContainer]'

    def __init__(self) -> None:
        pass

    def bytes(self) -> 'ListPersistentDataType[bytes, bytes]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of bytes.

        @return: the persistent data type.
        """
        ...

    def shorts(self) -> 'ListPersistentDataType[bytes, bytes]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of shorts.

        @return: the persistent data type.
        """
        ...

    def integers(self) -> 'ListPersistentDataType[int, int]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of integers.

        @return: the persistent data type.
        """
        ...

    def longs(self) -> 'ListPersistentDataType[int, int]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of longs.

        @return: the persistent data type.
        """
        ...

    def floats(self) -> 'ListPersistentDataType[float, float]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of floats.

        @return: the persistent data type.
        """
        ...

    def doubles(self) -> 'ListPersistentDataType[float, float]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of doubles.

        @return: the persistent data type.
        """
        ...

    def booleans(self) -> 'ListPersistentDataType[bytes, bool]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of booleans.

        @return: the persistent data type.
        """
        ...

    def strings(self) -> 'ListPersistentDataType[str, str]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of strings.

        @return: the persistent data type.
        """
        ...

    def byteArrays(self) -> 'ListPersistentDataType[bytes, bytes]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of byte arrays.

        @return: the persistent data type.
        """
        ...

    def integerArrays(self) -> 'ListPersistentDataType[List[int], List[int]]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of int arrays.

        @return: the persistent data type.
        """
        ...

    def longArrays(self) -> 'ListPersistentDataType[List[int], List[int]]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        storing lists of long arrays.

        @return: the persistent data type.
        """
        ...

    def dataContainers(self) -> 'ListPersistentDataType[PersistentDataContainer, PersistentDataContainer]':
        """
        Provides a shared {@link ListPersistentDataType} that is capable of
        persistent data containers.

        @return: the persistent data type.
        """
        ...

    def listTypeFrom(self, elementType: 'PersistentDataType[P, C]') -> 'ListPersistentDataType[P, C]':
        """
        Constructs a new list persistent data type given any persistent data type
        for its elements.

        @param elementType: the persistent data type that is capable of
        writing/reading the elements of the list.
        @param <P>: the generic type of the primitives stored in the list.
        @param <C>: the generic type of the complex values yielded back by the
        persistent data types.
        @return: the created list persistent data type.
        """
        ...

class ListPersistentDataTypeImpl(Generic[P, C], ListPersistentDataType[P, C]):
    """
    A private implementation of the {@link ListPersistentDataType} that uses
    {@link Collections2} for conversion from/to the primitive list.

    @param <P>: the generic type of the primitives stored in the list.
    @param <C>: the generic type of the complex values yielded back by the
    persistent data types.
    """

    def __init__(self, innerType: 'PersistentDataType[P, C]') -> None:
        ...

    def getPrimitiveType(self) -> 'Type[List[P]]':
        ...

    def getComplexType(self) -> 'Type[List[C]]':
        ...

    def toPrimitive(self, complex: List[C], context: 'PersistentDataAdapterContext') -> List[P]:
        ...

    def fromPrimitive(self, primitive: List[P], context: 'PersistentDataAdapterContext') -> List[C]:
        ...

    def elementType(self) -> 'PersistentDataType[P, C]':
        ...