from typing import Optional
from org.bukkit.plugin import Plugin

class NamespacedKey:
    """
    Represents a String based key which consists of two components - a namespace
    and a key.

    Namespaces may only contain lowercase alphanumeric characters, periods,
    underscores, and hyphens.
    <p>
    Keys may only contain lowercase alphanumeric characters, periods,
    underscores, hyphens, and forward slashes.
    """
    MINECRAFT: str = "minecraft"
    BUKKIT: str = "bukkit"

    def __init__(self, namespace: str, key: str) -> None:
        """
        Create a key in a specific namespace.

        @param namespace namespace
        @param key key
        @apiNote should never be used by plugins, for internal use only!!
        """
        pass

    def __init__(self, plugin: Plugin, key: str) -> None:
        """
        Create a key in the plugin's namespace.
        <p>
        Namespaces may only contain lowercase alphanumeric characters, periods,
        underscores, and hyphens.
        <p>
        Keys may only contain lowercase alphanumeric characters, periods,
        underscores, hyphens, and forward slashes.

        @param plugin the plugin to use for the namespace
        @param key the key to create
        """
        pass

    def getNamespace(self) -> str:
        pass

    def getKey(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: object) -> bool:
        pass

    def toString(self) -> str:
        pass

    @staticmethod
    def randomKey() -> 'NamespacedKey':
        """
        Return a new random key in the {@link #BUKKIT} namespace.

        @return new key
        @deprecated should never be used by plugins, for internal use only!!
        """
        pass

    @staticmethod
    def minecraft(key: str) -> 'NamespacedKey':
        """
        Get a key in the Minecraft namespace.

        @param key the key to use
        @return new key in the Minecraft namespace
        """
        pass

    @staticmethod
    def fromString(string: str, defaultNamespace: Optional[Plugin] = None) -> Optional['NamespacedKey']:
        """
        Get a NamespacedKey from the supplied string with a default namespace if
        a namespace is not defined. This is a utility method meant to fetch a
        NamespacedKey from user input. Please note that casing does matter and
        any instance of uppercase characters will be considered invalid. The
        input contract is as follows:
        <pre>
        fromString("foo", plugin) -{@literal >} "plugin:foo"
        fromString("foo:bar", plugin) -{@literal >} "foo:bar"
        fromString(":foo", null) -{@literal >} "minecraft:foo"
        fromString("foo", null) -{@literal >} "minecraft:foo"
        fromString("Foo", plugin) -{@literal >} null
        fromString(":Foo", plugin) -{@literal >} null
        fromString("foo:bar:bazz", plugin) -{@literal >} null
        fromString("", plugin) -{@literal >} null
        </pre>

        @param string the string to convert to a NamespacedKey
        @param defaultNamespace the default namespace to use if none was
        supplied. If null, the {@code minecraft} namespace
        ({@link #minecraft(String)}) will be used
        @return the created NamespacedKey. null if invalid key
        @see #fromString(String)
        """
        pass