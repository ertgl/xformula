from xformula.syntax.grammar.regex._escape_char import escape_char

__all__ = [
    "word",
]


def word(chars: str) -> str:
    return "".join(map(escape_char, chars))
