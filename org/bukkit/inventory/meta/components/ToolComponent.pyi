from typing import Collection, List, Optional
from org.bukkit import Material
from org.bukkit import Tag
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

"""
Represents a component which can turn any item into a tool.
"""
class ToolComponent(ConfigurationSerializable):

    """
    Get the default mining speed of this tool. This value is used by the tool
    if no rule explicitly overrides it. 1.0 is standard mining speed.

    @return: the default mining speed
    @see: ToolRule#getSpeed()
    """
    def get_default_mining_speed(self) -> float: ...

    """
    Set the default mining speed of this tool. This value is used by the tool
    if no rule explicitly overrides it. 1.0 is standard mining speed.

    @param speed: the speed to set
    """
    def set_default_mining_speed(self, speed: float) -> None: ...

    """
    Get the amount of durability to be removed from the tool each time a
    block is broken.

    @return: the damage per block
    """
    def get_damage_per_block(self) -> int: ...

    """
    Set the amount of durability to be removed from the tool each time a
    block is broken.

    @param damage: the damage to set. Must be 0 or a positive integer
    """
    def set_damage_per_block(self, damage: int) -> None: ...

    """
    Get whether this tool can destroy blocks in creative.

    @return: whether can destroy
    """
    def can_destroy_blocks_in_creative(self) -> bool: ...

    """
    Set whether this tool can destroy blocks in creative.

    @param destroy: whether can destroy
    """
    def set_can_destroy_blocks_in_creative(self, destroy: bool) -> None: ...

    """
    Get the list of {@link ToolRule ToolRules} that apply to this tool.

    @return: all tool rules. The mutability of the returned list cannot be
    guaranteed, but its contents are mutable and can have their values
    changed
    """
        def get_rules(self) -> List['ToolRule']: ...

    """
    Set the list of {@link ToolRule ToolRules} to apply to this tool. This
    will remove any existing tool rules.

    @param rules: the rules to set
    """
    def set_rules(self, rules: List['ToolRule']) -> None: ...

    """
    Add a new rule to this tool component, which provides further information
    about a specific block type.

    @param block: the block type to which the rule applies
    @param speed: the mining speed to use when mining the block, or null to
    use the default mining speed
    @param correct_for_drops: whether or not this tool, when mining the block,
    is considered the optimal tool for the block and will drop its items when
    broken, or null to use the default tool checking behavior defined by
    Minecraft
    @return: the {@link ToolRule} instance that was added to this tool
    """
        def add_rule(self, block: Material, speed: Optional[float], correct_for_drops: Optional[bool]) -> 'ToolRule': ...

    """
    Add a new rule to this tool component, which provides further information
    about a collection of block types.

    @param blocks: the block types to which the rule applies
    @param speed: the mining speed to use when mining one of the blocks, or
    null to use the default mining speed
    @param correct_for_drops: whether or not this tool, when mining one of the
    blocks, is considered the optimal tool for the block and will drop its
    items when broken, or null to use the default tool checking behavior
    defined by Minecraft
    @return: the {@link ToolRule} instance that was added to this tool
    """
        def add_rule(self, blocks: Collection[Material], speed: Optional[float], correct_for_drops: Optional[bool]) -> 'ToolRule': ...

    """
    Add a new rule to this tool component, which provides further information
    about a collection of block types represented by a block {@link Tag}.

    @param tag: the block tag containing block types to which the rule
    applies.
    @param speed: the mining speed to use when mining one of the blocks, or
    null to use the default mining speed
    @param correct_for_drops: whether or not this tool, when mining one of the
    blocks, is considered the optimal tool for the block and will drop its
    items when broken, or null to use the default tool checking behavior
    defined by Minecraft
    @return: the {@link ToolRule} instance that was added to this tool
    @throws IllegalArgumentException: if the passed {@code tag} is not a block
    tag
    """
        def add_rule(self, tag: Tag[Material], speed: Optional[float], correct_for_drops: Optional[bool]) -> 'ToolRule': ...

    """
    Remove the given {@link ToolRule} from this tool.

    @param rule: the rule to remove
    @return: true if the rule was removed, false if this component did not
    contain a matching rule
    """
    def remove_rule(self, rule: 'ToolRule') -> bool: ...

    """
    A rule governing use of this tool and overriding attributes per-block.
    """
    class ToolRule(ConfigurationSerializable):

        """
        Get a collection of the block types to which this tool rule applies.

        @return: the blocks
        """
                def get_blocks(self) -> Collection[Material]: ...

        """
        Set the block type to which this rule applies.

        @param block: the block type
        """
        def set_blocks(self, block: Material) -> None: ...

        """
        Set the block types to which this rule applies.

        @param blocks: the block types
        """
        def set_blocks(self, blocks: Collection[Material]) -> None: ...

        """
        Set the block types (represented as a block {@link Tag}) to which
        this rule applies.

        @param tag: the block tag
        @throws IllegalArgumentException: if the passed {@code tag} is not a
        block tag
        """
        def set_blocks(self, tag: Tag[Material]) -> None: ...

        """
        Get the mining speed of this rule. If non-null, this speed value is
        used in lieu of the default speed value of the tool. 1.0 is standard
        mining speed.

        @return: the mining speed, or null if the default speed is used
        """
                def get_speed(self) -> Optional[float]: ...

        """
        Set the mining speed of this rule. 1.0 is standard mining speed.

        @param speed: the mining speed, or null to use the default speed
        """
        def set_speed(self, speed: Optional[float]) -> None: ...

        """
        Get whether or not this rule is considered the optimal tool for the
        blocks listed by this rule and will drop items. If non-null, this
        value is used in lieu of the default tool checking behavior defined
        by Minecraft.

        @return: true if correct for drops, false otherwise, or null to
        fallback to vanilla tool checking behavior
        """
                def is_correct_for_drops(self) -> Optional[bool]: ...

        """
        Set whether or not this rule is considered the optimal tool for the
        blocks listed by this rule and will drop items.

        @param correct: whether or not this rule is correct for drops, or null
        to fallback to vanilla tool checking behavior
        """
        def set_correct_for_drops(self, correct: Optional[bool]) -> None: ...