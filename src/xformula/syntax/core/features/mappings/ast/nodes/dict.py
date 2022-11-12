import dataclasses

from xformula.syntax.ast.nodes.abc import Dict as _Dict
from xformula.syntax.ast.nodes.abc import Pair, SimpleExpression

__all__ = [
    "Dict",
]


@dataclasses.dataclass()
class Dict(
    _Dict[SimpleExpression, SimpleExpression],
):

    elements: list[Pair[SimpleExpression, SimpleExpression]] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )
