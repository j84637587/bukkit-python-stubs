from typing import Dict, Type
from org.bukkit.configuration import ConfigurationSection
from org.bukkit.configuration.serialization import ConfigurationSerializable, ConfigurationSerialization
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.representer import Representer


class YamlRepresenter(Representer):
    """
    Represents a YAML representer.
    """

    def __init__(self) -> None:
        """
        @deprecated options required
        """
        ...

    def __init__(self, options: DumperOptions) -> None:
        """
        Initializes the YamlRepresenter with the given DumperOptions.
        """
        ...

    class RepresentConfigurationSection(RepresentMap):
        """
        Represents a configuration section.
        """

        def representData(self, data: object) -> Node:
            """
            Represents the data of the configuration section.
            """
            ...

    class RepresentConfigurationSerializable(RepresentMap):
        """
        Represents a configuration serializable object.
        """

        def representData(self, data: object) -> Node:
            """
            Represents the data of the configuration serializable object.
            """
            ...