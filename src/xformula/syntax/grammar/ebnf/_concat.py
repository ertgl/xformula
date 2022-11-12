from typing import Iterable

from xformula.syntax.grammar.ebnf._flat_join import flat_join

__all__ = [
    "concat",
]


def concat(expressions: Iterable[str]) -> str:
    return flat_join(" ", expressions)
