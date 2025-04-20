from typing import List, Optional
from org.bukkit.configuration.file import FileConfigurationOptions
from org.jetbrains.annotations import NotNull, Nullable

class YamlConfigurationOptions(FileConfigurationOptions):
    """
    Various settings for controlling the input and output of a {@link
    YamlConfiguration}
    """

    def __init__(self, configuration: 'YamlConfiguration') -> None:
        super().__init__(configuration)

        def configuration(self) -> 'YamlConfiguration':
        ...

        def copy_defaults(self, value: bool) -> 'YamlConfigurationOptions':
        ...

        def path_separator(self, value: str) -> 'YamlConfigurationOptions':
        ...

        def set_header(self, value: Optional[List[str]]) -> 'YamlConfigurationOptions':
        ...

        @Deprecated(since="1.18.1")
    def header(self, value: Optional[str]) -> 'YamlConfigurationOptions':
        ...

        def set_footer(self, value: Optional[List[str]]) -> 'YamlConfigurationOptions':
        ...

        def parse_comments(self, value: bool) -> 'YamlConfigurationOptions':
        ...

        @Deprecated(since="1.18.1")
    def copy_header(self, value: bool) -> 'YamlConfigurationOptions':
        ...

    def indent(self) -> int:
        """
        Gets how much spaces should be used to indent each line.
        <p>
        The minimum value this may be is 2, and the maximum is 9.
        @return How much to indent by
        """
        ...

        def indent(self, value: int) -> 'YamlConfigurationOptions':
        """
        Sets how much spaces should be used to indent each line.
        <p>
        The minimum value this may be is 2, and the maximum is 9.
        @param value New indent
        @return This object, for chaining
        """
        ...

    def width(self) -> int:
        """
        Gets how long a line can be, before it gets split.
        @return How the max line width
        """
        ...

        def width(self, value: int) -> 'YamlConfigurationOptions':
        """
        Sets how long a line can be, before it gets split.
        @param value New width
        @return This object, for chaining
        """
        ...