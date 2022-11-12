from xformula.syntax.grammar.regex._flat_join import flat_join

__all__ = [
    "flat",
]


def flat(*expressions: str) -> str:
    return flat_join("", expressions)
