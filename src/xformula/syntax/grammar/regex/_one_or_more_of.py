from xformula.syntax.grammar.regex._flat_join import flat_join

__all__ = [
    "one_or_more_of",
]


def one_or_more_of(*expressions: str) -> str:
    inner = flat_join("", expressions)
    if not inner:
        return ""
    return f"({inner})+"
