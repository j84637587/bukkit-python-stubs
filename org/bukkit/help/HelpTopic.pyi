from org.bukkit.command import CommandSender
from org.bukkit.entity import Player
from typing import Optional

class HelpTopic:
    """
    HelpTopic implementations are displayed to the user when the user uses the
    /help command.
    <p>
    Custom implementations of this class can work at two levels. A simple
    implementation only needs to set the value of {@code name}, {@code
    shortText}, and {@code fullText} in the constructor. This base class will
    take care of the rest.
    <p>
    Complex implementations can be created by overriding the behavior of all
    the methods in this class.
    """

    name: str
    shortText: str
    fullText: str
    amendedPermission: Optional[str]

    def __init__(self) -> None:
        self.name = ""
        self.shortText = ""
        self.fullText = ""
        self.amendedPermission = None

    def can_see(self, player: CommandSender) -> bool:
        """
        Determines if a {@link Player} is allowed to see this help topic.
        <p>
        HelpTopic implementations should take server administrator wishes into
        account as set by the {@link HelpTopic#amendCanSee(String)} function.

        @param player The Player in question.
        @return True of the Player can see this help topic, false otherwise.
        """
        ...

    def amend_can_see(self, amended_permission: Optional[str]) -> None:
        """
        Allows the server administrator to override the permission required to
        see a help topic.
        <p>
        HelpTopic implementations should take this into account when
        determining topic visibility on the {@link
        HelpTopic#canSee(org.bukkit.command.CommandSender)} function.

        @param amended_permission The permission node the server administrator
            wishes to apply to this topic.
        """
        ...

    def get_name(self) -> str:
        """
        Returns the name of this help topic.

        @return The topic name.
        """
        ...

    def get_short_text(self) -> str:
        """
        Returns a brief description that will be displayed in the topic index.

        @return A brief topic description.
        """
        ...

    def get_full_text(self, for_who: CommandSender) -> str:
        """
        Returns the full description of this help topic that is displayed when
        the user requests this topic's details.
        <p>
        The result will be paginated to properly fit the user's client.

        @param for_who The player or console requesting the full text. Useful
            for further security trimming the command's full text based on
            sub-permissions in custom implementations.

        @return A full topic description.
        """
        ...

    def amend_topic(self, amended_short_text: Optional[str], amended_full_text: Optional[str]) -> None:
        """
        Allows the server admin (or another plugin) to add or replace the
        contents of a help topic.
        <p>
        A null in either parameter will leave that part of the topic unchanged.
        In either amending parameter, the string {@literal <text>} is replaced
        with the existing contents in the help topic. Use this to append or
        prepend additional content into an automatically generated help topic.

        @param amended_short_text The new topic short text to use, or null to
            leave alone.
        @param amended_full_text The new topic full text to use, or null to leave
            alone.
        """
        ...

    def apply_amendment(self, base_text: str, amendment: Optional[str]) -> str:
        """
        Developers implementing their own custom HelpTopic implementations can
        use this utility method to ensure their implementations comply with the
        expected behavior of the {@link HelpTopic#amendTopic(String, String)}
        method.

        @param base_text The existing text of the help topic.
        @param amendment The amending text from the amendTopic() method.
        @return The application of the amending text to the existing text,
            according to the expected rules of amendTopic().
        """
        ...