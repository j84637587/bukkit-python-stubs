from typing import Dict, Optional

class PistonMoveReaction:
    """
    Represents how a block or entity will react when interacting with a piston
    when it is extending or retracting.
    """
    
    MOVE: 'PistonMoveReaction'
    BREAK: 'PistonMoveReaction'
    BLOCK: 'PistonMoveReaction'
    IGNORE: 'PistonMoveReaction'
    PUSH_ONLY: 'PistonMoveReaction'

    def __init__(self, id: int) -> None:
        ...

    @property
    def id(self) -> int:
        """
        @return The ID of the move reaction
        @deprecated Magic value
        """
        ...

    @staticmethod
    def get_by_id(id: int) -> Optional['PistonMoveReaction']:
        """
        @param id An ID
        @return The move reaction with that ID
        @deprecated Magic value
        """
        ...
    
    @staticmethod
    def values() -> Dict[int, 'PistonMoveReaction']:
        ...