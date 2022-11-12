from typing import TYPE_CHECKING, Union

from xformula.syntax.grammar.ebnf._normalize_name_by_type import normalize_name_by_type

if TYPE_CHECKING:
    from xformula.syntax.grammar.definitions.abc.definition import Definition

__all__ = [
    "get_normalized_name_by_definition",
]


def get_normalized_name_by_definition(
    definition: Union[
        "Definition",
        type["Definition"],
    ],
) -> str:
    from xformula.syntax.grammar.definitions.abc import Definition

    definition_type = (
        definition.__class__ if isinstance(definition, Definition) else definition
    )

    return normalize_name_by_type(
        definition_type.options.type,
        definition_type.options.definition_name,
    )
