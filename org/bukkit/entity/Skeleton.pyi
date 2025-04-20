from typing import Literal

class Skeleton(AbstractSkeleton):
    """
    Represents a Skeleton.
    This interface only represents the normal skeleton type on the server.
    Other skeleton-like entities, such as the Stray or the WitherSkeleton are not related to this type.
    """

    def is_converting(self) -> bool:
        """
        Computes whether or not this skeleton is currently in the process of
        converting to a Stray due to it being frozen by powdered snow.

        :return: whether or not the skeleton is converting to a stray.
        """
        ...

    def get_conversion_time(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a stray
        as a result of being frozen by a powdered snow block.
        When this reaches 0, the entity will be converted.

        :return: the conversion time left represented in ticks.

        :raises IllegalStateException: if is_converting() is false.
        """
        ...

    def set_conversion_time(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a stray
        as a result of being frozen by a powdered snow block.
        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        :param time: the new conversion time left before the conversion in ticks.
        """
        ...

    class SkeletonType:
        """
        A legacy enum that defines the different variances of skeleton-like
        entities on the server.

        :deprecated: classes are different types. This interface only remains in
            the Skeleton interface to preserve backwards compatibility.
        """
        NORMAL: Literal['NORMAL'] = 'NORMAL'
        WITHER: Literal['WITHER'] = 'WITHER'
        STRAY: Literal['STRAY'] = 'STRAY'
        BOGGED: Literal['BOGGED'] = 'BOGGED'