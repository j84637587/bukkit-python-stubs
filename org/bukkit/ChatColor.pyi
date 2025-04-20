from typing import Dict, Optional, Union

class ChatColor:
    """
    All supported color values for chat
    """

    BLACK = 0x00
    DARK_BLUE = 0x1
    DARK_GREEN = 0x2
    DARK_AQUA = 0x3
    DARK_RED = 0x4
    DARK_PURPLE = 0x5
    GOLD = 0x6
    GRAY = 0x7
    DARK_GRAY = 0x8
    BLUE = 0x9
    GREEN = 0xA
    AQUA = 0xB
    RED = 0xC
    LIGHT_PURPLE = 0xD
    YELLOW = 0xE
    WHITE = 0xF
    MAGIC = 0x10
    BOLD = 0x11
    STRIKETHROUGH = 0x12
    UNDERLINE = 0x13
    ITALIC = 0x14
    RESET = 0x15

    COLOR_CHAR: str
    STRIP_COLOR_PATTERN: str
    intCode: int
    code: str
    isFormat: bool
    toString: str
    BY_ID: Dict[int, "ChatColor"]
    BY_CHAR: Dict[str, "ChatColor"]

    def getChar(self) -> str:
        """
        Gets the char value associated with this color

        @return A char value of this color code
        """
        ...

    def __str__(self) -> str: ...
    def isFormat(self) -> bool:
        """
        Checks if this code is a format code as opposed to a color code.

        @return whether this ChatColor is a format code
        """
        ...

    def isColor(self) -> bool:
        """
        Checks if this code is a color code as opposed to a format code.

        @return whether this ChatColor is a color code
        """
        ...

    @staticmethod
    def getByChar(code: Union[str, str]) -> Optional["ChatColor"]:
        """
        Gets the color represented by the specified color code

        @param code Code to check
        @return Associative {@link org.bukkit.ChatColor} with the given code,
            or null if it doesn't exist
        """
        ...

    @staticmethod
    def stripColor(input: Optional[str]) -> Optional[str]:
        """
        Strips the given message of all color codes

        @param input String to strip of color
        @return A copy of the input string, without any coloring
        """
        ...

    @staticmethod
    def translateAlternateColorCodes(altColorChar: str, textToTranslate: str) -> str:
        """
        Translates a string using an alternate color code character into a
        string that uses the internal ChatColor.COLOR_CODE color code
        character. The alternate color code character will only be replaced if
        it is immediately followed by 0-9, A-F, a-f, K-O, k-o, R or r.

        @param altColorChar The alternate color code character to replace. Ex: {@literal &}
        @param textToTranslate Text containing the alternate color code character.
        @return Text containing the ChatColor.COLOR_CODE color code character.
        """
        ...

    @staticmethod
    def getLastColors(input: str) -> str:
        """
        Gets the ChatColors used at the end of the given input string.

        @param input Input string to retrieve the colors from.
        @return Any remaining ChatColors to pass onto the next line.
        """
        ...

    @staticmethod
    def getHexColor(input: str, index: int) -> Optional[str]: ...
