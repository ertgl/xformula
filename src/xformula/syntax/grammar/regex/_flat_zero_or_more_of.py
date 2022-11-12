__all__ = [
    "flat_zero_or_more_of",
]


def flat_zero_or_more_of(expression: str) -> str:
    if not expression:
        return ""
    return f"{expression}*"
