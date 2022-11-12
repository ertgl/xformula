from typing import TypeVar, cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Literal as LiteralNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Literal",
]


T = TypeVar("T")


class Literal(
    NonTerminal[
        LiteralNode[T],
    ],
):
    class Meta:

        tags = {
            non_terminal("Term"): 5_000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[T],
    ) -> LiteralNode[T]:
        return cast(LiteralNode, tree.children[0])
