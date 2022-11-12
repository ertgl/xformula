from typing import TYPE_CHECKING

from xformula.syntax.grammar.ebnf._indent import indent

if TYPE_CHECKING:
    from xformula.syntax.grammar.definitions.abc.definition import Definition

__all__ = [
    "define_rule",
]


def define_rule(definition: "Definition") -> str:
    from xformula.syntax.grammar.definitions.abc import DefinitionType

    header = definition.__class__.options.definition_name
    extra_indent_width = 1

    if definition.__class__.options.retain_anonymous_literals:
        header = f"!{header}"

    if (
        definition.__class__.options.type == DefinitionType.NON_TERMINAL
        and not definition.__class__.options.atomic
    ):
        header = f"?{header}"

    if definition.__class__.options.type == DefinitionType.TEMPLATE:
        args = ", ".join(definition.__class__.options.arguments)
        specify_args = "".join(["{", args, "}"])
        header = f"{header}{specify_args}"

    if definition.__class__.options.priority != 0:
        header = f"{header}.{definition.__class__.options.priority}"

    indent_width = len(header) + extra_indent_width

    grammar = definition.build_grammar()

    lines = grammar.split("\n")
    first_body_line, rest_body_lines = lines[0], lines[1:]

    formatted_first_line = f"{header} : {first_body_line}"
    formatted_trailing_lines = indent(*rest_body_lines, width=indent_width)

    formatted_body_split = [formatted_first_line]
    if formatted_trailing_lines:
        formatted_body_split.append(formatted_trailing_lines)

    formatted_grammar = "\n".join(formatted_body_split)

    return formatted_grammar
