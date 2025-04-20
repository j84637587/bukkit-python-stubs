from typing import Any, Dict, Optional
from org.bukkit.configuration.serialization import ConfigurationSerialization
from org.yaml.snakeyaml.LoaderOptions import LoaderOptions
from org.yaml.snakeyaml.constructor import SafeConstructor
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.nodes import MappingNode, Node, Tag


class YamlConstructor(SafeConstructor):
    """
    YamlConstructor is a custom YAML constructor that extends SafeConstructor.
    
    @deprecated options required
    """
    
    def __init__(self) -> None:
        """
        Initializes a new instance of YamlConstructor with default LoaderOptions.
        """
        ...

    def __init__(self, loader_options: LoaderOptions) -> None:
        """
        Initializes a new instance of YamlConstructor with specified LoaderOptions.
        
        :param loader_options: The LoaderOptions to use.
        """
        ...

    def flatten_mapping(self, node: MappingNode) -> None:
        """
        Flattens the given mapping node.
        
        :param node: The mapping node to flatten.
        """
        ...

    def construct(self, node: Node) -> Optional[Any]:
        """
        Constructs an object from the given node.
        
        :param node: The node to construct from.
        :return: The constructed object, or None.
        """
        ...

    class ConstructCustomObject:
        """
        A custom object constructor for YAML maps.
        """

        def construct(self, node: Node) -> Optional[Any]:
            """
            Constructs an object from the given node.
            
            :param node: The node to construct from.
            :return: The constructed object, or None.
            :raises YAMLException: If the node has an unexpected referential mapping structure.
            """
            ...

        def construct2nd_step(self, node: Node, object: Any) -> None:
            """
            Performs the second step of construction for the given node and object.
            
            :param node: The node to construct from.
            :param object: The object to construct into.
            :raises YAMLException: If the node has an unexpected referential mapping structure.
            """
            ...