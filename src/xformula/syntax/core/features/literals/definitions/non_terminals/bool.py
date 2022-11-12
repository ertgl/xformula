from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import Bool as BoolNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Bool",
]


class Bool(
    NonTerminal[BoolNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Literal"): -2000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[bool],
    ) -> BoolNode:
        value = cast(bool, tree.children[0])
        return BoolNode(
            value=value,
        )
