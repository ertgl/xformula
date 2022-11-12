from typing import Iterable, cast

__all__ = [
    "suite",
]


def suite(*lines: str) -> str:
    return "\n".join(
        cast(
            Iterable[str],
            filter(
                len,
                lines,
            ),
        ),
    )
