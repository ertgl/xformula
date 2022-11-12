import dataclasses

from xformula.syntax.ast.nodes.abc import Pair, SimpleExpression

__all__ = [
    "CallKeywordArgument",
]


@dataclasses.dataclass()
class CallKeywordArgument(
    Pair[SimpleExpression, SimpleExpression],
):

    elements: tuple[SimpleExpression, SimpleExpression] = dataclasses.field(
        kw_only=True,
        default_factory=lambda: (SimpleExpression(), SimpleExpression()),
    )
