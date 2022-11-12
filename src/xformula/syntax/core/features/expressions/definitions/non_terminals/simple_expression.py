from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Node
from xformula.syntax.ast.nodes.abc import SimpleExpression as SimpleExpressionNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "SimpleExpression",
]


class SimpleExpression(
    NonTerminal[SimpleExpressionNode],
):
    class Meta:

        tags = {
            non_terminal("Start"): -1,
            non_terminal("CallArgument"): 1000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[Node],
    ) -> SimpleExpressionNode:
        return cast(SimpleExpressionNode, tree.children[0])
