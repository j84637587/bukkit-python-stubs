from typing import List, Optional
from org.bukkit.command import CommandSender
from org.bukkit.event import Event
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import RegisteredListener
from org.bukkit.plugin import TimedRegisteredListener
from org.bukkit.util import StringUtil
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableList

class TimingsCommand(BukkitCommand):
    TIMINGS_SUBCOMMANDS: List[str] = ImmutableList.of("merged", "reset", "separate")

    def __init__(self, name: str) -> None:
        """Records timings for all plugin events."""
        ...

    def execute(self, sender: CommandSender, current_alias: str, args: List[str]) -> bool:
        """Executes the timings command."""
        ...

    def tabComplete(self, sender: CommandSender, alias: str, args: List[str]) -> List[str]:
        """Completes the command arguments for tab completion."""
        ...