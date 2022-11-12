from xformula.syntax.ast.nodes.abc.has_type import HasType
from xformula.syntax.ast.nodes.abc.has_value import HasValue
from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.symbol_type import SymbolType

__all__ = [
    "Symbol",
]


class Symbol(
    HasType[SymbolType],
    HasValue[str],
    Node,
):
    class Meta(
        HasType.Meta,
        HasValue.Meta,
        Node.Meta,
    ):
        abstract = True

        is_symbol = True
