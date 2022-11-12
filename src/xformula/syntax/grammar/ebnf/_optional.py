__all__ = [
    "optional",
]


def optional(*expressions: str) -> str:
    inner = " ".join(expressions)
    wrap = len(expressions) > 1 or " " in inner
    if wrap:
        return f"({inner})?"
    return f"{inner}?"
