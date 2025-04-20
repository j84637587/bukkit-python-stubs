from typing import Dict, Optional

class Tone:
    """
    An enum holding tones.
    """
    G = ...
    A = ...
    B = ...
    C = ...
    D = ...
    E = ...
    F = ...

    BY_DATA: Dict[byte, Tone] = ...
    TONES_COUNT: byte = ...

    def __init__(self, id: int, sharpable: bool) -> None:
        ...

    def getId(self, sharped: bool = False) -> byte:
        """
        Returns the id of this tone. These method allows to return the
        sharped id of the tone. If the tone couldn't be sharped it always
        return the not sharped id of this tone.
        """
        ...

    def isSharpable(self) -> bool:
        """
        Returns if this tone could be sharped.
        """
        ...

    def isSharped(self, id: byte) -> bool:
        """
        Returns if this tone id is the sharped id of the tone.
        """
        ...

    @staticmethod
    def getById(id: byte) -> Optional[Tone]:
        """
        Returns the tone to id. Also returning the semitones.
        """
        ...

class Note:
    """
    A note class to store a specific note.
    """
    def __init__(self, note: int) -> None:
        ...

    @staticmethod
    def flat(octave: int, tone: Tone) -> Note:
        """
        Creates a new note for a flat tone, such as A-flat.
        """
        ...

    @staticmethod
    def sharp(octave: int, tone: Tone) -> Note:
        """
        Creates a new note for a sharp tone, such as A-sharp.
        """
        ...

    @staticmethod
    def natural(octave: int, tone: Tone) -> Note:
        """
        Creates a new note for a natural tone, such as A-natural.
        """
        ...

    def sharped(self) -> Note:
        """
        Returns the note a semitone above this one.
        """
        ...

    def flattened(self) -> Note:
        """
        Returns the note a semitone below this one.
        """
        ...

    def getId(self) -> byte:
        """
        Returns the internal id of this note.
        """
        ...

    def getOctave(self) -> int:
        """
        Returns the octave of this note.
        """
        ...

    def getTone(self) -> Tone:
        """
        Returns the tone of this note.
        """
        ...

    def isSharped(self) -> bool:
        """
        Returns if this note is sharped.
        """
        ...

    def getPitch(self) -> float:
        """
        Gets the pitch of this note.
        """
        ...

    def __eq__(self, obj: object) -> bool:
        """
        Checks if this note is equal to another.
        """
        ...

    def __str__(self) -> str:
        """
        Returns a string representation of this note.
        """
        ...