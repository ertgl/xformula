from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Context
from xformula.syntax.core.features.identifiers.ast.nodes import (
    Identifier as IdentifierNode,
)
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Identifier",
]


class Identifier(
    NonTerminal[IdentifierNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Term"): 10_000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[str],
    ) -> IdentifierNode:
        name = cast(str, tree.children[0])
        return IdentifierNode(
            name=name,
            context=Context.LOAD,
        )
