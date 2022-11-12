import dataclasses

from xformula.syntax.ast.nodes.abc import Symbol as _Symbol
from xformula.syntax.ast.nodes.abc import SymbolType

__all__ = [
    "Symbol",
]


@dataclasses.dataclass()
class Symbol(_Symbol):

    type: SymbolType = dataclasses.field(
        kw_only=True,
        default=SymbolType.UNDEFINED,
    )

    value: str = dataclasses.field(
        kw_only=True,
        default=str(),
    )
