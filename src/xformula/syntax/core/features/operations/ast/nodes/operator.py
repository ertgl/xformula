import dataclasses

from xformula.syntax.ast.nodes.abc import Arity, Associativity
from xformula.syntax.ast.nodes.abc import Operator as _Operator
from xformula.syntax.ast.nodes.abc import Placement, PrecedenceLevel, Symbol

__all__ = [
    "Operator",
]


@dataclasses.dataclass()
class Operator(_Operator):

    arity: Arity = dataclasses.field(
        kw_only=True,
        default=-1,
    )

    associativity: Associativity = dataclasses.field(
        kw_only=True,
        default=Associativity.UNDEFINED,
    )

    placement: Placement = dataclasses.field(
        kw_only=True,
        default=Placement.UNDEFINED,
    )

    precedence_level: PrecedenceLevel = dataclasses.field(
        kw_only=True,
        default=int(),
    )

    symbols: list[Symbol] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )
