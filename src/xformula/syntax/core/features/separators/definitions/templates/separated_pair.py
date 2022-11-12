from typing import TypeVar

from xformula.syntax.grammar.templates.abc import Template

__all__ = [
    "SeparatedPair",
]


T = TypeVar("T")


class SeparatedPair(
    Template[list[T]],
):
    class Meta:

        arguments = [
            Template.arg("sep"),
            Template.arg("lhs"),
            Template.arg("rhs"),
        ]

    def build_grammar(self) -> str:
        define = self.ebnf.define
        arg = self.ebnf.arg

        return define(arg("lhs"), arg("sep"), arg("rhs"))
