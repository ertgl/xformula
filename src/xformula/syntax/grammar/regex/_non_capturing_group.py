from xformula.syntax.grammar.regex._flat_join import flat_join

__all__ = [
    "non_capturing_group",
]


def non_capturing_group(*expressions: str) -> str:
    inner = flat_join("", expressions)
    if not inner:
        return ""
    return f"(?:{inner})"
