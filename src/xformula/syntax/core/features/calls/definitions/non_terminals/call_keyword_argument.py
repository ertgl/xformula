from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Context, Identifier, SimpleExpression
from xformula.syntax.core.features.calls.ast.nodes import (
    CallKeywordArgument as FunctionCallKeywordArgumentNode,
)
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "CallKeywordArgument",
]


class CallKeywordArgument(
    NonTerminal[FunctionCallKeywordArgumentNode],
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
                op("="),
                _non_terminal("Identifier"),
                _non_terminal("SimpleExpression"),
            ),
        )

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[
            tuple[SimpleExpression, SimpleExpression],
        ],
    ) -> FunctionCallKeywordArgumentNode:
        elements = cast(
            tuple[SimpleExpression, SimpleExpression],
            tuple(tree.children),
        )
        key = elements[0]
        value = elements[1]
        if isinstance(key, Identifier):
            key.context = Context.KEYWORD_ARGUMENT
        return FunctionCallKeywordArgumentNode(
            elements=(key, value),
        )
