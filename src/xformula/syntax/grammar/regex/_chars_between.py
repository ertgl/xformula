from xformula.syntax.grammar.regex._flat_join import flat_join

__all__ = [
    "chars_between",
]


def chars_between(
    lower: str,
    upper: str,
) -> str:
    return flat_join("-", [lower, upper])
