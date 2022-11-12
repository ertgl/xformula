from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "IDENTIFIER",
]


class IDENTIFIER(
    Terminal[str],
):
    class Meta:

        tags = {
            non_terminal("Identifier"): 2000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        return define(regex(r"(?<!\d)[^\W0-9]\w*"))

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> str:
        return token.value
