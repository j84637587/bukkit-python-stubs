from typing import Dict, Optional, Type
from enum import Enum

class WarningState(Enum):
    """
    This represents the states that server verbose for warnings may be.
    """
    ON = "ON"
    OFF = "OFF"
    DEFAULT = "DEFAULT"

    @staticmethod
    def value(value: Optional[str]) -> 'WarningState':
        """
        This method returns the corresponding warning state for the given
        string value.

        Args:
            value: The string value to check

        Returns:
            WarningState: DEFAULT if not found, or the respective WarningState
        """
        if value is None:
            return WarningState.DEFAULT
        state = WarningState.values.get(value.lower())
        if state is None:
            return WarningState.DEFAULT
        return state

    def print_for(self, warning: Optional['Warning']) -> bool:
        """
        This method checks the provided warning should be printed for this state.

        Args:
            warning: The warning annotation added to a deprecated item

        Returns:
            bool: <ul>
                <li>ON is always True
                <li>OFF is always false
                <li>DEFAULT is false if and only if annotation is not null and
                specifies false for Warning.value(), true otherwise.
                </ul>
        """
        if self == WarningState.DEFAULT:
            return warning is None or warning.value()
        return self == WarningState.ON

# This will be the decorator for the Warning annotation
class Warning:
    """
    This designates the warning state for a specific item.
    <p>
    When the server settings dictate 'default' warnings, warnings are printed
    if the value() is true.
    """

    def __init__(self, value: bool = False, reason: str = "") -> None:
        """
        This sets if the deprecation warnings when registering events gets
        printed when the setting is in the default state.

        Args:
            value: false normally, or true to encourage warning printout
            reason: The reason an event is deprecated
        """
        self.value = value
        self.reason = reason

    @property
    def value(self) -> bool:
        """
        This sets if the deprecation warnings when registering events gets
        printed when the setting is in the default state.

        Returns:
            bool: false normally, or true to encourage warning printout
        """
        return self._value

    @value.setter
    def value(self, value: bool) -> None:
        self._value = value

    @property
    def reason(self) -> str:
        """
        This can provide detailed information on why the event is deprecated.

        Returns:
            str: The reason an event is deprecated
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str) -> None:
        self._reason = reason

# Static map for WarningState values
WarningState.values: Dict[str, WarningState] = {
    "off": WarningState.OFF,
    "false": WarningState.OFF,
    "f": WarningState.OFF,
    "no": WarningState.OFF,
    "n": WarningState.OFF,
    "on": WarningState.ON,
    "true": WarningState.ON,
    "t": WarningState.ON,
    "yes": WarningState.ON,
    "y": WarningState.ON,
    "": WarningState.DEFAULT,
    "d": WarningState.DEFAULT,
    "default": WarningState.DEFAULT,
}