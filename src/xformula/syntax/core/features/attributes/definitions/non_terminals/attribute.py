from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Context, HasContext, Identifier, Node
from xformula.syntax.core.features.attributes.ast.nodes import (
    Attribute as AttributeNode,
)
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "Attribute",
]


class Attribute(
    NonTerminal[AttributeNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Term"): 15_000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        _non_terminal = self.ebnf.non_terminal
        op = self.ebnf.op
        orelse = self.ebnf.orelse
        suite = self.ebnf.suite

        return suite(
            define(_non_terminal("Attribute"), op("."), _non_terminal("Identifier")),
            orelse(_non_terminal("Primary"), op("."), _non_terminal("Identifier")),
        )

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[Node],
    ) -> AttributeNode:
        owner = cast(Node, tree.children[0])
        if owner.__class__.options.has_context_attribute:
            owner = cast(HasContext, owner)
            owner.context = getattr(
                owner.context.__class__,
                "LOAD",
                Context.LOAD,
            )
        name = cast(Identifier, tree.children[1])
        name.context = name.context.__class__.ATTRIBUTE
        return AttributeNode(
            owner=owner,
            name=name,
            context=Context.LOAD,
        )
