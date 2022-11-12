from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import Int as IntNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Int",
]


class Int(
    NonTerminal[IntNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Literal"): -3000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[int],
    ) -> IntNode:
        value = cast(int, tree.children[0])
        return IntNode(
            value=value,
        )
