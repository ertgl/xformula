from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import None_ as NoneNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "None_",
]


class None_(  # NOSONAR
    NonTerminal[NoneNode],
):
    class Meta:

        definition_name = "None"

        atomic = True

        tags = {
            non_terminal("Literal"): -1000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree,
    ) -> NoneNode:
        return NoneNode()
