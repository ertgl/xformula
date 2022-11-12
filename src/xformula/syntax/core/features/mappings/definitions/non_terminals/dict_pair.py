from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import SimpleExpression
from xformula.syntax.core.features.mappings.ast.nodes import DictPair as DictPairNode
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "DictPair",
]


class DictPair(
    NonTerminal[DictPairNode],
):
    class Meta:

        atomic = True

    def build_grammar(self) -> str:
        define = self.ebnf.define
        use_template = self.ebnf.use_template
        op = self.ebnf.op
        _non_terminal = self.ebnf.non_terminal

        return define(
            use_template(
                "SeparatedPair",
                op(":"),
                _non_terminal("SimpleExpression"),
                _non_terminal("SimpleExpression"),
            ),
        )

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[SimpleExpression],
    ) -> DictPairNode:
        elements = cast(
            tuple[SimpleExpression, SimpleExpression],
            tuple(tree.children),
        )
        return DictPairNode(
            elements=elements,
        )
