from typing import TYPE_CHECKING, Any

from xformula.syntax.core.features.operations.runtime.reflection import (
    NonTerminalOperationClassBuilder,
)
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal

if TYPE_CHECKING:
    from xformula.syntax.core.context.abc.syntax_context import SyntaxContext

__all__ = [
    "NonTerminalOperationTypeGenerator",
]


class NonTerminalOperationTypeGenerator:
    @classmethod
    def generate(
        cls,
        syntax_context: "SyntaxContext",
    ) -> list[type[NonTerminal]]:
        generated_non_terminal_types: list[type[NonTerminal]] = []

        operand = non_terminal("Operand")

        for (
            operator_precedence_index,
            operator_precedence,
        ) in enumerate(syntax_context.operator_precedences):

            kwargs: dict[str, Any] = dict()

            if (
                operator_precedence_index
                == len(syntax_context.operator_precedences) - 1
            ):
                kwargs["tags"] = {
                    non_terminal("Operation"): 0,
                }

            generated_non_terminal_type = NonTerminalOperationClassBuilder.build(
                f"OperationLevel{operator_precedence_index + 1}",
                operator_precedence,
                operand,
                **kwargs,
            )

            generated_non_terminal_types.append(generated_non_terminal_type)
            operand = generated_non_terminal_type.options.definition_name

        return generated_non_terminal_types
