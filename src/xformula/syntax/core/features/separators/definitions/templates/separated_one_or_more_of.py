from typing import TypeVar

from xformula.syntax.grammar.templates.abc import Template

__all__ = [
    "SeparatedOneOrMoreOf",
]


T = TypeVar("T")


class SeparatedOneOrMoreOf(
    Template[list[T]],
):
    class Meta:

        arguments = [
            Template.arg("sep"),
            Template.arg("rule"),
        ]

    def build_grammar(self) -> str:
        suite = self.ebnf.suite
        define = self.ebnf.define
        orelse = self.ebnf.orelse
        use_template = self.ebnf.use_template
        arg = self.ebnf.arg

        return suite(
            define(
                use_template("SeparatedOneOrMoreOf", arg("sep"), arg("rule")),
                arg("sep"),
                arg("rule"),
            ),
            orelse(arg("rule"), arg("sep"), arg("rule")),
        )
