from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Primary as PrimaryNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Primary",
]


class Primary(
    NonTerminal[PrimaryNode],
):
    class Meta:

        tags = {
            non_terminal("Operand"): -1,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[bool],
    ) -> PrimaryNode:
        return cast(PrimaryNode, tree.children[0])
