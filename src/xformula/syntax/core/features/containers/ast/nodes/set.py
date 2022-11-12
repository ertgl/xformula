import dataclasses

from xformula.syntax.ast.nodes.abc import Set as _Set
from xformula.syntax.ast.nodes.abc import SimpleExpression

__all__ = [
    "Set",
]


@dataclasses.dataclass()
class Set(
    _Set[SimpleExpression],
):

    elements: list[SimpleExpression] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )
