from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import Str as StrNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Str",
]


class Str(
    NonTerminal[StrNode],
):
    class Meta:

        definition_name = "Str"

        atomic = True

        tags = {
            non_terminal("Literal"): -6000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[str],
    ) -> StrNode:
        value = cast(str, tree.children[0])
        return StrNode(
            value=value,
        )
