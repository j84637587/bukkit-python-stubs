from org.bukkit.event import Event

"""
Miscellaneous server events
"""
class ServerEvent(Event):
    def __init__(self) -> None:
        super().__init__()

    def __init__(self, is_async: bool) -> None:
        super().__init__(is_async)