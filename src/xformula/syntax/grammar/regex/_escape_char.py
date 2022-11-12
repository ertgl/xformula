import string

__all__ = [
    "escape_char",
]


def escape_char(char: str) -> str:
    if len(char) > 1:
        return char
    if char.isspace():
        return r"(\s+)"
    if char in string.punctuation:
        return rf"\{char}"
    return char
