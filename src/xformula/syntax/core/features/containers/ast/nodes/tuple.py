import dataclasses

from xformula.syntax.ast.nodes.abc import SimpleExpression
from xformula.syntax.ast.nodes.abc import Tuple as _Tuple

__all__ = [
    "Tuple",
]


@dataclasses.dataclass()
class Tuple(
    _Tuple[SimpleExpression],
):

    elements: list[SimpleExpression] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )
