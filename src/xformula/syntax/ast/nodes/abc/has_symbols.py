from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.symbol import Symbol

__all__ = [
    "HasSymbols",
]


class HasSymbols(Node):

    symbols: list[Symbol]

    class Meta(Node.Meta):

        abstract = True

        has_symbols_attribute = True
