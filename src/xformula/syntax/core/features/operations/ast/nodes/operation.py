import dataclasses

from xformula.syntax.ast.nodes.abc import Operand
from xformula.syntax.ast.nodes.abc import Operation as _Operation
from xformula.syntax.ast.nodes.abc import Operator

__all__ = [
    "Operation",
]


@dataclasses.dataclass()
class Operation(_Operation):

    operator: Operator = dataclasses.field(
        kw_only=True,
        default_factory=Operator,
    )

    operands: list[Operand] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )
