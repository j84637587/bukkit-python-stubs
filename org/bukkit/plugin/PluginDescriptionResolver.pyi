from yaml.nodes import Tag
from yaml.resolver import Resolver

class PluginDescriptionResolver(Resolver):
    """Final class that resolves plugin descriptions."""

    def add_implicit_resolvers(self) -> None:
        """Add implicit resolvers for various YAML tags."""
        ...