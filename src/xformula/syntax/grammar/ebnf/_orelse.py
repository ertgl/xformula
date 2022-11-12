from xformula.syntax.grammar.ebnf._flat_join import flat_join

__all__ = [
    "orelse",
]


def orelse(*expressions: str) -> str:
    return f"| {flat_join(' ', expressions)}"
