from typing import Protocol, TypeVar, Any
from org.jetbrains.annotations import NotNull

HelpTopicType = TypeVar('HelpTopicType', bound='HelpTopic')

class HelpTopic:
    def get_name(self) -> str:
        """Returns the name of the help topic."""
        ...

class HelpTopicComparator(Protocol[HelpTopicType]):
    """
    Used to impose a custom total ordering on help topics.
    <p>
    All topics are listed in alphabetic order, but topics that start with a
    slash come after topics that don't.
    """

    @staticmethod
        def topic_name_comparator_instance() -> 'HelpTopicComparator':
        ...

    @staticmethod
        def help_topic_comparator_instance() -> 'HelpTopicComparator':
        ...

    def compare(self, lhs: HelpTopicType, rhs: HelpTopicType) -> int:
        ...

class TopicNameComparator(Protocol):
    def compare(self, lhs: str, rhs: str) -> int:
        ...