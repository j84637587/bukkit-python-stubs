"""A MetadataEvaluationException is thrown any time a {@link
LazyMetadataValue} fails to evaluate its value due to an exception. The
originating exception will be included as this exception's cause.
"""

from typing import Optional

class MetadataEvaluationException(RuntimeError):
    def __init__(self, cause: Optional[Exception]) -> None:
        ...