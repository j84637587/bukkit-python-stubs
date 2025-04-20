from typing import Set

class PluginAwareness:
    """
    Represents a concept that a plugin is aware of.
    The internal representation may be singleton, or be a parameterized
    instance, but must be immutable.
    """

    class Flags(PluginAwareness):
        """
        Each entry here represents a particular plugin's awareness. These can
        be checked by using PluginDescriptionFile.get_awareness().Set.contains(flag).
        """

        @property
        def UTF8(self) -> 'Flags':
            """
            This specifies that all (text) resources stored in a plugin's jar
            use UTF-8 encoding.

            @deprecated all plugins are now assumed to be UTF-8 aware.
            """
            ...