from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Node
from xformula.syntax.core.features.calls.ast.nodes import Call as FunctionCallNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Call",
]


class Call(
    NonTerminal[FunctionCallNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Term"): 20_000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        _non_terminal = self.ebnf.non_terminal
        op = self.ebnf.op
        optional = self.ebnf.optional
        orelse = self.ebnf.orelse
        use_template = self.ebnf.use_template
        suite = self.ebnf.suite

        return suite(
            define(
                _non_terminal("Term"),
                op("("),
                use_template(
                    "SeparatedZeroOrMoreOf",
                    op(","),
                    _non_terminal("CallArgument"),
                ),
                op(","),
                use_template(
                    "SeparatedZeroOrMoreOf",
                    op(","),
                    _non_terminal("CallKeywordArgument"),
                ),
                optional(op(",")),
                op(")"),
            ),
            orelse(
                _non_terminal("Term"),
                op("("),
                use_template(
                    "SeparatedZeroOrMoreOf",
                    op(","),
                    _non_terminal("CallArgument"),
                ),
                optional(op(",")),
                op(")"),
            ),
            orelse(
                _non_terminal("Term"),
                op("("),
                use_template(
                    "SeparatedZeroOrMoreOf",
                    op(","),
                    _non_terminal("CallKeywordArgument"),
                ),
                optional(op(",")),
                op(")"),
            ),
            orelse(_non_terminal("Term"), op("("), op(")")),
        )

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[Node],
    ) -> FunctionCallNode:
        callee = cast(Node, tree.children[0])
        arguments = cast(list[Node], tree.children[1:])
        return FunctionCallNode(
            callee=callee,
            arguments=arguments,
        )
