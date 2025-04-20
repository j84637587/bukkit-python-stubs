from typing import TypeVar, Generic, Type, Any
from org.bukkit.persistence import PersistentDataType
from org.jetbrains.annotations import NotNull

T = TypeVar('T')
Z = TypeVar('Z')

class ItemTagType(Generic[T, Z]):
    """
    This class represents an enum with a generic content type. It defines the
    types a custom item tag can have.
    <p>
    This interface can be used to create your own custom {@link ItemTagType} with
    different complex types. This may be useful for the likes of a
    UUIDItemTagType:
    <pre>
    {@code
    public class UUIDItemTagType implements ItemTagType<byte[], UUID> {

            {@literal @Override}
            public Class<byte[]> getPrimitiveType() {
                return byte[].class;
            }

            {@literal @Override}
            public Class<UUID> getComplexType() {
                return UUID.class;
            }

            {@literal @Override}
            public byte[] toPrimitive(UUID complex, ItemTagAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(new byte[16]);
                bb.putLong(complex.getMostSignificantBits());
                bb.putLong(complex.getLeastSignificantBits());
                return bb.array();
            }

            {@literal @Override}
            public UUID fromPrimitive(byte[] primitive, ItemTagAdapterContext context) {
                ByteBuffer bb = ByteBuffer.wrap(primitive);
                long firstLong = bb.getLong();
                long secondLong = bb.getLong();
                return new UUID(firstLong, secondLong);
            }
        }}</pre>

    @param <T> the primary object type that is stored in the given tag
    @param <Z> the retrieved object type when applying this item tag type

    @deprecated please use {@link PersistentDataType} as this part of the api is being replaced
    """

    BYTE: ItemTagType[bytes, bytes]
    SHORT: ItemTagType[int, int]
    INTEGER: ItemTagType[int, int]
    LONG: ItemTagType[int, int]
    FLOAT: ItemTagType[float, float]
    DOUBLE: ItemTagType[float, float]
    STRING: ItemTagType[str, str]
    BYTE_ARRAY: ItemTagType[bytes, bytes]
    INTEGER_ARRAY: ItemTagType[list[int], list[int]]
    LONG_ARRAY: ItemTagType[list[int], list[int]]
    TAG_CONTAINER: ItemTagType['CustomItemTagContainer', 'CustomItemTagContainer']

        def getPrimitiveType(self) -> Type[T]:
        """
        Returns the primitive data type of this tag.

        @return the class
        """
        ...

        def getComplexType(self) -> Type[Z]:
        """
        Returns the complex object type the primitive value resembles.

        @return the class type
        """
        ...

        def toPrimitive(self, complex: Z, context: 'ItemTagAdapterContext') -> T:
        """
        Returns the primitive data that resembles the complex object passed to
        this method.

        @param complex the complex object instance
        @param context the context this operation is running in
        @return the primitive value
        """
        ...

        def fromPrimitive(self, primitive: T, context: 'ItemTagAdapterContext') -> Z:
        """
        Creates a complex object based of the passed primitive value

        @param primitive the primitive value
        @param context the context this operation is running in
        @return the complex object instance
        """
        ...


class PrimitiveTagType(Generic[T], ItemTagType[T, T]):
    """
    A default implementation that simply exists to pass on the retrieved or
    inserted value to the next layer.

    This implementation does not add any kind of logic, but is used to
    provide default implementations for the primitive types.

    @param <T> the generic type of the primitive objects
    """

    def __init__(self, primitiveType: Type[T]) -> None:
        ...

        def getPrimitiveType(self) -> Type[T]:
        ...

        def getComplexType(self) -> Type[T]:
        ...

        def toPrimitive(self, complex: T, context: 'ItemTagAdapterContext') -> T:
        ...

        def fromPrimitive(self, primitive: T, context: 'ItemTagAdapterContext') -> T:
        ...