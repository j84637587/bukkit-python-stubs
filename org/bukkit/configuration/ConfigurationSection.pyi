from typing import List, Map, Set, Optional, TypeVar, Generic

T = TypeVar('T')
ConfigurationSerializable = TypeVar('ConfigurationSerializable')

class ConfigurationSection(Generic[T]):
    """
    Represents a section of a Configuration
    """

    def getKeys(self, deep: bool) -> Set[str]:
        """
        Gets a set containing all keys in this section.
        If deep is set to true, then this will contain all the keys within any
        child ConfigurationSections (and their children, etc). These
        will be in a valid path notation for you to use.
        If deep is set to false, then this will contain only the keys of any
        direct children, and not their own children.

        :param deep: Whether or not to get a deep list, as opposed to a shallow list.
        :return: Set of keys contained within this ConfigurationSection.
        """
        ...

    def getValues(self, deep: bool) -> Map[str, object]:
        """
        Gets a Map containing all keys and their values for this section.
        If deep is set to true, then this will contain all the keys and values
        within any child ConfigurationSections (and their children, etc). These
        keys will be in a valid path notation for you to use.
        If deep is set to false, then this will contain only the keys and
        values of any direct children, and not their own children.

        :param deep: Whether or not to get a deep list, as opposed to a shallow list.
        :return: Map of keys and values of this section.
        """
        ...

    def contains(self, path: str) -> bool:
        """
        Checks if this ConfigurationSection contains the given path.
        If the value for the requested path does not exist but a default value
        has been specified, this will return true.

        :param path: Path to check for existence.
        :return: True if this section contains the requested path, either via
            default or being set.
        :raises ValueError: Thrown when path is null.
        """
        ...

    def contains(self, path: str, ignoreDefault: bool) -> bool:
        """
        Checks if this ConfigurationSection contains the given path.
        If the value for the requested path does not exist, the boolean parameter
        of true has been specified, a default value for the path exists, this
        will return true.
        If a boolean parameter of false has been specified, true will only be
        returned if there is a set value for the specified path.

        :param path: Path to check for existence.
        :param ignoreDefault: Whether or not to ignore if a default value for the
            specified path exists.
        :return: True if this section contains the requested path, or if a default
            value exists and the boolean parameter for this method is true.
        :raises ValueError: Thrown when path is null.
        """
        ...

    def isSet(self, path: str) -> bool:
        """
        Checks if this ConfigurationSection has a value set for the
        given path.
        If the value for the requested path does not exist but a default value
        has been specified, this will still return false.

        :param path: Path to check for existence.
        :return: True if this section contains the requested path, regardless of
            having a default.
        :raises ValueError: Thrown when path is null.
        """
        ...

    def getCurrentPath(self) -> Optional[str]:
        """
        Gets the path of this ConfigurationSection from its root Configuration
        For any Configuration themselves, this will return an empty
        string.
        If the section is no longer contained within its root for any reason,
        such as being replaced with a different value, this may return null.
        To retrieve the single name of this section, that is, the final part of
        the path returned by this method, you may use getName().

        :return: Path of this section relative to its root
        """
        ...

    def getName(self) -> str:
        """
        Gets the name of this individual ConfigurationSection, in the
        path.
        This will always be the final part of getCurrentPath(), unless
        the section is orphaned.

        :return: Name of this section
        """
        ...

    def getRoot(self) -> Optional['Configuration']:
        """
        Gets the root Configuration that contains this ConfigurationSection
        For any Configuration themselves, this will return its own
        object.
        If the section is no longer contained within its root for any reason,
        such as being replaced with a different value, this may return null.

        :return: Root configuration containing this section.
        """
        ...

    def getParent(self) -> Optional['ConfigurationSection']:
        """
        Gets the parent ConfigurationSection that directly contains
        this ConfigurationSection.
        For any Configuration themselves, this will return null.
        If the section is no longer contained within its parent for any reason,
        such as being replaced with a different value, this may return null.

        :return: Parent section containing this section.
        """
        ...

    def get(self, path: str) -> Optional[object]:
        """
        Gets the requested Object by path.
        If the Object does not exist but a default value has been specified,
        this will return the default value. If the Object does not exist and no
        default value was specified, this will return null.

        :param path: Path of the Object to get.
        :return: Requested Object.
        """
        ...

    def get(self, path: str, defValue: Optional[object]) -> Optional[object]:
        """
        Gets the requested Object by path, returning a default value if not
        found.
        If the Object does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the Object to get.
        :param defValue: The default value to return if the path is not found.
        :return: Requested Object.
        """
        ...

    def set(self, path: str, value: Optional[object]) -> None:
        """
        Sets the specified path to the given value.
        If value is null, the entry will be removed. Any existing entry will be
        replaced, regardless of what the new value is.
        Some implementations may have limitations on what you may store. See
        their individual javadocs for details. No implementations should allow
        you to store Configuration or ConfigurationSections, please use
        createSection(java.lang.String) for that.

        :param path: Path of the object to set.
        :param value: New value to set the path to.
        """
        ...

    def createSection(self, path: str) -> 'ConfigurationSection':
        """
        Creates an empty ConfigurationSection at the specified path.
        Any value that was previously set at this path will be overwritten. If
        the previous value was itself a ConfigurationSection, it will
        be orphaned.

        :param path: Path to create the section at.
        :return: Newly created section
        """
        ...

    def createSection(self, path: str, map: Map) -> 'ConfigurationSection':
        """
        Creates a ConfigurationSection at the specified path, with
        specified values.
        Any value that was previously set at this path will be overwritten. If
        the previous value was itself a ConfigurationSection, it will
        be orphaned.

        :param path: Path to create the section at.
        :param map: The values to used.
        :return: Newly created section
        """
        ...

    # Primitives
    def getString(self, path: str) -> Optional[str]:
        """
        Gets the requested String by path.
        If the String does not exist but a default value has been specified,
        this will return the default value. If the String does not exist and no
        default value was specified, this will return null.

        :param path: Path of the String to get.
        :return: Requested String.
        """
        ...

    def getString(self, path: str, defValue: Optional[str]) -> Optional[str]:
        """
        Gets the requested String by path, returning a default value if not
        found.
        If the String does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the String to get.
        :param defValue: The default value to return if the path is not found or is
            not a String.
        :return: Requested String.
        """
        ...

    def isString(self, path: str) -> bool:
        """
        Checks if the specified path is a String.
        If the path exists but is not a String, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a String and return appropriately.

        :param path: Path of the String to check.
        :return: Whether or not the specified path is a String.
        """
        ...

    def getInt(self, path: str) -> int:
        """
        Gets the requested int by path.
        If the int does not exist but a default value has been specified, this
        will return the default value. If the int does not exist and no default
        value was specified, this will return 0.

        :param path: Path of the int to get.
        :return: Requested int.
        """
        ...

    def getInt(self, path: str, defValue: int) -> int:
        """
        Gets the requested int by path, returning a default value if not found.
        If the int does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the int to get.
        :param defValue: The default value to return if the path is not found or is
            not an int.
        :return: Requested int.
        """
        ...

    def isInt(self, path: str) -> bool:
        """
        Checks if the specified path is an int.
        If the path exists but is not a int, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a int and return appropriately.

        :param path: Path of the int to check.
        :return: Whether or not the specified path is an int.
        """
        ...

    def getBoolean(self, path: str) -> bool:
        """
        Gets the requested boolean by path.
        If the boolean does not exist but a default value has been specified,
        this will return the default value. If the boolean does not exist and
        no default value was specified, this will return false.

        :param path: Path of the boolean to get.
        :return: Requested boolean.
        """
        ...

    def getBoolean(self, path: str, defValue: bool) -> bool:
        """
        Gets the requested boolean by path, returning a default value if not
        found.
        If the boolean does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the boolean to get.
        :param defValue: The default value to return if the path is not found or is
            not a boolean.
        :return: Requested boolean.
        """
        ...

    def isBoolean(self, path: str) -> bool:
        """
        Checks if the specified path is a boolean.
        If the path exists but is not a boolean, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a boolean and return appropriately.

        :param path: Path of the boolean to check.
        :return: Whether or not the specified path is a boolean.
        """
        ...

    def getDouble(self, path: str) -> float:
        """
        Gets the requested double by path.
        If the double does not exist but a default value has been specified,
        this will return the default value. If the double does not exist and no
        default value was specified, this will return 0.

        :param path: Path of the double to get.
        :return: Requested double.
        """
        ...

    def getDouble(self, path: str, defValue: float) -> float:
        """
        Gets the requested double by path, returning a default value if not
        found.
        If the double does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the double to get.
        :param defValue: The default value to return if the path is not found or is
            not a double.
        :return: Requested double.
        """
        ...

    def isDouble(self, path: str) -> bool:
        """
        Checks if the specified path is a double.
        If the path exists but is not a double, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a double and return appropriately.

        :param path: Path of the double to check.
        :return: Whether or not the specified path is a double.
        """
        ...

    def getLong(self, path: str) -> int:
        """
        Gets the requested long by path.
        If the long does not exist but a default value has been specified, this
        will return the default value. If the long does not exist and no
        default value was specified, this will return 0.

        :param path: Path of the long to get.
        :return: Requested long.
        """
        ...

    def getLong(self, path: str, defValue: int) -> int:
        """
        Gets the requested long by path, returning a default value if not
        found.
        If the long does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the long to get.
        :param defValue: The default value to return if the path is not found or is
            not a long.
        :return: Requested long.
        """
        ...

    def isLong(self, path: str) -> bool:
        """
        Checks if the specified path is a long.
        If the path exists but is not a long, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a long and return appropriately.

        :param path: Path of the long to check.
        :return: Whether or not the specified path is a long.
        """
        ...

    # Java
    def getList(self, path: str) -> Optional[List[object]]:
        """
        Gets the requested List by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return null.

        :param path: Path of the List to get.
        :return: Requested List.
        """
        ...

    def getList(self, path: str, defValue: Optional[List[object]]) -> Optional[List[object]]:
        """
        Gets the requested List by path, returning a default value if not
        found.
        If the List does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the List to get.
        :param defValue: The default value to return if the path is not found or is
            not a List.
        :return: Requested List.
        """
        ...

    def isList(self, path: str) -> bool:
        """
        Checks if the specified path is a List.
        If the path exists but is not a List, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a List and return appropriately.

        :param path: Path of the List to check.
        :return: Whether or not the specified path is a List.
        """
        ...

    def getStringList(self, path: str) -> List[str]:
        """
        Gets the requested List of String by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a String if possible,
        but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of String.
        """
        ...

    def getIntegerList(self, path: str) -> List[int]:
        """
        Gets the requested List of Integer by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Integer if possible,
        but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Integer.
        """
        ...

    def getBooleanList(self, path: str) -> List[bool]:
        """
        Gets the requested List of Boolean by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Boolean if possible,
        but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Boolean.
        """
        ...

    def getDoubleList(self, path: str) -> List[float]:
        """
        Gets the requested List of Double by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Double if possible,
        but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Double.
        """
        ...

    def getFloatList(self, path: str) -> List[float]:
        """
        Gets the requested List of Float by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Float if possible,
        but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Float.
        """
        ...

    def getLongList(self, path: str) -> List[int]:
        """
        Gets the requested List of Long by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Long if possible,
        but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Long.
        """
        ...

    def getByteList(self, path: str) -> List[bytes]:
        """
        Gets the requested List of Byte by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Byte if possible,
        but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Byte.
        """
        ...

    def getCharacterList(self, path: str) -> List[str]:
        """
        Gets the requested List of Character by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Character if
        possible, but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Character.
        """
        ...

    def getShortList(self, path: str) -> List[int]:
        """
        Gets the requested List of Short by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Short if possible,
        but may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Short.
        """
        ...

    def getMapList(self, path: str) -> List[Map]:
        """
        Gets the requested List of Maps by path.
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        This method will attempt to cast any values into a Map if possible, but
        may miss any values out if they are not compatible.

        :param path: Path of the List to get.
        :return: Requested List of Maps.
        """
        ...

    # Bukkit
    def getObject(self, path: str, clazz: type[T]) -> Optional[T]:
        """
        Gets the requested object at the given path.
        If the Object does not exist but a default value has been specified, this
        will return the default value. If the Object does not exist and no
        default value was specified, this will return null.

        :param path: the path to the object.
        :param clazz: the type of the requested object
        :return: Requested object
        """
        ...

    def getObject(self, path: str, clazz: type[T], defValue: Optional[T]) -> Optional[T]:
        """
        Gets the requested object at the given path, returning a default value if
        not found
        If the Object does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: the path to the object.
        :param clazz: the type of the requested object
        :param defValue: the default object to return if the object is not present at
            the path
        :return: Requested object
        """
        ...

    def getSerializable(self, path: str, clazz: type[ConfigurationSerializable]) -> Optional[ConfigurationSerializable]:
        """
        Gets the requested ConfigurationSerializable object at the given
        path.
        If the Object does not exist but a default value has been specified, this
        will return the default value. If the Object does not exist and no
        default value was specified, this will return null.

        :param path: the path to the object.
        :param clazz: the type of ConfigurationSerializable
        :return: Requested ConfigurationSerializable object
        """
        ...

    def getSerializable(self, path: str, clazz: type[ConfigurationSerializable], defValue: Optional[ConfigurationSerializable]) -> Optional[ConfigurationSerializable]:
        """
        Gets the requested ConfigurationSerializable object at the given
        path, returning a default value if not found
        If the Object does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: the path to the object.
        :param clazz: the type of ConfigurationSerializable
        :param defValue: the default object to return if the object is not present at
            the path
        :return: Requested ConfigurationSerializable object
        """
        ...

    def getVector(self, path: str) -> Optional['Vector']:
        """
        Gets the requested Vector by path.
        If the Vector does not exist but a default value has been specified,
        this will return the default value. If the Vector does not exist and no
        default value was specified, this will return null.

        :param path: Path of the Vector to get.
        :return: Requested Vector.
        """
        ...

    def getVector(self, path: str, defValue: Optional['Vector']) -> Optional['Vector']:
        """
        Gets the requested Vector by path, returning a default value if not
        found.
        If the Vector does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the Vector to get.
        :param defValue: The default value to return if the path is not found or is
            not a Vector.
        :return: Requested Vector.
        """
        ...

    def isVector(self, path: str) -> bool:
        """
        Checks if the specified path is a Vector.
        If the path exists but is not a Vector, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a Vector and return appropriately.

        :param path: Path of the Vector to check.
        :return: Whether or not the specified path is a Vector.
        """
        ...

    def getOfflinePlayer(self, path: str) -> Optional['OfflinePlayer']:
        """
        Gets the requested OfflinePlayer by path.
        If the OfflinePlayer does not exist but a default value has been
        specified, this will return the default value. If the OfflinePlayer
        does not exist and no default value was specified, this will return
        null.

        :param path: Path of the OfflinePlayer to get.
        :return: Requested OfflinePlayer.
        """
        ...

    def getOfflinePlayer(self, path: str, defValue: Optional['OfflinePlayer']) -> Optional['OfflinePlayer']:
        """
        Gets the requested OfflinePlayer by path, returning a default
        value if not found.
        If the OfflinePlayer does not exist then the specified default value
        will returned regardless of if a default has been identified in the
        root Configuration.

        :param path: Path of the OfflinePlayer to get.
        :param defValue: The default value to return if the path is not found or is
            not an OfflinePlayer.
        :return: Requested OfflinePlayer.
        """
        ...

    def isOfflinePlayer(self, path: str) -> bool:
        """
        Checks if the specified path is an OfflinePlayer.
        If the path exists but is not a OfflinePlayer, this will return false.
        If the path does not exist, this will return false. If the path does
        not exist but a default value has been specified, this will check if
        that default value is a OfflinePlayer and return appropriately.

        :param path: Path of the OfflinePlayer to check.
        :return: Whether or not the specified path is an OfflinePlayer.
        """
        ...

    def getItemStack(self, path: str) -> Optional['ItemStack']:
        """
        Gets the requested ItemStack by path.
        If the ItemStack does not exist but a default value has been specified,
        this will return the default value. If the ItemStack does not exist and
        no default value was specified, this will return null.

        :param path: Path of the ItemStack to get.
        :return: Requested ItemStack.
        """
        ...

    def getItemStack(self, path: str, defValue: Optional['ItemStack']) -> Optional['ItemStack']:
        """
        Gets the requested ItemStack by path, returning a default value
        if not found.
        If the ItemStack does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the ItemStack to get.
        :param defValue: The default value to return if the path is not found or is
            not an ItemStack.
        :return: Requested ItemStack.
        """
        ...

    def isItemStack(self, path: str) -> bool:
        """
        Checks if the specified path is an ItemStack.
        If the path exists but is not a ItemStack, this will return false. If
        the path does not exist, this will return false. If the path does not
        exist but a default value has been specified, this will check if that
        default value is an ItemStack and return appropriately.

        :param path: Path of the ItemStack to check.
        :return: Whether or not the specified path is an ItemStack.
        """
        ...

    def getColor(self, path: str) -> Optional['Color']:
        """
        Gets the requested Color by path.
        If the Color does not exist but a default value has been specified,
        this will return the default value. If the Color does not exist and no
        default value was specified, this will return null.

        :param path: Path of the Color to get.
        :return: Requested Color.
        """
        ...

    def getColor(self, path: str, defValue: Optional['Color']) -> Optional['Color']:
        """
        Gets the requested Color by path, returning a default value if
        not found.
        If the Color does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the Color to get.
        :param defValue: The default value to return if the path is not found or is
            not a Color.
        :return: Requested Color.
        """
        ...

    def isColor(self, path: str) -> bool:
        """
        Checks if the specified path is a Color.
        If the path exists but is not a Color, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a Color and return appropriately.

        :param path: Path of the Color to check.
        :return: Whether or not the specified path is a Color.
        """
        ...

    def getLocation(self, path: str) -> Optional['Location']:
        """
        Gets the requested Location by path.
        If the Location does not exist but a default value has been specified,
        this will return the default value. If the Location does not exist and no
        default value was specified, this will return null.

        :param path: Path of the Location to get.
        :return: Requested Location.
        """
        ...

    def getLocation(self, path: str, defValue: Optional['Location']) -> Optional['Location']:
        """
        Gets the requested Location by path, returning a default value if
        not found.
        If the Location does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        :param path: Path of the Location to get.
        :param defValue: The default value to return if the path is not found or is
            not a Location.
        :return: Requested Location.
        """
        ...

    def isLocation(self, path: str) -> bool:
        """
        Checks if the specified path is a Location.
        If the path exists but is not a Location, this will return false. If the
        path does not exist, this will return false. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a Location and return appropriately.

        :param path: Path of the Location to check.
        :return: Whether or not the specified path is a Location.
        """
        ...

    def getConfigurationSection(self, path: str) -> Optional['ConfigurationSection']:
        """
        Gets the requested ConfigurationSection by path.
        If the ConfigurationSection does not exist but a default value has been
        specified, this will return the default value. If the
        ConfigurationSection does not exist and no default value was specified,
        this will return null.

        :param path: Path of the ConfigurationSection to get.
        :return: Requested ConfigurationSection.
        """
        ...

    def isConfigurationSection(self, path: str) -> bool:
        """
        Checks if the specified path is a ConfigurationSection.
        If the path exists but is not a ConfigurationSection, this will return
        false. If the path does not exist, this will return false. If the path
        does not exist but a default value has been specified, this will check
        if that default value is a ConfigurationSection and return
        appropriately.

        :param path: Path of the ConfigurationSection to check.
        :return: Whether or not the specified path is a ConfigurationSection.
        """
        ...

    def getDefaultSection(self) -> Optional['ConfigurationSection']:
        """
        Gets the equivalent ConfigurationSection from the default
        Configuration defined in getRoot().
        If the root contains no defaults, or the defaults doesn't contain a
        value for this path, or the value at this path is not a ConfigurationSection
        then this will return null.

        :return: Equivalent section in root configuration
        """
        ...

    def addDefault(self, path: str, value: Optional[object]) -> None:
        """
        Sets the default value in the root at the given path as provided.
        If no source Configuration was provided as a default
        collection, then a new MemoryConfiguration will be created to
        hold the new default value.
        If value is null, the value will be removed from the default
        Configuration source.
        If the value as returned by getDefaultSection() is null, then
        this will create a new section at the path, replacing anything that may
        have existed there previously.

        :param path: Path of the value to set.
        :param value: Value to set the default to.
        :raises ValueError: Thrown if path is null.
        """
        ...

    def getComments(self, path: str) -> List[str]:
        """
        Gets the requested comment list by path.
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.

        :param path: Path of the comments to get.
        :return: A unmodifiable list of the requested comments, every entry
            represents one line.
        """
        ...

    def getInlineComments(self, path: str) -> List[str]:
        """
        Gets the requested inline comment list by path.
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.

        :param path: Path of the comments to get.
        :return: A unmodifiable list of the requested comments, every entry
            represents one line.
        """
        ...

    def setComments(self, path: str, comments: Optional[List[str]]) -> None:
        """
        Sets the comment list at the specified path.
        If value is null, the comments will be removed. A null entry is an empty
        line and an empty String entry is an empty comment line. If the path does
        not exist, no comments will be set. Any existing comments will be
        replaced, regardless of what the new comments are.
        Some implementations may have limitations on what persists. See their
        individual javadocs for details.

        :param path: Path of the comments to set.
        :param comments: New comments to set at the path, every entry represents
            one line.
        """
        ...

    def setInlineComments(self, path: str, comments: Optional[List[str]]) -> None:
        """
        Sets the inline comment list at the specified path.
        If value is null, the comments will be removed. A null entry is an empty
        line and an empty String entry is an empty comment line. If the path does
        not exist, no comment will be set. Any existing comments will be
        replaced, regardless of what the new comments are.
        Some implementations may have limitations on what persists. See their
        individual javadocs for details.

        :param path: Path of the comments to set.
        :param comments: New comments to set at the path, every entry represents
            one line.
        """
        ...