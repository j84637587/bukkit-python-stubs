from typing import Any

class MetadataConversionException(RuntimeError):
    """
    A MetadataConversionException is thrown any time a {@link
    LazyMetadataValue} attempts to convert a metadata value to an inappropriate
    data type.
    """
    
    def __init__(self, message: str) -> None:
        ...