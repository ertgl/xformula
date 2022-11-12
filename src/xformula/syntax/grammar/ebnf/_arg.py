__all__ = [
    "arg",
]


def arg(name: str) -> str:
    return f"_tmpl_arg__{name.lower()}"
