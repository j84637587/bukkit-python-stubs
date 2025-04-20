from org.bukkit.configuration import Configuration
from typing import Any

class ConfigurationOptions:
    """
    Various settings for controlling the input and output of a {@link
    Configuration}
    """

    def __init__(self, configuration: Configuration) -> None:
        """
        Initializes ConfigurationOptions with the given configuration.

        :param configuration: The configuration to associate with this options object.
        """
        ...

    def configuration(self) -> Configuration:
        """
        Returns the {@link Configuration} that this object is responsible for.

        :return: Parent configuration
        """
        ...

    def path_separator(self) -> str:
        """
        Gets the char that will be used to separate {@link
        ConfigurationSection}s
        <p>
        This value does not affect how the {@link Configuration} is stored,
        only in how you access the data. The default value is '.'.

        :return: Path separator
        """
        ...

    def path_separator(self, value: str) -> 'ConfigurationOptions':
        """
        Sets the char that will be used to separate {@link
        ConfigurationSection}s
        <p>
        This value does not affect how the {@link Configuration} is stored,
        only in how you access the data. The default value is '.'.

        :param value: Path separator
        :return: This object, for chaining
        """
        ...

    def copy_defaults(self) -> bool:
        """
        Checks if the {@link Configuration} should copy values from its default
        {@link Configuration} directly.
        <p>
        If this is true, all values in the default Configuration will be
        directly copied, making it impossible to distinguish between values
        that were set and values that are provided by default. As a result,
        {@link ConfigurationSection#contains(java.lang.String)} will always
        return the same value as {@link
        ConfigurationSection#isSet(java.lang.String)}. The default value is
        false.

        :return: Whether or not defaults are directly copied
        """
        ...

    def copy_defaults(self, value: bool) -> 'ConfigurationOptions':
        """
        Sets if the {@link Configuration} should copy values from its default
        {@link Configuration} directly.
        <p>
        If this is true, all values in the default Configuration will be
        directly copied, making it impossible to distinguish between values
        that were set and values that are provided by default. As a result,
        {@link ConfigurationSection#contains(java.lang.String)} will always
        return the same value as {@link
        ConfigurationSection#isSet(java.lang.String)}. The default value is
        false.

        :param value: Whether or not defaults are directly copied
        :return: This object, for chaining
        """
        ...