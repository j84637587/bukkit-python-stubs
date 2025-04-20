from typing import Protocol
from socket import SocketAddress
from typing import Any

class CommandSender(Protocol):
    pass

class RemoteConsoleCommandSender(CommandSender, Protocol):
    """
    Gets the socket address of this remote sender.
    
    @return: the remote sender's address
    """
    
    def get_address(self) -> SocketAddress:
        ...