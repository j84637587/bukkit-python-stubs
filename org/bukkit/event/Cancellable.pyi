from typing import Protocol

class Cancellable(Protocol):
    """A type characterizing events that may be cancelled by a plugin or the server."""

    def is_cancelled(self) -> bool:
        """Gets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.

        Returns:
            bool: true if this event is cancelled
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """Sets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.

        Args:
            cancel (bool): true if you wish to cancel this event
        """
        ...