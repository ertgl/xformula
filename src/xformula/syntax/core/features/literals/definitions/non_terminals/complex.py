from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import Complex as ComplexNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Complex",
]


class Complex(
    NonTerminal[ComplexNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Literal"): -5000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[complex],
    ) -> ComplexNode:
        value = cast(complex, tree.children[0])
        return ComplexNode(
            value=value,
        )
