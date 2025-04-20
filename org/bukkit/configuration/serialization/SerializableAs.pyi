from typing import Callable, TypeVar

T = TypeVar('T')

class SerializableAs:
    """
    Represents an "alias" that a ConfigurationSerializable may be
    stored as.
    If this is not present on a ConfigurationSerializable class, it
    will use the fully qualified name of the class.
    <p>
    This value will be stored in the configuration so that the configuration
    deserialization can determine what type it is.
    <p>
    Using this annotation on any other class than a
    ConfigurationSerializable will have no effect.
    
    @see ConfigurationSerialization#registerClass(Class, String)
    """

    def __init__(self, value: str) -> None:
        """
        This is the name your class will be stored and retrieved as.
        <p>
        This name MUST be unique. We recommend using names such as
        "MyPluginThing" instead of "Thing".
        
        @return Name to serialize the class as.
        """
        ...

    value: str