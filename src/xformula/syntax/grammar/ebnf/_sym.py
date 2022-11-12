from typing import TYPE_CHECKING

from xformula.syntax.grammar.ebnf._keyword import keyword
from xformula.syntax.grammar.ebnf._literal import literal
from xformula.syntax.grammar.ebnf._op import op

if TYPE_CHECKING:
    from xformula.syntax.ast.nodes.abc.symbol_type import SymbolType

__all__ = [
    "sym",
]


def sym(info: tuple["SymbolType", str]) -> str:
    from xformula.syntax.ast.nodes.abc import SymbolType

    if info[0] == SymbolType.KEYWORD:
        return keyword(info[1])

    if info[0] == SymbolType.OPERATOR:
        return op(info[1])

    return literal(info[1])
