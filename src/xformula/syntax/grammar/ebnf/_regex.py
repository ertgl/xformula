from xformula.syntax.grammar.regex import flat_join

__all__ = [
    "regex",
]


def regex(*expressions: str) -> str:
    return f"/{flat_join('', expressions)}/"
