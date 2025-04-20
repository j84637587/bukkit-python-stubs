from typing import Optional, Awaitable
from uuid import UUID
from concurrent.futures import Future
from org.bukkit import Server
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.jetbrains.annotations import NotNull, Nullable

class PlayerProfile(ConfigurationSerializable):
    """
    A player profile.
    <p>
    A player profile always provides a unique id, a non-empty name, or both. Its
    unique id and name are immutable, but other properties (such as its textures)
    can be altered.
    <p>
    New profiles can be created via
    {@link Server#createPlayerProfile(UUID, String)}.
    """

        def getUniqueId(self) -> Optional[UUID]:
        """
        Gets the player's unique id.

        @return the player's unique id, or <code>null</code> if not available
        """
        ...

        def getName(self) -> Optional[str]:
        """
        Gets the player name.

        @return the player name, or <code>null</code> if not available
        """
        ...

        def getTextures(self) -> 'PlayerTextures':
        """
        Gets the {@link PlayerTextures} of this profile.

        @return the textures, not <code>null</code>
        """
        ...

    def setTextures(self, textures: Optional['PlayerTextures']) -> None:
        """
        Copies the given textures.

        @param textures the textures to copy, or <code>null</code> to clear the
        textures
        """
        ...

    def isComplete(self) -> bool:
        """
        Checks whether this profile is complete.
        <p>
        A profile is currently considered complete if it has a name, a unique id,
        and textures.

        @return <code>true</code> if this profile is complete
        """
        ...

        def update(self) -> Future['PlayerProfile']:
        """
        Produces an updated player profile based on this profile.
        <p>
        This tries to produce a completed profile by filling in missing
        properties (name, unique id, textures, etc.), and updates existing
        properties (e.g. name, textures, etc.) to their official and up-to-date
        values. This operation does not alter the current profile, but produces a
        new updated {@link PlayerProfile}.
        <p>
        If no player exists for the unique id or name of this profile, this
        operation yields a profile that is equal to the current profile, which
        might not be complete.
        <p>
        This is an asynchronous operation: Updating the profile can result in an
        outgoing connection in another thread in order to fetch the latest
        profile properties. The returned {@link CompletableFuture} will be
        completed once the updated profile is available. In order to not block
        the server's main thread, you should not wait for the result of the
        returned CompletableFuture on the server's main thread. Instead, if you
        want to do something with the updated player profile on the server's main
        thread once it is available, you could do something like this:
        <pre>
        profile.update().thenAcceptAsync(updatedProfile -> {
            // Do something with the updated profile:
            // ...
        }, runnable -> Bukkit.getScheduler().runTask(plugin, runnable));
        </pre>

        @return a completable future that gets completed with the updated
        PlayerProfile once it is available
        """
        ...

        def clone(self) -> 'PlayerProfile':
        ...