from xformula.syntax.grammar.templates.abc import Template

__all__ = [
    "WrapZeroOrMoreOf",
]


class WrapZeroOrMoreOf(Template):
    class Meta:

        arguments = [
            Template.arg("left"),
            Template.arg("right"),
            Template.arg("rule"),
        ]

    def build_grammar(self) -> str:
        suite = self.ebnf.suite
        define = self.ebnf.define
        orelse = self.ebnf.orelse
        arg = self.ebnf.arg
        use_template = self.ebnf.use_template

        return suite(
            define(
                use_template(
                    "WrapOneOrMoreOf",
                    arg("left"),
                    arg("right"),
                    arg("rule"),
                ),
            ),
            orelse(arg("left"), arg("right")),
        )
