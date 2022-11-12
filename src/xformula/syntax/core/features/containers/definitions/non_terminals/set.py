from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import SimpleExpression
from xformula.syntax.core.features.containers.ast.nodes import Set as SetNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Set",
]


class Set(
    NonTerminal[SetNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Primary"): 2000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        use_template = self.ebnf.use_template
        op = self.ebnf.op
        _non_terminal = self.ebnf.non_terminal

        return define(
            use_template(
                "WrapOneOrMoreOf",
                op("{"),
                op("}"),
                _non_terminal("SimpleExpression"),
            ),
        )

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[SimpleExpression],
    ) -> SetNode:
        return SetNode(
            elements=cast(list[SimpleExpression], tree.children),
        )
