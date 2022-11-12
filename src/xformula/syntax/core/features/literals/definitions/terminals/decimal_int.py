from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "DECIMAL_INT",
]


class DECIMAL_INT(  # NOSONAR
    Terminal[int],
):
    class Meta:

        tags = {
            non_terminal("Int"): -4000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        any_char_of = self.regex.any_char_of
        any_of = self.regex.any_of
        chars_between = self.regex.chars_between
        flat = self.regex.flat
        flat_optional = self.regex.flat_optional
        flat_zero_or_more_of = self.regex.flat_zero_or_more_of
        non_capturing_group = self.regex.non_capturing_group

        re_zero = flat(
            r"0",
            flat_zero_or_more_of(
                non_capturing_group(
                    flat_optional(r"_"),
                    "0",
                ),
            ),
        )

        re_non_zero = flat(
            any_char_of(chars_between(r"1", r"9")),
            flat_zero_or_more_of(
                non_capturing_group(
                    flat_optional(r"_"),
                    any_char_of(chars_between(r"0", r"9")),
                ),
            ),
        )

        return define(regex(any_of(re_zero, re_non_zero)))

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> int:
        return int(token.value, base=10)
