from typing import Optional
import uuid

"""
Represents a resource pack.

@see <a href="https://minecraft.wiki/w/Resource_pack">Minecraft wiki</a>
"""
class ResourcePack:
    """
    Gets the id of the resource pack.

    @return the id
    """
    def get_id(self) -> uuid.UUID:
        ...

    """
    Gets the url of the resource pack.

    @return the url
    """
    def get_url(self) -> str:
        ...

    """
    Gets the hash of the resource pack.

    @return the hash
    """
    def get_hash(self) -> Optional[str]:
        ...

    """
    Gets the prompt to show of the resource pack.

    @return the prompt
    """
    def get_prompt(self) -> Optional[str]:
        ...

    """
    Gets if the resource pack is required by the server.

    @return True if is required
    """
    def is_required(self) -> bool:
        ...