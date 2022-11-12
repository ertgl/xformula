from xformula.syntax.grammar.templates.abc import Template

__all__ = [
    "WrapOneOrMoreOf",
]


class WrapOneOrMoreOf(Template):
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
        optional = self.ebnf.optional
        op = self.ebnf.op

        return suite(
            define(
                arg("left"),
                use_template("SeparatedOneOrMoreOf", op(","), arg("rule")),
                optional(op(",")),
                arg("right"),
            ),
            orelse(arg("left"), arg("rule"), optional(op(",")), arg("right")),
        )
