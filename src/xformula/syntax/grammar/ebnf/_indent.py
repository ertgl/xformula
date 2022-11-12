__all__ = [
    "indent",
]


def indent(
    *block: str,
    width: int = 4,
) -> str:
    width = max(4, width)

    tabs = "".join([(" " * 4) for _ in range(width // 4)])
    spaces = "".join([" " for _ in range(width % 4)])

    prefix = f"{tabs}{spaces}"

    return "\n".join(
        [
            f"{prefix}{line}".rstrip()
            for statement in block
            for line in statement.split("\n")
        ],
    )
