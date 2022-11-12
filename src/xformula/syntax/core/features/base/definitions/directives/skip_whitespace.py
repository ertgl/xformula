from xformula.syntax.grammar.directives.abc import Directive

__all__ = [
    "SkipWhitespace",
]


class SkipWhitespace(Directive):
    def build_grammar(self) -> str:
        use_directive = self.ebnf.use_directive
        terminal = self.ebnf.terminal

        return use_directive("ignore", terminal("WHITESPACE"))
