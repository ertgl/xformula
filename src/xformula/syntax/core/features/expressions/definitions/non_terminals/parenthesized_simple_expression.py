from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import SimpleExpression as SimpleExpressionNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "ParenthesizedSimpleExpression",
]


class ParenthesizedSimpleExpression(
    NonTerminal[SimpleExpressionNode],
):
    class Meta:

        tags = {
            non_terminal("Term"): 25_000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        _non_terminal = self.ebnf.non_terminal
        op = self.ebnf.op

        return define(
            op("("),
            _non_terminal("SimpleExpression"),
            op(")"),
        )

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[bool],
    ) -> SimpleExpressionNode:
        return cast(SimpleExpressionNode, tree.children[0])
