from typing import List, Optional
from org.bukkit.configuration import MemoryConfiguration, MemoryConfigurationOptions

class FileConfigurationOptions(MemoryConfigurationOptions):
    """
    Various settings for controlling the input and output of a {@link
    FileConfiguration}
    """

    def __init__(self, configuration: MemoryConfiguration) -> None:
        ...

    def configuration(self) -> 'FileConfiguration':
        ...

    def copy_defaults(self, value: bool) -> 'FileConfigurationOptions':
        ...

    def path_separator(self, value: str) -> 'FileConfigurationOptions':
        ...

    def get_header(self) -> List[str]:
        """
        Gets the header that will be applied to the top of the saved output.
        <p>
        This header will be commented out and applied directly at the top of
        the generated output of the {@link FileConfiguration}. It is not
        required to include a newline at the end of the header as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        <p>
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.
        @return Unmodifiable header, every entry represents one line.
        """
        ...

    @Deprecated(since="1.18.1")
    def header(self) -> str:
        """
        @return The string header.
        @deprecated use getHeader() instead.
        """
        ...

    def set_header(self, value: Optional[List[str]]) -> 'FileConfigurationOptions':
        """
        Sets the header that will be applied to the top of the saved output.
        <p>
        This header will be commented out and applied directly at the top of
        the generated output of the {@link FileConfiguration}. It is not
        required to include a newline at the end of the header as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        <p>
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.
        @param value New header, every entry represents one line.
        @return This object, for chaining
        """
        ...

    @Deprecated(since="1.18.1")
    def copy_header(self) -> bool:
        """
        @return Whether or not comments are parsed.
        @deprecated Call {@link #parseComments()} instead.
        """
        ...

    @Deprecated(since="1.18.1")
    def copy_header(self, value: bool) -> 'FileConfigurationOptions':
        """
        @param value Should comments be parsed.
        @return This object, for chaining
        @deprecated Call {@link #parseComments(boolean)} instead.
        """
        ...

    def get_footer(self) -> List[str]:
        """
        Gets the footer that will be applied to the bottom of the saved output.
        <p>
        This footer will be commented out and applied directly at the bottom of
        the generated output of the {@link FileConfiguration}. It is not required
        to include a newline at the beginning of the footer as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        <p>
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.
        @return Unmodifiable footer, every entry represents one line.
        """
        ...

    def set_footer(self, value: Optional[List[str]]) -> 'FileConfigurationOptions':
        """
        Sets the footer that will be applied to the bottom of the saved output.
        <p>
        This footer will be commented out and applied directly at the bottom of
        the generated output of the {@link FileConfiguration}. It is not required
        to include a newline at the beginning of the footer as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        <p>
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.
        @param value New footer, every entry represents one line.
        @return This object, for chaining
        """
        ...

    def parse_comments(self) -> bool:
        """
        Gets whether or not comments should be loaded and saved.
        <p>
        Defaults to true.
        @return Whether or not comments are parsed.
        """
        ...

    def parse_comments(self, value: bool) -> 'MemoryConfigurationOptions':
        """
        Sets whether or not comments should be loaded and saved.
        <p>
        Defaults to true.
        @param value Whether or not comments are parsed.
        @return This object, for chaining
        """
        ...