from typing import Optional
from urllib import request

class PlayerTextures:
    """
    Provides access to the textures stored inside a PlayerProfile.
    <p>
    Modifying the textures immediately invalidates and clears any previously
    present attributes that are specific to official player profiles, such as the
    timestamp and signature.
    """

    class SkinModel:
        """
        The different Minecraft skin models.
        """
        CLASSIC = "CLASSIC"
        SLIM = "SLIM"

    def is_empty(self) -> bool:
        """
        Checks if the profile stores no textures.

        @return true if the profile stores no textures
        """
        ...

    def clear(self) -> None:
        """
        Clears the textures.
        """
        ...

    def get_skin(self) -> Optional[request.URL]:
        """
        Gets the URL that points to the player's skin.

        @return the URL of the player's skin, or null if not set
        """
        ...

    def set_skin(self, skin_url: Optional[request.URL]) -> None:
        """
        Sets the player's skin to the specified URL, and the skin model to
        SkinModel.CLASSIC.
        <p>
        The URL must point to the Minecraft texture server. Example URL:
        <pre>
        http://textures.minecraft.net/texture/b3fbd454b599df593f57101bfca34e67d292a8861213d2202bb575da7fd091ac
        </pre>

        @param skin_url the URL of the player's skin, or null to unset it
        """
        ...

    def set_skin(self, skin_url: Optional[request.URL], skin_model: Optional['PlayerTextures.SkinModel']) -> None:
        """
        Sets the player's skin and SkinModel.
        <p>
        The URL must point to the Minecraft texture server. Example URL:
        <pre>
        http://textures.minecraft.net/texture/b3fbd454b599df593f57101bfca34e67d292a8861213d2202bb575da7fd091ac
        </pre>
        <p>
        A skin model of null results in SkinModel.CLASSIC to be used.

        @param skin_url the URL of the player's skin, or null to unset it
        @param skin_model the skin model, ignored if the skin URL is null
        """
        ...

    def get_skin_model(self) -> 'PlayerTextures.SkinModel':
        """
        Gets the model of the player's skin.
        <p>
        This returns SkinModel.CLASSIC if no skin is set.

        @return the model of the player's skin
        """
        ...

    def get_cape(self) -> Optional[request.URL]:
        """
        Gets the URL that points to the player's cape.

        @return the URL of the player's cape, or null if not set
        """
        ...

    def set_cape(self, cape_url: Optional[request.URL]) -> None:
        """
        Sets the URL that points to the player's cape.
        <p>
        The URL must point to the Minecraft texture server. Example URL:
        <pre>
        http://textures.minecraft.net/texture/2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933
        </pre>

        @param cape_url the URL of the player's cape, or null to unset it
        """
        ...

    def get_timestamp(self) -> int:
        """
        Gets the timestamp at which the profile was last updated.

        @return the timestamp, or 0 if unknown
        """
        ...

    def is_signed(self) -> bool:
        """
        Checks if the textures are signed and the signature is valid.

        @return true if the textures are signed and the signature is valid
        """
        ...