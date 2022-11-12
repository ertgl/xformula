from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "BOOL",
]


class BOOL(
    Terminal[bool],
):
    class Meta:

        priority = 2000

        tags = {
            non_terminal("Bool"): 1000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        any_of = self.regex.any_of
        bound = self.regex.bound
        word = self.regex.word

        return define(
            regex(
                any_of(
                    bound(word("false")),
                    bound(word("true")),
                ),
            ),
        )

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> bool:
        return token.value.lower() == "true"
