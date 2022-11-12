from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Pair, SimpleExpression
from xformula.syntax.core.features.mappings.ast.nodes import Dict as DictNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Dict",
]


class Dict(
    NonTerminal[DictNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Primary"): 1000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        use_template = self.ebnf.use_template
        op = self.ebnf.op
        _non_terminal = self.ebnf.non_terminal

        return define(
            use_template(
                "WrapZeroOrMoreOf",
                op("{"),
                op("}"),
                _non_terminal("DictPair"),
            ),
        )

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[SimpleExpression],
    ) -> DictNode:
        return DictNode(
            elements=cast(
                list[Pair[SimpleExpression, SimpleExpression]],
                tree.children,
            ),
        )
