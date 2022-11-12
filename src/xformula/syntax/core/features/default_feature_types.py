from xformula.syntax.core.features.attributes import AttributeFeature
from xformula.syntax.core.features.base import BaseFeature
from xformula.syntax.core.features.calls import CallFeature
from xformula.syntax.core.features.containers import ContainerFeature
from xformula.syntax.core.features.expressions import ExpressionFeature
from xformula.syntax.core.features.identifiers import IdentifierFeature
from xformula.syntax.core.features.literals import LiteralFeature
from xformula.syntax.core.features.mappings import MappingFeature
from xformula.syntax.core.features.operations import OperationFeature
from xformula.syntax.core.features.polyfill import PolyfillFeature
from xformula.syntax.core.features.primaries import PrimaryFeature
from xformula.syntax.core.features.separators import SeparatorFeature
from xformula.syntax.core.features.terms import TermFeature
from xformula.syntax.core.features.validation import ValidationFeature
from xformula.syntax.core.features.wrappers import WrapperFeature

__all__ = [
    "DEFAULT_FEATURE_TYPES",
]


DEFAULT_FEATURE_TYPES = [
    BaseFeature,
    SeparatorFeature,
    WrapperFeature,
    LiteralFeature,
    IdentifierFeature,
    AttributeFeature,
    CallFeature,
    TermFeature,
    ContainerFeature,
    MappingFeature,
    PrimaryFeature,
    OperationFeature,
    ExpressionFeature,
    PolyfillFeature,
    ValidationFeature,
]
