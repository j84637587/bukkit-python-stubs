from pathlib import Path
from typing import Any

class FileUtil:
    """
    Class containing file utilities
    """

    @staticmethod
    def copy(in_file: Path, out_file: Path) -> bool:
        """
        This method copies one file to another location

        @param in_file: the source filename
        @param out_file: the target filename
        @return: true on success
        """
        ...