from typing import TypeVar, Generic, Any
from org.jetbrains.annotations import NotNull

P = TypeVar('P')
C = TypeVar('C')

class PersistentDataType(Generic[P, C]):
    """
    This class represents an enum with a generic content type. It defines the
    types a custom tag can have.
    <p>
    This interface can be used to create your own custom
    {@link PersistentDataType} with different complex types. This may be useful
    for the likes of a UUIDTagType:
    <pre>
    {@code
    public class UUIDTagType implements PersistentDataType<byte[], UUID> {

            @Override
            public Class<byte[]> getPrimitiveType() {
                return byte[].class;
            }

            @Override
            public Class<UUID> getComplexType() {
                return UUID.class;
            }

            @Override
            public byte[] toPrimitive(UUID complex, PersistentDataAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(new byte[16]);
                bb.putLong(complex.getMostSignificantBits());
                bb.putLong(complex.getLeastSignificantBits());
                return bb.array();
            }

            @Override
            public UUID fromPrimitive(byte[] primitive, PersistentDataAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(primitive);
                long firstLong = bb.getLong();
                long secondLong = bb.getLong();
                return new UUID(firstLong, secondLong);
            }
        }
    }</pre>

    Any plugin owned implementation of this interface is required to define one
    of the existing primitive types found in this interface. Notably
    {@link #BOOLEAN} is not a primitive type but a convenience type.

    @param <P> the primary object type that is stored in the given tag
    @param <C> the retrieved object type when applying this tag type
    """

    BYTE: 'PersistentDataType[bytes, bytes]'
    SHORT: 'PersistentDataType[int, int]'
    INTEGER: 'PersistentDataType[int, int]'
    LONG: 'PersistentDataType[int, int]'
    FLOAT: 'PersistentDataType[float, float]'
    DOUBLE: 'PersistentDataType[float, float]'
    BOOLEAN: 'PersistentDataType[bytes, bool]'
    STRING: 'PersistentDataType[str, str]'
    BYTE_ARRAY: 'PersistentDataType[bytes, bytes]'
    INTEGER_ARRAY: 'PersistentDataType[list[int], list[int]]'
    LONG_ARRAY: 'PersistentDataType[list[int], list[int]]'
    TAG_CONTAINER_ARRAY: 'PersistentDataType[list[Any], list[Any]]'
    TAG_CONTAINER: 'PersistentDataType[Any, Any]'
    LIST: 'ListPersistentDataTypeProvider'

        def getPrimitiveType(self) -> type[P]:
        """
        Returns the primitive data type of this tag.

        @return the class
        """

        def getComplexType(self) -> type[C]:
        """
        Returns the complex object type the primitive value resembles.

        @return the class type
        """

        def toPrimitive(self, complex: C, context: 'PersistentDataAdapterContext') -> P:
        """
        Returns the primitive data that resembles the complex object passed to
        this method.

        @param complex the complex object instance
        @param context the context this operation is running in
        @return the primitive value
        """

        def fromPrimitive(self, primitive: P, context: 'PersistentDataAdapterContext') -> C:
        """
        Creates a complex object based of the passed primitive value

        @param primitive the primitive value
        @param context the context this operation is running in
        @return the complex object instance
        """


class PrimitivePersistentDataType(Generic[P], PersistentDataType[P, P]):
    """
    A default implementation that simply exists to pass on the retrieved or
    inserted value to the next layer.
    <p>
    This implementation does not add any kind of logic, but is used to
    provide default implementations for the primitive types.

    @param <P> the generic type of the primitive objects
    """

    def __init__(self, primitiveType: type[P]) -> None:
        self.primitiveType = primitiveType

        def getPrimitiveType(self) -> type[P]:
        ...

        def getComplexType(self) -> type[P]:
        ...

        def toPrimitive(self, complex: P, context: 'PersistentDataAdapterContext') -> P:
        ...

        def fromPrimitive(self, primitive: P, context: 'PersistentDataAdapterContext') -> P:
        ...


class BooleanPersistentDataType(PersistentDataType[bytes, bool]):
    """
    A convenience implementation to convert between Byte and Boolean as there is
    no native implementation for booleans. <br>
    Any byte value not equal to 0 is considered to be true.
    """

        def getPrimitiveType(self) -> type[bytes]:
        ...

        def getComplexType(self) -> type[bool]:
        ...

        def toPrimitive(self, complex: bool, context: 'PersistentDataAdapterContext') -> bytes:
        ...

        def fromPrimitive(self, primitive: bytes, context: 'PersistentDataAdapterContext') -> bool:
        ...