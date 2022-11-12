import dataclasses

from xformula.syntax.ast.nodes.abc import List as _List
from xformula.syntax.ast.nodes.abc import SimpleExpression

__all__ = [
    "List",
]


@dataclasses.dataclass()
class List(
    _List[SimpleExpression],
):

    elements: list[SimpleExpression] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )
