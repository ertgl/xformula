__all__ = [
    "flat_one_or_more_of",
]


def flat_one_or_more_of(expression: str) -> str:
    if not expression:
        return ""
    return f"{expression}+"
