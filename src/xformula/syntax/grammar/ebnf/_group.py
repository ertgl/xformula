from xformula.syntax.grammar.ebnf._flat_join import flat_join

__all__ = [
    "group",
]


def group(*expressions: str) -> str:
    inner = flat_join(" ", expressions)
    if not inner:
        return ""
    return f"({inner})"
