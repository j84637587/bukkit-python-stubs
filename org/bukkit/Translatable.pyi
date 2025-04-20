from typing import Protocol

class Translatable(Protocol):
    """
    Represents an object with a text representation that can be translated by the
    Minecraft client.
    """

    def getTranslationKey() -> str:
        """
        Get the translation key, suitable for use in a translation component.

        :return: the translation key
        """