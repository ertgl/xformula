from typing import overload

from xformula.syntax.grammar.regex._flat_join import flat_join

__all__ = [
    "wrap",
]


@overload
def wrap(
    outer: str,
    inner: str,
) -> str:
    ...


@overload
def wrap(
    left: str,
    right: str,
    inner: str,
) -> str:
    ...


@overload
def wrap(
    left: str,
    right: str,
    *inner: str,
) -> str:
    ...


def wrap(*args):
    if len(args) == 2:
        return f"{args[0]}{args[1]}{args[0]}"
    if len(args) == 3:
        return f"{args[0]}{args[2]}{args[1]}"
    return f"{args[0]}{args[2]}{flat_join('', args[3:])}{args[1]}"
