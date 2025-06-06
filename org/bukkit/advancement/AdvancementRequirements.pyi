from typing import List
from typing import Protocol

class AdvancementRequirement:
    pass

class AdvancementRequirements(Protocol):
    """
    The list of requirements for the advancement.

    Requirements are complimentary to criteria. They are just lists that contain
    more lists, which in turn contains strings that equal the names of the
    criteria. Ultimately defining the logic around how criteria are completed in
    order to grant the advancement.

    @see <a href=https://minecraft.wiki/w/Advancement_definition>Advancement Definition</a>
    @see <a href=https://www.minecraftforum.net/forums/minecraft-java-edition/redstone-discussion-and/commands-command-blocks-and/2809368-1-12-custom-advancements-aka-achievements#Requirements>Advancement Requirements</a>
    """

    def get_requirements(self) -> List[AdvancementRequirement]:
        """
        Get all the requirements present in this advancement.

        @return an unmodifiable copy of all requirements.
        """
        ...