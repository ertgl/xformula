from xformula.syntax.grammar.regex._flat_join import flat_join

__all__ = [
    "bound",
]


def bound(*expressions):
    inner = flat_join("", expressions)
    if not inner:
        return ""
    return rf"\b{inner}\b"
