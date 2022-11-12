import dataclasses

from xformula.syntax.ast.nodes.abc import (
    Arity,
    Associativity,
    Placement,
    PrecedenceLevel,
    SymbolType,
)

__all__ = [
    "OperatorPrecedence",
]


@dataclasses.dataclass()
class OperatorPrecedence:

    arity: Arity = dataclasses.field(
        kw_only=True,
        default=0,
    )

    associativity: Associativity = dataclasses.field(
        kw_only=True,
        default=Associativity.UNDEFINED,
    )

    level: PrecedenceLevel = dataclasses.field(
        kw_only=True,
        default=int(),
    )

    placement: Placement = dataclasses.field(
        kw_only=True,
        default=Placement.UNDEFINED,
    )

    symbols: list[tuple[SymbolType, str]] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )
