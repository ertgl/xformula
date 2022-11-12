from xformula.syntax.grammar.regex._flat_join import flat_join

__all__ = [
    "zero_or_more_of",
]


def zero_or_more_of(*expressions: str) -> str:
    inner = flat_join("", expressions)
    if not inner:
        return ""
    return f"({inner})+"
