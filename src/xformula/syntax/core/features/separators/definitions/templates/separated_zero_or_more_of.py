from typing import TypeVar

from xformula.syntax.grammar.templates.abc import Template

__all__ = [
    "SeparatedZeroOrMoreOf",
]


T = TypeVar("T")


class SeparatedZeroOrMoreOf(
    Template[list[T]],
):
    class Meta:

        arguments = [
            Template.arg("sep"),
            Template.arg("rule"),
        ]

    def build_grammar(self) -> str:
        arg = self.ebnf.arg
        define = self.ebnf.define
        optional = self.ebnf.optional
        use_template = self.ebnf.use_template
        suite = self.ebnf.suite

        return suite(
            define(
                optional(
                    use_template("SeparatedZeroOrMoreOf", arg("sep"), arg("rule")),
                    arg("sep"),
                ),
                arg("rule"),
            ),
        )
