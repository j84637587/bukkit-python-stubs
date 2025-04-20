from typing import Type, Dict, Any, Optional, Callable
import logging

class ConfigurationSerializable:
    pass

class ConfigurationSerialization:
    SERIALIZED_TYPE_KEY: str = "=="
    aliases: Dict[str, Type[ConfigurationSerializable]] = {}

    def __init__(self, clazz: Type[ConfigurationSerializable]) -> None:
        """Utility class for storing and retrieving classes for Configuration."""
        self.clazz = clazz

    def get_method(self, name: str, is_static: bool) -> Optional[Callable]:
        """Get a method by name."""
        ...

    def get_constructor(self) -> Optional[Callable]:
        """Get the constructor for the class."""
        ...

    def deserialize_via_method(self, method: Callable, args: Dict[str, Any]) -> Optional[ConfigurationSerializable]:
        """Deserialize using a method."""
        ...

    def deserialize_via_ctor(self, ctor: Callable, args: Dict[str, Any]) -> Optional[ConfigurationSerializable]:
        """Deserialize using a constructor."""
        ...

    def deserialize(self, args: Dict[str, Any]) -> Optional[ConfigurationSerializable]:
        """Deserialize the given arguments into a new instance of the class."""
        ...

    @staticmethod
    def deserialize_object(args: Dict[str, Any], clazz: Type[ConfigurationSerializable]) -> Optional[ConfigurationSerializable]:
        """Attempts to deserialize the given arguments into a new instance of the given class."""
        ...

    @staticmethod
    def deserialize_object(args: Dict[str, Any]) -> Optional[ConfigurationSerializable]:
        """Attempts to deserialize the given arguments into a new instance of the given class."""
        ...

    @staticmethod
    def register_class(clazz: Type[ConfigurationSerializable]) -> None:
        """Registers the given ConfigurationSerializable class by its alias."""
        ...

    @staticmethod
    def register_class(clazz: Type[ConfigurationSerializable], alias: str) -> None:
        """Registers the given alias to the specified ConfigurationSerializable class."""
        ...

    @staticmethod
    def unregister_class(alias: str) -> None:
        """Unregisters the specified alias to a ConfigurationSerializable."""
        ...

    @staticmethod
    def unregister_class(clazz: Type[ConfigurationSerializable]) -> None:
        """Unregisters any aliases for the specified ConfigurationSerializable class."""
        ...

    @staticmethod
    def get_class_by_alias(alias: str) -> Optional[Type[ConfigurationSerializable]]:
        """Attempts to get a registered ConfigurationSerializable class by its alias."""
        ...

    @staticmethod
    def get_alias(clazz: Type[ConfigurationSerializable]) -> str:
        """Gets the correct alias for the given ConfigurationSerializable class."""
        ...