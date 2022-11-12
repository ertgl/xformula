from xformula.syntax.grammar.ebnf._template import template

__all__ = [
    "use_template",
]


def use_template(
    name: str,
    *arguments: str,
) -> str:
    args = ", ".join(arguments)
    specify_args = "".join(["{", args, "}"])
    return f"{template(name)}{specify_args}"
