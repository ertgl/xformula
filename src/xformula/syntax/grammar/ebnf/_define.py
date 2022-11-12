from xformula.syntax.grammar.ebnf._flat_join import flat_join

__all__ = [
    "define",
]


def define(*expressions: str) -> str:
    return flat_join(" ", expressions)
