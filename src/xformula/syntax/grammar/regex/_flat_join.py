from typing import Iterable, cast

__all__ = [
    "flat_join",
]


def flat_join(
    separator: str,
    expressions: Iterable[str],
) -> str:
    return separator.join(
        cast(
            Iterable[str],
            filter(
                len,
                expressions,
            ),
        ),
    )
