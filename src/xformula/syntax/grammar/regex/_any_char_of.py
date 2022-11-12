from typing import Iterable, cast

from xformula.syntax.grammar.regex._escape_char import escape_char

__all__ = [
    "any_char_of",
]


def any_char_of(*chars: str) -> str:
    inner = "".join(
        map(
            escape_char,
            cast(
                Iterable[str],
                filter(
                    len,
                    chars,
                ),
            ),
        ),
    )
    if not inner:
        return ""
    return f"[{inner}]"
