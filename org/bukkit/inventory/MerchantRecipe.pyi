from typing import List, Optional
from org.bukkit.inventory import Recipe
from org.bukkit import Material
from org.bukkit.entity import Villager
from org.bukkit.potion import PotionEffectType
from org.bukkit.util import NumberConversions
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull, Nullable

class MerchantRecipe(Recipe):
    """
    Represents a merchant's trade.
    <p>
    Trades can take one or two ingredients, and provide one result. The
    ingredients' ItemStack amounts are respected in the trade.
    <p>
    A trade has a maximum number of uses. A {@link Villager} may periodically
    replenish its trades by resetting the {@link #getUses uses} of its merchant
    recipes to <code>0</code>, allowing them to be used again.
    <p>
    A trade may or may not reward experience for being completed.
    <p>
    During trades, the {@link MerchantRecipe} dynamically adjusts the amount of
    its first ingredient based on the following criteria:
    <ul>
    <li>{@link #getDemand() Demand}: This value is periodically updated by the
    villager that owns this merchant recipe based on how often the recipe has
    been used since it has been last restocked in relation to its
    {@link #getMaxUses maximum uses}. The amount by which the demand influences
    the amount of the first ingredient is scaled by the recipe's
    {@link #getPriceMultiplier price multiplier}, and can never be below zero.
    <li>{@link #getSpecialPrice() Special price}: This value is dynamically
    updated whenever a player starts and stops trading with a villager that owns
    this merchant recipe. It is based on the player's individual reputation with
    the villager, and the player's currently active status effects (see
    {@link PotionEffectType#HERO_OF_THE_VILLAGE}). The influence of the player's
    reputation on the special price is scaled by the recipe's
    {@link #getPriceMultiplier price multiplier}.
    </ul>
    The adjusted amount of the first ingredient is calculated by adding up the
    original amount of the first ingredient, the demand scaled by the recipe's
    {@link #getPriceMultiplier price multiplier} and truncated to the next lowest
    integer value greater than or equal to 0, and the special price, and then
    constraining the resulting value between <code>1</code> and the item stack's
    {@link ItemStack#getMaxStackSize() maximum stack size}.
    """

    def __init__(self: "MerchantRecipe", result: ItemStack, max_uses: int) -> None:
        ...

    def __init__(self: "MerchantRecipe", result: ItemStack, uses: int, max_uses: int, experience_reward: bool) -> None:
        ...

    def __init__(self: "MerchantRecipe", result: ItemStack, uses: int, max_uses: int, experience_reward: bool, villager_experience: int, price_multiplier: float) -> None:
        ...

    def __init__(self: "MerchantRecipe", result: ItemStack, uses: int, max_uses: int, experience_reward: bool, villager_experience: int, price_multiplier: float, demand: int, special_price: int) -> None:
        ...

        def get_result(self: "MerchantRecipe") -> ItemStack:
        ...

    def add_ingredient(self: "MerchantRecipe", item: ItemStack) -> None:
        ...

    def remove_ingredient(self: "MerchantRecipe", index: int) -> None:
        ...

    def set_ingredients(self: "MerchantRecipe", ingredients: List[ItemStack]) -> None:
        ...

        def get_ingredients(self: "MerchantRecipe") -> List[ItemStack]:
        ...

        def get_adjusted_ingredient_1(self: "MerchantRecipe") -> Optional[ItemStack]:
        ...

    def adjust(self: "MerchantRecipe", item_stack: Optional[ItemStack]) -> None:
        ...

    def get_demand(self: "MerchantRecipe") -> int:
        ...

    def set_demand(self: "MerchantRecipe", demand: int) -> None:
        ...

    def get_special_price(self: "MerchantRecipe") -> int:
        ...

    def set_special_price(self: "MerchantRecipe", special_price: int) -> None:
        ...

    def get_uses(self: "MerchantRecipe") -> int:
        ...

    def set_uses(self: "MerchantRecipe", uses: int) -> None:
        ...

    def get_max_uses(self: "MerchantRecipe") -> int:
        ...

    def set_max_uses(self: "MerchantRecipe", max_uses: int) -> None:
        ...

    def has_experience_reward(self: "MerchantRecipe") -> bool:
        ...

    def set_experience_reward(self: "MerchantRecipe", flag: bool) -> None:
        ...

    def get_villager_experience(self: "MerchantRecipe") -> int:
        ...

    def set_villager_experience(self: "MerchantRecipe", villager_experience: int) -> None:
        ...

    def get_price_multiplier(self: "MerchantRecipe") -> float:
        ...

    def set_price_multiplier(self: "MerchantRecipe", price_multiplier: float) -> None:
        ...