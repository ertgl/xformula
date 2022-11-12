from xformula.syntax.grammar.ebnf._directive import directive
from xformula.syntax.grammar.ebnf._flat_join import flat_join

__all__ = [
    "use_directive",
]


def use_directive(
    name: str,
    *expressions: str,
) -> str:
    return f"%{directive(name)} {flat_join(' ', expressions)}"
