from itertools import chain
from typing import TYPE_CHECKING

from xformula.syntax.grammar.ebnf._define_rule import define_rule

if TYPE_CHECKING:
    from xformula.syntax.core.context.abc.syntax_context import SyntaxContext

__all__ = [
    "document",
]


def document(syntax_context: "SyntaxContext") -> str:
    return "\n".join(
        chain(
            [
                "// Auto-generated via xformula.syntax module",
            ],
            [""],
            [
                f"{directive.build_grammar()}\n"
                for directive in syntax_context.directives[::-1]
            ],
            [""],
            [
                f"{define_rule(non_terminal)}\n"
                for non_terminal in syntax_context.non_terminals[::-1]
            ],
            [""],
            [
                f"{define_rule(template)}\n"
                for template in syntax_context.templates[::-1]
            ],
            [""],
            [
                f"{define_rule(terminal)}\n"
                for terminal in syntax_context.terminals[::-1]
            ],
        ),
    )
