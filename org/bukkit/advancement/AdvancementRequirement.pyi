from typing import List

class AdvancementRequirement:
    """
    Get all required criteria.
    
    @return the list of required criteria for this requirement.
    """
    def get_required_criteria(self) -> List[str]:
        ...

    """
    Check if the requirement is strict.
    
    @return true if requirement list contains one criteria, false if
    multiple.
    """
    def is_strict(self) -> bool:
        ...