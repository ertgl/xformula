from typing import TYPE_CHECKING

from xformula.syntax.core.features.polyfill.runtime.reflection import (
    NonTerminalClassBuilder,
)
from xformula.syntax.grammar.non_terminals.abc import NonTerminal

if TYPE_CHECKING:
    from xformula.syntax.core.context.abc.syntax_context import SyntaxContext

__all__ = [
    "NonTerminalTypeGenerator",
]


class NonTerminalTypeGenerator:

    syntax_context: "SyntaxContext"

    missing_definitions: dict[str, set[str]]

    @classmethod
    def generate(
        cls,
        syntax_context: "SyntaxContext",
        missing_definitions: dict[str, set[str]],
    ) -> list[type[NonTerminal]]:
        generator = cls(syntax_context, missing_definitions)
        return generator.generate_types()

    def __init__(
        self,
        syntax_context: "SyntaxContext",
        missing_definitions: dict[str, set[str]],
    ) -> None:
        self.syntax_context = syntax_context
        self.missing_definitions = missing_definitions

    def generate_types(self) -> list[type[NonTerminal]]:
        generated_types: list[type[NonTerminal]] = []
        for name, alternation in self.missing_definitions.items():
            generated_type = NonTerminalClassBuilder.build(name, alternation)
            generated_types.append(generated_type)
        return generated_types
