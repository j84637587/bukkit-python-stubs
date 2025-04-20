from typing import Collection, List, Optional, Type, TypeVar

HelpTopic = TypeVar('HelpTopic')
HelpTopicFactory = TypeVar('HelpTopicFactory')

class HelpMap:
    """
    The HelpMap tracks all help topics registered in a Bukkit server. When the
    server starts up or is reloaded, help is processed and topics are added in
    the following order:
    
    <ol>
    <li>General topics are loaded from the help.yml
    <li>Plugins load and optionally call {@code addTopic()}
    <li>Registered plugin commands are processed by {@link HelpTopicFactory}
        objects to create topics
    <li>Topic contents are amended as directed in help.yml
    </ol>
    """

    def get_help_topic(self, topic_name: str) -> Optional[HelpTopic]:
        """
        Returns a help topic for a given topic name.
        
        @param topic_name: The help topic name to look up.
        @return: A {@link HelpTopic} object matching the topic name or None if
            none can be found.
        """
        ...

    def get_help_topics(self) -> Collection[HelpTopic]:
        """
        Returns a collection of all the registered help topics.
        
        @return: All the registered help topics.
        """
        ...

    def add_topic(self, topic: HelpTopic) -> None:
        """
        Adds a topic to the server's help index.
        
        @param topic: The new help topic to add.
        """
        ...

    def clear(self) -> None:
        """
        Clears out the contents of the help index. Normally called during
        server reload.
        """
        ...

    def register_help_topic_factory(self, command_class: Type, factory: HelpTopicFactory) -> None:
        """
        Associates a {@link HelpTopicFactory} object with given command base
        class. Plugins typically call this method during {@code onLoad()}. Once
        registered, the custom HelpTopicFactory will be used to create a custom
        {@link HelpTopic} for all commands deriving from the {@code
        command_class} base class, or all commands deriving from {@link
        org.bukkit.command.PluginCommand} who's executor derives from {@code
        command_class} base class.
        
        @param command_class: The class for which the custom HelpTopicFactory
            applies. Must derive from either {@link org.bukkit.command.Command}
            or {@link org.bukkit.command.CommandExecutor}.
        @param factory: The {@link HelpTopicFactory} implementation to associate
            with the {@code command_class}.
        @raises IllegalArgumentException: Thrown if {@code command_class} does
            not derive from a legal base class.
        """
        ...

    def get_ignored_plugins(self) -> List[str]:
        """
        Gets the list of plugins the server administrator has chosen to exclude
        from the help index. Plugin authors who choose to directly extend
        {@link org.bukkit.command.Command} instead of {@link
        org.bukkit.command.PluginCommand} will need to check this collection in
        their {@link HelpTopicFactory} implementations to ensure they meet the
        server administrator's expectations.
        
        @return: A list of plugins that should be excluded from the help index.
        """
        ...