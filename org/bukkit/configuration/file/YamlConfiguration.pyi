from typing import List, Dict, Any, Optional
from org.bukkit.configuration import Configuration, ConfigurationSection, InvalidConfigurationException
from org.bukkit.configuration.serialization import ConfigurationSerialization
from org.yaml.snakeyaml import DumperOptions, LoaderOptions, Yaml
from org.yaml.snakeyaml.comments import CommentLine, CommentType
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.nodes import AnchorNode, MappingNode, Node, NodeTuple, ScalarNode, SequenceNode, Tag
from org.yaml.snakeyaml.reader import UnicodeReader
from java.io import ByteArrayInputStream, File, Reader
from java.io import FileNotFoundException, IOException
from java.lang import String
import java.util.logging.Level
import com.google.common.base.Preconditions

class YamlConfiguration(Configuration):
    """
    An implementation of {@link Configuration} which saves all files in Yaml.
    Note that this implementation is not synchronized.
    """
    
    @Deprecated(since="1.18.1")
    COMMENT_PREFIX: str
    @Deprecated(since="1.18.1")
    BLANK_CONFIG: str

    def __init__(self) -> None:
        ...
    
    def saveToString(self) -> str:
        """
        @return: The YAML string representation of this configuration.
        """
        ...
    
    def loadFromString(self, contents: str) -> None:
        """
        @param contents: The string to load.
        @throws InvalidConfigurationException: If the contents cannot be parsed.
        """
        ...
    
    def adjustNodeComments(self, node: MappingNode) -> None:
        """
        This method splits the header on the last empty line, and sets the
        comments below this line as comments for the first key on the map object.
        
        @param node: The root node of the yaml object
        """
        ...
    
    def fromNodeTree(self, input: MappingNode, section: ConfigurationSection) -> None:
        ...
    
    def hasSerializedTypeKey(self, node: MappingNode) -> bool:
        ...
    
    def toNodeTree(self, section: ConfigurationSection) -> MappingNode:
        ...
    
    def getCommentLines(self, comments: List[CommentLine]) -> List[str]:
        ...
    
    def getCommentLines(self, comments: List[str], commentType: CommentType) -> List[CommentLine]:
        ...
    
    def loadHeader(self, header: List[str]) -> List[str]:
        """
        Removes the empty line at the end of the header that separates the header
        from further comments. Also removes all empty header starts (backwards
        compat).
        
        @param header: The list of heading comments
        @return: The modified list
        """
        ...
    
    def saveHeader(self, header: List[str]) -> List[str]:
        """
        Adds the empty line at the end of the header that separates the header
        from further comments.
        
        @param header: The list of heading comments
        @return: The modified list
        """
        ...
    
    def options(self) -> 'YamlConfigurationOptions':
        """
        @return: The options for this configuration.
        """
        ...
    
    @staticmethod
    def loadConfiguration(file: File) -> 'YamlConfiguration':
        """
        Creates a new {@link YamlConfiguration}, loading from the given file.
        <p>
        Any errors loading the Configuration will be logged and then ignored.
        If the specified input is not a valid config, a blank config will be
        returned.
        <p>
        The encoding used may follow the system dependent default.
        
        @param file: Input file
        @return: Resulting configuration
        @throws IllegalArgumentException: Thrown if file is null
        """
        ...
    
    @staticmethod
    def loadConfiguration(reader: Reader) -> 'YamlConfiguration':
        """
        Creates a new {@link YamlConfiguration}, loading from the given reader.
        <p>
        Any errors loading the Configuration will be logged and then ignored.
        If the specified input is not a valid config, a blank config will be
        returned.
        
        @param reader: input
        @return: resulting configuration
        @throws IllegalArgumentException: Thrown if stream is null
        """
        ...