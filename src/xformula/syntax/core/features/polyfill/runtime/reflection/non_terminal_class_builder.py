from itertools import chain
from typing import Any

from xformula.arch.runtime.reflection import ClassBuilder
from xformula.syntax.grammar.non_terminals.abc import NonTerminal

__all__ = [
    "NonTerminalClassBuilder",
]


class NonTerminalClassBuilder(ClassBuilder):
    @classmethod
    def get_name(
        cls,
        name: str,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        return name

    @classmethod
    def get_bases(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> tuple[type, ...]:
        return (NonTerminal,)

    @classmethod
    def get_namespace(
        cls,
        name: str,
        alternation: set[str],
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:

        branches = list(alternation)

        meta = type(
            "Meta",
            (),
            dict(
                atomic=False,
                is_polyfill=True,
                definition_name=name,
            ),
        )

        def build_grammar(self: NonTerminal) -> str:
            nonlocal branches

            suite = self.ebnf.suite
            define = self.ebnf.define
            orelse = self.ebnf.orelse

            return suite(
                *chain(
                    [
                        define(branches[0]),
                    ],
                    [orelse(branch) for branch in branches[1:]],
                ),
            )

        namespace = dict(
            Meta=meta,
            build_grammar=build_grammar,
        )

        return namespace
