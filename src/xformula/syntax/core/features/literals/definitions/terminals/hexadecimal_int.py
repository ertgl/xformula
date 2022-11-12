from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "HEXADECIMAL_INT",
]


class HEXADECIMAL_INT(  # NOSONAR
    Terminal[int],
):
    class Meta:

        tags = {
            non_terminal("Int"): -3000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        any_char_of = self.regex.any_char_of
        chars_between = self.regex.chars_between
        flat_one_or_more_of = self.regex.flat_one_or_more_of
        flat_optional = self.regex.flat_optional
        non_capturing_group = self.regex.non_capturing_group

        return define(
            regex(
                "0",
                any_char_of("x", "X"),
                flat_one_or_more_of(
                    non_capturing_group(
                        flat_optional("_"),
                        any_char_of(
                            chars_between("0", "9"),
                            chars_between("a", "f"),
                            chars_between("A", "F"),
                        ),
                    ),
                ),
            ),
        )

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> int:
        return int(token.value, base=16)
