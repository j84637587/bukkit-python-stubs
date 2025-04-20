from typing import List, TypeVar, Optional
from org.bukkit.Color import Color
from org.bukkit.Particle import Particle
from org.bukkit.potion.PotionData import PotionData
from org.bukkit.potion.PotionEffect import PotionEffect
from org.bukkit.potion.PotionEffectType import PotionEffectType
from org.bukkit.potion.PotionType import PotionType
from org.bukkit.projectiles.ProjectileSource import ProjectileSource
from org.jetbrains.annotations import NotNull, Nullable

T = TypeVar('T')

class AreaEffectCloud(Entity):
    """
    Represents an area effect cloud which will imbue a potion effect onto
    entities which enter it.
    """

    def getDuration(self) -> int:
        """
        Gets the duration which this cloud will exist for (in ticks).

        @return cloud duration
        """
        ...

    def setDuration(self, duration: int) -> None:
        """
        Sets the duration which this cloud will exist for (in ticks).

        @param duration cloud duration
        """
        ...

    def getWaitTime(self) -> int:
        """
        Gets the time which an entity has to be exposed to the cloud before the
        effect is applied.

        @return wait time
        """
        ...

    def setWaitTime(self, waitTime: int) -> None:
        """
        Sets the time which an entity has to be exposed to the cloud before the
        effect is applied.

        @param waitTime wait time
        """
        ...

    def getReapplicationDelay(self) -> int:
        """
        Gets the time that an entity will be immune from subsequent exposure.

        @return reapplication delay
        """
        ...

    def setReapplicationDelay(self, delay: int) -> None:
        """
        Sets the time that an entity will be immune from subsequent exposure.

        @param delay reapplication delay
        """
        ...

    def getDurationOnUse(self) -> int:
        """
        Gets the amount that the duration of this cloud will decrease by when it
        applies an effect to an entity.

        @return duration on use delta
        """
        ...

    def setDurationOnUse(self, duration: int) -> None:
        """
        Sets the amount that the duration of this cloud will decrease by when it
        applies an effect to an entity.

        @param duration duration on use delta
        """
        ...

    def getRadius(self) -> float:
        """
        Gets the initial radius of the cloud.

        @return radius
        """
        ...

    def setRadius(self, radius: float) -> None:
        """
        Sets the initial radius of the cloud.

        @param radius radius
        """
        ...

    def getRadiusOnUse(self) -> float:
        """
        Gets the amount that the radius of this cloud will decrease by when it
        applies an effect to an entity.

        @return radius on use delta
        """
        ...

    def setRadiusOnUse(self, radius: float) -> None:
        """
        Sets the amount that the radius of this cloud will decrease by when it
        applies an effect to an entity.

        @param radius radius on use delta
        """
        ...

    def getRadiusPerTick(self) -> float:
        """
        Gets the amount that the radius of this cloud will decrease by each tick.

        @return radius per tick delta
        """
        ...

    def setRadiusPerTick(self, radius: float) -> None:
        """
        Gets the amount that the radius of this cloud will decrease by each tick.

        @param radius per tick delta
        """
        ...

        def getParticle(self) -> Particle:
        """
        Gets the particle which this cloud will be composed of

        @return particle the set particle type
        """
        ...

    def setParticle(self, particle: Particle) -> None:
        """
        Sets the particle which this cloud will be composed of

        @param particle the new particle type
        """
        ...

    def setParticleWithData(self, particle: Particle, data: Optional[T]) -> None:
        """
        Sets the particle which this cloud will be composed of

        @param <T> type of particle data (see {@link Particle#getDataType()}
        @param particle the new particle type
        @param data the data to use for the particle or null,
                     the type of this depends on {@link Particle#getDataType()}
        """
        ...

    def setBasePotionData(self, data: Optional[PotionData]) -> None:
        """
        Sets the underlying potion data

        @param data PotionData to set the base potion state to
        @deprecated Upgraded / extended potions are now their own {@link PotionType} use {@link #setBasePotionType} instead.
        """
        ...

        def getBasePotionData(self) -> Optional[PotionData]:
        """
        Returns the potion data about the base potion

        @return a PotionData object
        @deprecated Upgraded / extended potions are now their own {@link PotionType} use {@link #getBasePotionType()} instead.
        """
        ...

    def setBasePotionType(self, type: Optional[PotionType]) -> None:
        """
        Sets the underlying potion type

        @param type PotionType to set the base potion state to
        """
        ...

        def getBasePotionType(self) -> Optional[PotionType]:
        """
        Returns the potion type about the base potion

        @return a PotionType object
        """
        ...

    def hasCustomEffects(self) -> bool:
        """
        Checks for the presence of custom potion effects.

        @return true if custom potion effects are applied
        """
        ...

        def getCustomEffects(self) -> List[PotionEffect]:
        """
        Gets an immutable list containing all custom potion effects applied to
        this cloud.
        <p>
        Plugins should check that hasCustomEffects() returns true before calling
        this method.

        @return the immutable list of custom potion effects
        """
        ...

    def addCustomEffect(self, effect: PotionEffect, overwrite: bool) -> bool:
        """
        Adds a custom potion effect to this cloud.

        @param effect the potion effect to add
        @param overwrite true if any existing effect of the same type should be
        overwritten
        @return true if the effect was added as a result of this call
        """
        ...

    def removeCustomEffect(self, type: PotionEffectType) -> bool:
        """
        Removes a custom potion effect from this cloud.

        @param type the potion effect type to remove
        @return true if the an effect was removed as a result of this call
        """
        ...

    def hasCustomEffect(self, type: Optional[PotionEffectType]) -> bool:
        """
        Checks for a specific custom potion effect type on this cloud.

        @param type the potion effect type to check for
        @return true if the potion has this effect
        """
        ...

    def clearCustomEffects(self) -> None:
        """
        Removes all custom potion effects from this cloud.
        """
        ...

        def getColor(self) -> Color:
        """
        Gets the color of this cloud. Will be applied as a tint to its particles.

        @return cloud color
        """
        ...

    def setColor(self, color: Color) -> None:
        """
        Sets the color of this cloud. Will be applied as a tint to its particles.

        @param color cloud color
        """
        ...

        def getSource(self) -> Optional[ProjectileSource]:
        """
        Retrieve the original source of this cloud.

        @return the {@link ProjectileSource} that threw the LingeringPotion
        """
        ...

    def setSource(self, source: Optional[ProjectileSource]) -> None:
        """
        Set the original source of this cloud.

        @param source the {@link ProjectileSource} that threw the LingeringPotion
        """
        ...