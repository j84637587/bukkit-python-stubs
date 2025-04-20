from typing import Protocol
from ipaddress import IPv4Address, IPv6Address

class BanList(Protocol[T]):
    """A protocol representing a BanList."""

    pass

class IpBanList(BanList[IPv4Address]):
    """A BanList targeting IP bans."""
    
    pass