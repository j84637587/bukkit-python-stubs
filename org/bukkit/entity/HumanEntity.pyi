from typing import Collection, Set, Optional

from org.bukkit import GameMode, Location, Material, NamespacedKey
from org.bukkit.inventory import Inventory, InventoryHolder, InventoryView, ItemStack, MainHand, PlayerInventory, Merchant
from org.bukkit.inventory.meta import FireworkMeta
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a human entity, such as an NPC or a player
"""
class HumanEntity(LivingEntity, AnimalTamer, InventoryHolder):

        def get_name(self) -> str:
        """Returns the name of this player

        Returns:
            Player name
        """
        ...

        def get_inventory(self) -> PlayerInventory:
        """Get the player's inventory.

        Returns:
            The inventory of the player, this also contains the armor slots.
        """
        ...

        def get_ender_chest(self) -> Inventory:
        """Get the player's EnderChest inventory

        Returns:
            The EnderChest of the player
        """
        ...

        def get_main_hand(self) -> MainHand:
        """Gets the player's selected main hand

        Returns:
            the players main hand
        """
        ...

    @Deprecated(for_removal=True, since="1.21")
    def set_window_property(self, prop: InventoryView.Property, value: int) -> bool:
        """If the player currently has an inventory window open, this method will
        set a property of that window, such as the state of a progress bar.

        Args:
            prop: The property.
            value: The value to set the property to.

        Returns:
            True if the property was successfully set.
        """
        ...

    def get_enchantment_seed(self) -> int:
        """Gets the player's current enchantment seed.

        The Seed is used to generate enchantment options in the enchanting table
        for the player.

        Returns:
            the player's enchantment seed
        """
        ...

    def set_enchantment_seed(self, seed: int) -> None:
        """Sets the player's enchantment seed.

        The Seed is used to generate enchantment options in the enchanting table
        for the player.

        Args:
            seed: the player's new enchantment seed
        """
        ...

        def get_open_inventory(self) -> InventoryView:
        """Gets the inventory view the player is currently viewing. If they do not
        have an inventory window open, it returns their internal crafting view.

        Returns:
            The inventory view.
        """
        ...

        def open_inventory(self, inventory: Inventory) -> Optional[InventoryView]:
        """Opens an inventory window with the specified inventory on the top and
        the player's inventory on the bottom.

        Args:
            inventory: The inventory to open

        Returns:
            The newly opened inventory view
        """
        ...

    @Deprecated(since="1.21.4")
        def open_workbench(self, location: Optional[Location], force: bool) -> Optional[InventoryView]:
        """Opens an empty workbench inventory window with the player's inventory
        on the bottom.

        Args:
            location: The location to attach it to. If null, the player's
                location is used.
            force: If false, and there is no workbench block at the location,
                no inventory will be opened and null will be returned.

        Returns:
            The newly opened inventory view, or null if it could not be
            opened.
        """
        ...

    @Deprecated(since="1.21.4")
        def open_enchanting(self, location: Optional[Location], force: bool) -> Optional[InventoryView]:
        """Opens an empty enchanting inventory window with the player's inventory
        on the bottom.

        Args:
            location: The location to attach it to. If null, the player's
                location is used.
            force: If false, and there is no enchanting table at the
                location, no inventory will be opened and null will be returned.

        Returns:
            The newly opened inventory view, or null if it could not be
            opened.
        """
        ...

    def open_inventory(self, inventory: InventoryView) -> None:
        """Opens an inventory window to the specified inventory view.

        The player associated with the InventoryView must be the same as this
        instance of HumanEntity.

        Args:
            inventory: The view to open
        """
        ...

    @Deprecated(since="1.21.4")
        def open_merchant(self, trader: Merchant, force: bool) -> Optional[InventoryView]:
        """Starts a trade between the player and the merchant.

        Note that only one player may trade with a merchant at once. You must use
        the force parameter for this.

        Args:
            merchant: The merchant to trade with. Cannot be null.
            force: whether to force the trade even if another player is trading

        Returns:
            The newly opened inventory view, or null if it could not be
            opened.
        """
        ...

    def close_inventory(self) -> None:
        """Force-closes the currently open inventory view for this player, if any."""
        ...

    @Deprecated(since="1.9")
        def get_item_in_hand(self) -> ItemStack:
        """Returns the ItemStack currently in your hand, can be empty.

        Returns:
            The ItemStack of the item you are currently holding.
        """
        ...

    @Deprecated(since="1.9")
    def set_item_in_hand(self, item: Optional[ItemStack]) -> None:
        """Sets the item to the given ItemStack, this will replace whatever the
        user was holding.

        Args:
            item: The ItemStack which will end up in the hand
        """
        ...

        def get_item_on_cursor(self) -> ItemStack:
        """Returns the ItemStack currently on your cursor, can be empty. Will
        always be empty if the player currently has no open window.

        Returns:
            The ItemStack of the item you are currently moving around.
        """
        ...

    def set_item_on_cursor(self, item: Optional[ItemStack]) -> None:
        """Sets the item to the given ItemStack, this will replace whatever the
        user was moving. Will always be empty if the player currently has no
        open window.

        Args:
            item: The ItemStack which will end up in the hand
        """
        ...

    def has_cooldown(self, material: Material) -> bool:
        """Check whether a cooldown is active on the specified material.

        Args:
            material: the material to check

        Returns:
            if a cooldown is active on the material

        Raises:
            IllegalArgumentException: if the material is not an item
        """
        ...

    def get_cooldown(self, material: Material) -> int:
        """Get the cooldown time in ticks remaining for the specified material.

        Args:
            material: the material to check

        Returns:
            the remaining cooldown time in ticks

        Raises:
            IllegalArgumentException: if the material is not an item
        """
        ...

    def set_cooldown(self, material: Material, ticks: int) -> None:
        """Set a cooldown on the specified material for a certain amount of ticks.
        ticks. 0 ticks will result in the removal of the cooldown.

        Cooldowns are used by the server for items such as ender pearls and
        shields to prevent them from being used repeatedly.

        Note that cooldowns will not by themselves stop an item from being used
        for attacking.

        Args:
            material: the material to set the cooldown for
            ticks: the amount of ticks to set or 0 to remove

        Raises:
            IllegalArgumentException: if the material is not an item
        """
        ...

    def has_cooldown(self, item: ItemStack) -> bool:
        """Check whether a cooldown is active on the specified item.

        Args:
            item: the item to check

        Returns:
            if a cooldown is active on the item
        """
        ...

    def get_cooldown(self, item: ItemStack) -> int:
        """Get the cooldown time in ticks remaining for the specified item.

        Args:
            item: the item to check

        Returns:
            the remaining cooldown time in ticks
        """
        ...

    def set_cooldown(self, item: ItemStack, ticks: int) -> None:
        """Set a cooldown on the specified item for a certain amount of ticks.
        ticks. 0 ticks will result in the removal of the cooldown.

        Cooldowns are used by the server for items such as ender pearls and
        shields to prevent them from being used repeatedly.

        Note that cooldowns will not by themselves stop an item from being used
        for attacking.

        Args:
            item: the item to set the cooldown for
            ticks: the amount of ticks to set or 0 to remove
        """
        ...

    def get_sleep_ticks(self) -> int:
        """Get the sleep ticks of the player. This value may be capped.

        Returns:
            slumber ticks
        """
        ...

    def sleep(self, location: Location, force: bool) -> bool:
        """Attempts to make the entity sleep at the given location.

        The location must be in the current world and have a bed placed at the
        location. The game may also enforce other requirements such as proximity
        to bed, monsters, and dimension type if force is not set.

        Args:
            location: the location of the bed
            force: whether to try and sleep at the location even if not
                normally possible

        Returns:
            whether the sleep was successful
        """
        ...

    def wakeup(self, set_spawn_location: bool) -> None:
        """Causes the player to wakeup if they are currently sleeping.

        Args:
            set_spawn_location: whether to set their spawn location to the bed
                they are currently sleeping in

        Raises:
            IllegalStateException: if not sleeping
        """
        ...

    def start_riptide_attack(self, duration: int, attack_strength: float, attack_item: Optional[ItemStack]) -> None:
        """Make the player start a riptide spin attack.

        Args:
            duration: spin attack duration in ticks.
            attack_strength: damage value inflicted upon entities hit by spin attack.
            attack_item: item used to attack.
        """
        ...

        def get_bed_location(self) -> Location:
        """Gets the location of the bed the player is currently sleeping in

        Returns:
            location

        Raises:
            IllegalStateException: if not sleeping
        """
        ...

        def get_game_mode(self) -> GameMode:
        """Gets this human's current GameMode

        Returns:
            Current game mode
        """
        ...

    def set_game_mode(self, mode: GameMode) -> None:
        """Sets this human's current GameMode

        Args:
            mode: New game mode
        """
        ...

    def is_blocking(self) -> bool:
        """Check if the player is currently blocking (ie with a shield).

        Returns:
            Whether they are blocking.
        """
        ...

    def is_hand_raised(self) -> bool:
        """Check if the player currently has their hand raised (ie about to begin
        blocking).

        Returns:
            Whether their hand is raised
        """
        ...

    def get_exp_to_level(self) -> int:
        """Get the total amount of experience required for the player to level

        Returns:
            Experience required to level up
        """
        ...

    def get_attack_cooldown(self) -> float:
        """Gets the current cooldown for a player's attack.

        This is used to calculate damage, with 1.0 representing a fully charged
        attack and 0.0 representing a non-charged attack

        Returns:
            A float between 0.0-1.0 representing the progress of the charge
        """
        ...

    def discover_recipe(self, recipe: NamespacedKey) -> bool:
        """Discover a recipe for this player such that it has not already been
        discovered. This method will add the key's associated recipe to the
        player's recipe book.

        Args:
            recipe: the key of the recipe to discover

        Returns:
            whether or not the recipe was newly discovered
        """
        ...

    def discover_recipes(self, recipes: Collection[NamespacedKey]) -> int:
        """Discover a collection of recipes for this player such that they have not
        already been discovered. This method will add the keys' associated
        recipes to the player's recipe book. If a recipe in the provided
        collection has already been discovered, it will be silently ignored.

        Args:
            recipes: the keys of the recipes to discover

        Returns:
            the amount of newly discovered recipes where 0 indicates that
            none were newly discovered and a number equal to recipes.size()
            indicates that all were new
        """
        ...

    def undiscover_recipe(self, recipe: NamespacedKey) -> bool:
        """Undiscover a recipe for this player such that it has already been
        discovered. This method will remove the key's associated recipe from the
        player's recipe book.

        Args:
            recipe: the key of the recipe to undiscover

        Returns:
            whether or not the recipe was successfully undiscovered (i.e. it
            was previously discovered)
        """
        ...

    def undiscover_recipes(self, recipes: Collection[NamespacedKey]) -> int:
        """Undiscover a collection of recipes for this player such that they have
        already been discovered. This method will remove the keys' associated
        recipes from the player's recipe book. If a recipe in the provided
        collection has not yet been discovered, it will be silently ignored.

        Args:
            recipes: the keys of the recipes to undiscover

        Returns:
            the amount of undiscovered recipes where 0 indicates that none
            were undiscovered and a number equal to recipes.size() indicates
            that all were undiscovered
        """
        ...

    def has_discovered_recipe(self, recipe: NamespacedKey) -> bool:
        """Check whether or not this entity has discovered the specified recipe.

        Args:
            recipe: the key of the recipe to check

        Returns:
            true if discovered, false otherwise
        """
        ...

        def get_discovered_recipes(self) -> Set[NamespacedKey]:
        """Get an immutable set of recipes this entity has discovered.

        Returns:
            all discovered recipes
        """
        ...

    @Deprecated(since="1.12")
        def get_shoulder_entity_left(self) -> Optional[Entity]:
        """Gets the entity currently perched on the left shoulder or null if no
        entity.

        The returned entity will not be spawned within the world, so most
        operations are invalid unless the entity is first spawned in.

        Returns:
            left shoulder entity
        """
        ...

    @Deprecated(since="1.12")
    def set_shoulder_entity_left(self, entity: Optional[Entity]) -> None:
        """Sets the entity currently perched on the left shoulder, or null to
        remove. This method will remove the entity from the world.

        Note that only a copy of the entity will be set to display on the
        shoulder.

        Args:
            entity: left shoulder entity
        """
        ...

    @Deprecated(since="1.12")
        def get_shoulder_entity_right(self) -> Optional[Entity]:
        """Gets the entity currently perched on the right shoulder or null if no
        entity.

        The returned entity will not be spawned within the world, so most
        operations are invalid unless the entity is first spawned in.

        Returns:
            right shoulder entity
        """
        ...

    @Deprecated(since="1.12")
    def set_shoulder_entity_right(self, entity: Optional[Entity]) -> None:
        """Sets the entity currently perched on the right shoulder, or null to
        remove. This method will remove the entity from the world.

        Note that only a copy of the entity will be set to display on the
        shoulder.

        Args:
            entity: right shoulder entity
        """
        ...

    def drop_item(self, drop_all: bool) -> bool:
        """Make the entity drop the item in their hand.

        This will force the entity to drop the item they are holding with
        an option to drop the entire ItemStack or just 1 of the items.

        Args:
            drop_all: True to drop entire stack, false to drop 1 of the stack

        Returns:
            True if item was dropped successfully
        """
        ...

    def get_exhaustion(self) -> float:
        """Gets the players current exhaustion level.

        Exhaustion controls how fast the food level drops. While you have a
        certain amount of exhaustion, your saturation will drop to zero, and
        then your food will drop to zero.

        Returns:
            Exhaustion level
        """
        ...

    def set_exhaustion(self, value: float) -> None:
        """Sets the players current exhaustion level

        Args:
            value: Exhaustion level
        """
        ...

    def get_saturation(self) -> float:
        """Gets the players current saturation level.

        Saturation is a buffer for food level. Your food level will not drop if
        you are saturated > 0.

        Returns:
            Saturation level
        """
        ...

    def set_saturation(self, value: float) -> None:
        """Sets the players current saturation level

        Args:
            value: Saturation level
        """
        ...

    def get_food_level(self) -> int:
        """Gets the players current food level

        Returns:
            Food level
        """
        ...

    def set_food_level(self, value: int) -> None:
        """Sets the players current food level

        Args:
            value: New food level
        """
        ...

    def get_saturated_regen_rate(self) -> int:
        """Get the regeneration rate (1 health per x ticks) of
        the HumanEntity when they have saturation and
        their food level is >= 20. Default is 10.

        Returns:
            the regeneration rate
        """
        ...

    def set_saturated_regen_rate(self, ticks: int) -> None:
        """Set the regeneration rate (1 health per x ticks) of
        the HumanEntity when they have saturation and
        their food level is >= 20. Default is 10.
        Not affected if the world's difficulty is peaceful.

        Args:
            ticks: the amount of ticks to gain 1 health.
        """
        ...

    def get_unsaturated_regen_rate(self) -> int:
        """Get the regeneration rate (1 health per x ticks) of
        the HumanEntity when they have no saturation and
        their food level is >= 18. Default is 80.

        Returns:
            the regeneration rate
        """
        ...

    def set_unsaturated_regen_rate(self, ticks: int) -> None:
        """Get the regeneration rate (1 health per x ticks) of
        the HumanEntity when they have no saturation and
        their food level is >= 18. Default is 80.
        Not affected if the world's difficulty is peaceful.

        Args:
            ticks: the amount of ticks to gain 1 health.
        """
        ...

    def get_starvation_rate(self) -> int:
        """Get the starvation rate (1 health per x ticks) of
        the HumanEntity. Default is 80.

        Returns:
            the starvation rate
        """
        ...

    def set_starvation_rate(self, ticks: int) -> None:
        """Get the starvation rate (1 health per x ticks) of
        the HumanEntity. Default is 80.

        Args:
            ticks: the amount of ticks to lose 1 health
        """
        ...

        def get_last_death_location(self) -> Optional[Location]:
        """Gets the player's last death location.

        Returns:
            the last death location if it exists, otherwise null.
        """
        ...

    def set_last_death_location(self, location: Optional[Location]) -> None:
        """Sets the player's last death location.

        Note: This data is updated in the player's client only when the
        player respawns.

        Args:
            location: where to set the last death player location
        """
        ...

        def firework_boost(self, firework_item_stack: ItemStack) -> Optional[Firework]:
        """Perform a firework boost.

        This method will only work such that is_gliding() is true and
        the entity is actively gliding with an elytra. Additionally, the supplied
        firework_item_stack must be a firework rocket. The power of the boost
        will directly correlate to FireworkMeta.getPower().

        Args:
            firework_item_stack: the firework item stack to use to glide

        Returns:
            the attached Firework, or null if the entity could not
            be boosted

        Raises:
            IllegalArgumentException: if the firework_item_stack is not a firework
        """
        ...