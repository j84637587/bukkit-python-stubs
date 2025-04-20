from typing import Set, TypeVar, Generic, Optional
from org.bukkit import NamespacedKey
from org.bukkit.persistence import PersistentDataType
from org.jetbrains.annotations import NotNull, Nullable

P = TypeVar('P')
C = TypeVar('C')

class PersistentDataContainer(Generic[P, C]):
    """
    This interface represents a map like object, capable of storing custom tags
    in it.
    """

        def set(self, key: NamespacedKey, type: PersistentDataType[P, C], value: C) -> None:
        """
        Stores a metadata value on the {@link PersistentDataHolder} instance.
        <p>
        This API cannot be used to manipulate minecraft data, as the values will
        be stored using your namespace. This method will override any existing
        value the {@link PersistentDataHolder} may have stored under the provided
        key.

        @param key the key this value will be stored under
        @param type the type this tag uses
        @param value the value to store in the tag
        @param <P> the generic java type of the tag value
        @param <C> the generic type of the object to store

        @raises IllegalArgumentException if the key is null
        @raises IllegalArgumentException if the type is null
        @raises IllegalArgumentException if the value is null. Removing a tag should
        be done using {@link #remove(NamespacedKey)}
        @raises IllegalArgumentException if no suitable adapter was found for
        the {@link PersistentDataType#getPrimitiveType()}
        """

        def has(self, key: NamespacedKey, type: PersistentDataType[P, C]) -> bool:
        """
        Returns if the persistent metadata provider has metadata registered
        matching the provided parameters.
        <p>
        This method will only return true if the found value has the same primitive
        data type as the provided key.
        <p>
        Storing a value using a custom {@link PersistentDataType} implementation
        will not store the complex data type. Therefore storing a UUID (by
        storing a byte[]) will match has("key" ,
        {@link PersistentDataType#BYTE_ARRAY}). Likewise a stored byte[] will
        always match your UUID {@link PersistentDataType} even if it is not 16
        bytes long.
        <p>
        This method is only usable for custom object keys. Overwriting existing
        tags, like the display name, will not work as the values are stored
        using your namespace.

        @param key the key the value is stored under
        @param type the type the primative stored value has to match
        @param <P> the generic type of the stored primitive
        @param <C> the generic type of the eventually created complex object

        @return if a value with the provided key and type exists

        @raises IllegalArgumentException if the key to look up is null
        @raises IllegalArgumentException if the type to cast the found object to is
        null
        """

        def has(self, key: NamespacedKey) -> bool:
        """
        Returns if the persistent metadata provider has metadata registered matching
        the provided parameters.
        <p>
        This method will return true as long as a value with the given key exists,
        regardless of its type.
        <p>
        This method is only usable for custom object keys. Overwriting existing tags,
        like the display name, will not work as the values are stored using your
        namespace.

        @param key the key the value is stored under

        @return if a value with the provided key exists

        @raises IllegalArgumentException if the key to look up is null
        """

        def get(self, key: NamespacedKey, type: PersistentDataType[P, C]) -> Optional[C]:
        """
        Returns the metadata value that is stored on the
        {@link PersistentDataHolder} instance.

        @param key the key to look up in the custom tag map
        @param type the type the value must have and will be casted to
        @param <P> the generic type of the stored primitive
        @param <C> the generic type of the eventually created complex object

        @return the value or {@code null} if no value was mapped under the given
        value

        @raises IllegalArgumentException if the key to look up is null
        @raises IllegalArgumentException if the type to cast the found object to is
        null
        @raises IllegalArgumentException if a value exists under the given key,
        but cannot be accessed using the given type
        @raises IllegalArgumentException if no suitable adapter was found for
        the {@link
        PersistentDataType#getPrimitiveType()}
        """

        def getOrDefault(self, key: NamespacedKey, type: PersistentDataType[P, C], defaultValue: C) -> C:
        """
        Returns the metadata value that is stored on the
        {@link PersistentDataHolder} instance. If the value does not exist in the
        container, the default value provided is returned.

        @param key the key to look up in the custom tag map
        @param type the type the value must have and will be casted to
        @param defaultValue the default value to return if no value was found for
        the provided key
        @param <P> the generic type of the stored primitive
        @param <C> the generic type of the eventually created complex object

        @return the value or the default value if no value was mapped under the
        given key

        @raises IllegalArgumentException if the key to look up is null
        @raises IllegalArgumentException if the type to cast the found object to is
        null
        @raises IllegalArgumentException if a value exists under the given key,
        but cannot be accessed using the given type
        @raises IllegalArgumentException if no suitable adapter was found for
        the {@link PersistentDataType#getPrimitiveType()}
        """

        def getKeys(self) -> Set[NamespacedKey]:
        """
        Get the set of keys present on this {@link PersistentDataContainer}
        instance.

        Any changes made to the returned set will not be reflected on the
        instance.

        @return the key set
        """

    def remove(self, key: NamespacedKey) -> None:
        """
        Removes a custom key from the {@link PersistentDataHolder} instance.

        @param key the key to remove

        @raises IllegalArgumentException if the provided key is null
        """

    def isEmpty(self) -> bool:
        """
        Returns if the container instance is empty, therefore has no entries
        inside it.

        @return the boolean
        """

    def copyTo(self, other: PersistentDataContainer, replace: bool) -> None:
        """
        Copies all values from this {@link PersistentDataContainer} to the provided
        container.
        <p>
        This method only copies custom object keys. Existing tags, like the display
        name, will not be copied as the values are stored using your namespace.

        @param other   the container to copy to
        @param replace whether to replace any matching values in the target container

        @raises IllegalArgumentException if the other container is null
        """

        def getAdapterContext(self) -> PersistentDataAdapterContext:
        """
        Returns the adapter context this tag container uses.

        @return the tag context
        """