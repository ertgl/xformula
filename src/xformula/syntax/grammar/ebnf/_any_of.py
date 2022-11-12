from xformula.syntax.grammar.ebnf._flat_join import flat_join

__all__ = [
    "any_of",
]


def any_of(*expressions: str) -> str:
    return f"{flat_join(' | ', expressions)}"
