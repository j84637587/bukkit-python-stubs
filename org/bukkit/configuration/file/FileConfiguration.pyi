from typing import Optional, Union
from pathlib import Path
from org.bukkit.configuration import Configuration
from org.bukkit.configuration import InvalidConfigurationException
from org.bukkit.configuration import MemoryConfiguration

class FileConfiguration(MemoryConfiguration):
    """
    This is a base class for all File based implementations of {@link
    Configuration}
    """

    def __init__(self, defaults: Optional[Configuration] = None) -> None:
        """
        Creates an empty {@link FileConfiguration} using the specified {@link
        Configuration} as a source for all default values.

        :param defaults: Default value provider
        """
        super().__init__(defaults)

    def save(self, file: Path) -> None:
        """
        Saves this {@link FileConfiguration} to the specified location.
        If the file does not exist, it will be created. If already exists, it
        will be overwritten. If it cannot be overwritten or created, an
        exception will be thrown.
        This method will save using the system default encoding, or possibly
        using UTF8.

        :param file: File to save to.
        :raises IOError: Thrown when the given file cannot be written to for
            any reason.
        :raises ValueError: Thrown when file is null.
        """
        ...

    def save(self, file: str) -> None:
        """
        Saves this {@link FileConfiguration} to the specified location.
        If the file does not exist, it will be created. If already exists, it
        will be overwritten. If it cannot be overwritten or created, an
        exception will be thrown.
        This method will save using the system default encoding, or possibly
        using UTF8.

        :param file: File to save to.
        :raises IOError: Thrown when the given file cannot be written to for
            any reason.
        :raises ValueError: Thrown when file is null.
        """
        ...

    def saveToString(self) -> str:
        """
        Saves this {@link FileConfiguration} to a string, and returns it.

        :return: String containing this configuration.
        """
        ...

    def load(self, file: Path) -> None:
        """
        Loads this {@link FileConfiguration} from the specified location.
        All the values contained within this configuration will be removed,
        leaving only settings and defaults, and the new values will be loaded
        from the given file.
        If the file cannot be loaded for any reason, an exception will be
        thrown.

        :param file: File to load from.
        :raises FileNotFoundError: Thrown when the given file cannot be
            opened.
        :raises IOError: Thrown when the given file cannot be read.
        :raises InvalidConfigurationException: Thrown when the given file is not
            a valid Configuration.
        :raises ValueError: Thrown when file is null.
        """
        ...

    def load(self, reader: 'Reader') -> None:
        """
        Loads this {@link FileConfiguration} from the specified reader.
        All the values contained within this configuration will be removed,
        leaving only settings and defaults, and the new values will be loaded
        from the given stream.

        :param reader: the reader to load from
        :raises IOError: thrown when underlying reader throws an IOError
        :raises InvalidConfigurationException: thrown when the reader does not
            represent a valid Configuration
        :raises ValueError: thrown when reader is null
        """
        ...

    def load(self, file: str) -> None:
        """
        Loads this {@link FileConfiguration} from the specified location.
        All the values contained within this configuration will be removed,
        leaving only settings and defaults, and the new values will be loaded
        from the given file.
        If the file cannot be loaded for any reason, an exception will be
        thrown.

        :param file: File to load from.
        :raises FileNotFoundError: Thrown when the given file cannot be
            opened.
        :raises IOError: Thrown when the given file cannot be read.
        :raises InvalidConfigurationException: Thrown when the given file is not
            a valid Configuration.
        :raises ValueError: Thrown when file is null.
        """
        ...

    def loadFromString(self, contents: str) -> None:
        """
        Loads this {@link FileConfiguration} from the specified string, as
        opposed to from file.
        All the values contained within this configuration will be removed,
        leaving only settings and defaults, and the new values will be loaded
        from the given string.
        If the string is invalid in any way, an exception will be thrown.

        :param contents: Contents of a Configuration to load.
        :raises InvalidConfigurationException: Thrown if the specified string is
            invalid.
        :raises ValueError: Thrown if contents is null.
        """
        ...

    def buildHeader(self) -> str:
        """
        @return: empty string

        @deprecated: This method only exists for backwards compatibility. It will
        do nothing and should not be used! Please use
        {@link FileConfigurationOptions#getHeader()} instead.
        """
        ...

    def options(self) -> 'FileConfigurationOptions':
        """
        :return: FileConfigurationOptions
        """
        ...