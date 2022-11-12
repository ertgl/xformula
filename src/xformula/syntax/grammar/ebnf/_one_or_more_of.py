__all__ = [
    "one_or_more_of",
]


def one_or_more_of(*expressions: str) -> str:
    inner = " ".join(expressions)
    wrap = len(expressions) > 1 or " " in inner
    if wrap:
        return f"({inner})+"
    return f"{inner}+"
