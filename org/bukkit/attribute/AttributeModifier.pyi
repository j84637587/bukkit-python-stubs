from typing import Dict, Optional, Union
import re
import uuid

from org.bukkit import Keyed, NamespacedKey
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory import EquipmentSlot, EquipmentSlotGroup
from org.bukkit.util import NumberConversions
from org.jetbrains.annotations import NotNull, Nullable

UUID_PATTERN = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)

class AttributeModifier(ConfigurationSerializable, Keyed):
    """
    Concrete implementation of an attribute modifier.
    """

    def __init__(self, name: str, amount: float, operation: "Operation") -> None:
        """
        @deprecated since = "1.21", forRemoval = true
        """
        ...

    def __init__(
        self, uuid: uuid.UUID, name: str, amount: float, operation: "Operation"
    ) -> None:
        """
        @deprecated since = "1.21", forRemoval = true
        """
        ...

    def __init__(
        self,
        uuid: uuid.UUID,
        name: str,
        amount: float,
        operation: "Operation",
        slot: Optional[EquipmentSlot] = None,
    ) -> None:
        """
        @deprecated since = "1.21", forRemoval = true
        """
        ...

    def __init__(
        self,
        uuid: uuid.UUID,
        name: str,
        amount: float,
        operation: "Operation",
        slot: EquipmentSlotGroup,
    ) -> None: ...
    def __init__(
        self,
        key: NamespacedKey,
        amount: float,
        operation: "Operation",
        slot: EquipmentSlotGroup,
    ) -> None: ...
        @Deprecated(since="1.21", forRemoval=True)
    def get_unique_id(self) -> uuid.UUID:
        """
        Get the unique ID for this modifier.

        @return unique id
        @see #getKey()
        @deprecated attributes are now identified by keys
        """
        ...

        def get_key(self) -> NamespacedKey: ...
        def get_name(self) -> str:
        """
        Get the name of this modifier.

        @return name
        """
        ...

    def get_amount(self) -> float:
        """
        Get the amount by which this modifier will apply its {@link Operation}.

        @return modification amount
        """
        ...

        def get_operation(self) -> "Operation":
        """
        Get the operation this modifier will apply.

        @return operation
        """
        ...

        @Deprecated(since="1.20.5")
    def get_slot(self) -> Optional[EquipmentSlot]:
        """
        Get the {@link EquipmentSlot} this AttributeModifier is active on,
        or null if this modifier is applicable for any slot.

        @return the slot
        """
        ...

        def get_slot_group(self) -> EquipmentSlotGroup:
        """
        Get the {@link EquipmentSlot} this AttributeModifier is active on,
        or null if this modifier is applicable for any slot.

        @return the slot
        """
        ...

        def serialize(self) -> Dict[str, Union[str, float, int]]: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
        @staticmethod
    def deserialize(args: Dict[str, object]) -> "AttributeModifier":
        """
        @param args: The arguments to deserialize
        @return: An instance of AttributeModifier
        """
        ...

    class Operation:
        """
        Enumerable operation to be applied.
        """

        ADD_NUMBER = ...
        ADD_SCALAR = ...
        MULTIPLY_SCALAR_1 = ...
