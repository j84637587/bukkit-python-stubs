from typing import List, Optional
from urllib.parse import urlparse

class ServerLinks:
    """
    Represents a collections of links which may be sent to a client.
    """
    def getLink(self, type: 'Type') -> Optional['ServerLink']:
        """
        Gets the link of a given type, if it exists.

        :param type: link type
        :return: link or null
        """
        pass

    def getLinks(self) -> List['ServerLink']:
        """
        Gets an immutable list of all links.

        :return: immutable list
        """
        pass

    def setLink(self, type: 'Type', url: urlparse) -> 'ServerLink':
        """
        Adds the given link, overwriting the first link of the same type if
        already set.

        :param type: link type
        :param url: link url
        :return: the added link
        """
        pass

    def addLink(self, type: 'Type', url: urlparse) -> 'ServerLink':
        """
        Adds the given link to the list of links.

        :param type: link type
        :param url: link url
        :return: the added link
        """
        pass

    def addLink(self, displayName: str, url: urlparse) -> 'ServerLink':
        """
        Adds the given link to the list of links.

        :param displayName: link name / display text
        :param url: link url
        :return: the added link
        """
        pass

    def removeLink(self, link: 'ServerLink') -> bool:
        """
        Removes the given link.

        :param link: the link to remove
        :return: if the link existed and was removed
        """
        pass

    def copy(self) -> 'ServerLinks':
        """
        Returns a copy of this link collection, unassociated from the server.

        :return: copied links
        """
        pass

class ServerLink:
    """
    Represents a server link.
    """
    def getType(self) -> Optional['Type']:
        """
        Gets the type of this link if it is a known special type.

        :return: type or null
        """
        pass

    def getDisplayName(self) -> str:
        """
        Gets the display name/text of this link.

        :return: display name
        """
        pass

    def getUrl(self) -> urlparse:
        """
        Gets the url of this link.

        :return: link url
        """
        pass

class Type:
    """
    Represents a known type of link which will be translated by the client
    and may have special functionality.
    """
    REPORT_BUG = 0
    COMMUNITY_GUIDELINES = 1
    SUPPORT = 2
    STATUS = 3
    FEEDBACK = 4
    COMMUNITY = 5
    WEBSITE = 6
    FORUMS = 7
    NEWS = 8
    ANNOUNCEMENTS = 9