from xformula.syntax.grammar.regex._flat_join import flat_join

__all__ = [
    "any_of",
]


def any_of(*expressions: str) -> str:
    return flat_join("|", expressions)
