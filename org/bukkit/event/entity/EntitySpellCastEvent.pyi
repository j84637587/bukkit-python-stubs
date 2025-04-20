from org.bukkit.entity import Spellcaster
from org.bukkit.event import Cancellable, HandlerList
from typing import Any

class EntitySpellCastEvent(EntityEvent, Cancellable):
    """
    Called when a {@link Spellcaster} casts a spell.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    spell: Spellcaster.Spell

    def __init__(self, what: Spellcaster, spell: Spellcaster.Spell) -> None:
        """
        Initialize the event with the given Spellcaster and Spell.

        :param what: The Spellcaster that is casting the spell.
        :param spell: The Spell to be cast.
        """
        ...

    def getEntity(self) -> Spellcaster:
        """
        Get the Spellcaster that is casting the spell.

        :return: The Spellcaster entity.
        """
        ...

    def getSpell(self) -> Spellcaster.Spell:
        """
        Get the spell to be cast in this event.

        This is a convenience method equivalent to
        {@link Spellcaster#getSpell()}.

        :return: The spell to cast.
        """
        ...

    def setCancelled(self, cancelled: bool) -> None:
        """
        Set whether the event is cancelled.

        :param cancelled: True to cancel the event, False otherwise.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Check if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Get the handler list for this event.

        :return: The handler list.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Get the static handler list for this event.

        :return: The static handler list.
        """
        ...