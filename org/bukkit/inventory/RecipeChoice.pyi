from typing import List, Protocol, TypeVar, Union
from org.bukkit import ItemStack, Material, Tag
from com.google.common.base import Preconditions
from java.lang import Cloneable

T = TypeVar('T')

class RecipeChoice(Protocol[T], Cloneable):
    """
    Represents a potential item match within a recipe. All choices within a
    recipe must be satisfied for it to be craftable. Choices must never be
    null or air.

    <b>This class is not legal for implementation by plugins!</b>
    """

    def get_item_stack(self) -> ItemStack:
        """
        Gets a single item stack representative of this stack choice.

        @return: a single representative item
        @deprecated for compatibility only
        """
        ...

    def clone(self) -> 'RecipeChoice':
        ...

    def test(self, item_stack: ItemStack) -> bool:
        ...

class MaterialChoice(RecipeChoice[Material]):
    """
    Represents a choice of multiple matching Materials.
    """

    def __init__(self, choice: Material) -> None:
        ...

    def __init__(self, *choices: Material) -> None:
        ...

    def __init__(self, choices: Tag[Material]) -> None:
        ...

    def __init__(self, choices: List[Material]) -> None:
        ...

    def test(self, t: ItemStack) -> bool:
        ...

    def get_item_stack(self) -> ItemStack:
        ...

    def get_choices(self) -> List[Material]:
        ...

    def clone(self) -> 'MaterialChoice':
        ...

    def hash_code(self) -> int:
        ...

    def equals(self, obj: object) -> bool:
        ...

    def to_string(self) -> str:
        ...

class ExactChoice(RecipeChoice[ItemStack]):
    """
    Represents a choice that will be valid only if one of the stacks is
    exactly matched (aside from stack size).
    <br>
    <b>Only valid for shaped recipes</b>
    """

    def __init__(self, stack: ItemStack) -> None:
        ...

    def __init__(self, *stacks: ItemStack) -> None:
        ...

    def __init__(self, choices: List[ItemStack]) -> None:
        ...

    def get_item_stack(self) -> ItemStack:
        ...

    def get_choices(self) -> List[ItemStack]:
        ...

    def clone(self) -> 'ExactChoice':
        ...

    def test(self, t: ItemStack) -> bool:
        ...

    def hash_code(self) -> int:
        ...

    def equals(self, obj: object) -> bool:
        ...

    def to_string(self) -> str:
        ...