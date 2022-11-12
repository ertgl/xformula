__all__ = [
    "flat_optional",
]


def flat_optional(expression: str) -> str:
    if not expression:
        return ""
    return f"{expression}?"
