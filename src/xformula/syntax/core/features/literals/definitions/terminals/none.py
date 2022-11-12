from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "NONE",
]


class NONE(
    Terminal[None],
):
    class Meta:

        priority = 2000

        tags = {
            non_terminal("None"): 0,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        bound = self.regex.bound
        word = self.regex.word

        return define(regex(bound(word("none"))))

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> None:
        return None
