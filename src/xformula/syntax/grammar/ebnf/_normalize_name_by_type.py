from typing import TYPE_CHECKING

from xformula.syntax.grammar.ebnf._directive import directive
from xformula.syntax.grammar.ebnf._non_terminal import non_terminal
from xformula.syntax.grammar.ebnf._template import template
from xformula.syntax.grammar.ebnf._terminal import terminal

if TYPE_CHECKING:
    from xformula.syntax.grammar.definitions.abc.definition_type import DefinitionType

__all__ = [
    "normalize_name_by_type",
]


def normalize_name_by_type(
    definition_type: "DefinitionType",
    name: str,
) -> str:
    from xformula.syntax.grammar.definitions.abc.definition_type import DefinitionType

    dispatcher = {
        DefinitionType.DIRECTIVE: directive,
        DefinitionType.TERMINAL: terminal,
        DefinitionType.TEMPLATE: template,
        DefinitionType.NON_TERMINAL: non_terminal,
    }

    normalize = dispatcher[definition_type]
    return normalize(name)
