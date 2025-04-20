from typing import Protocol, Any

class Plugin(Protocol):
    def getDescription(self) -> Any:
        ...

class PluginBase(Plugin):
    """
    Represents a base {@link Plugin}
    <p>
    Extend this class if your plugin is not a {@link
    org.bukkit.plugin.java.JavaPlugin}
    """

    def __hash__(self) -> int:
        ...

    def __eq__(self, obj: Any) -> bool:
        ...

    def getName(self) -> str:
        ...