from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "WHITESPACE",
]


class WHITESPACE(
    Terminal[str],
):
    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        one_or_more_of = self.regex.one_or_more_of
        whitespace = self.regex.whitespace

        return define(
            regex(
                one_or_more_of(
                    whitespace(),
                ),
            ),
        )

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> str:
        return token.value
