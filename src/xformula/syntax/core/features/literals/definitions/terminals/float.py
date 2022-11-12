from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "FLOAT",
]


class FLOAT(
    Terminal[float],
):
    class Meta:

        priority = 5000

        tags = {
            non_terminal("Float"): 1000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        any_char_of = self.regex.any_char_of
        any_of = self.regex.any_of
        chars_between = self.regex.chars_between
        escape_char = self.regex.escape_char
        flat = self.regex.flat
        flat_optional = self.regex.flat_optional
        flat_zero_or_more_of = self.regex.flat_zero_or_more_of
        non_capturing_group = self.regex.non_capturing_group

        re_number_dot_optional_scale = flat(
            any_char_of(chars_between("0", "9")),
            flat_zero_or_more_of(
                non_capturing_group(
                    flat_optional("_"),
                    any_char_of(chars_between("0", "9")),
                ),
            ),
            escape_char("."),
            flat_optional(
                non_capturing_group(
                    any_char_of(chars_between("0", "9")),
                    flat_zero_or_more_of(
                        non_capturing_group(
                            flat_optional("_"),
                            any_char_of(chars_between("0", "9")),
                        ),
                    ),
                ),
            ),
        )

        re_dot_number = flat(
            escape_char("."),
            any_char_of(chars_between("0", "9")),
            flat_zero_or_more_of(
                non_capturing_group(
                    flat_optional(r"_"),
                    any_char_of(chars_between("0", "9")),
                ),
            ),
        )

        re_exponent_part = flat(
            any_char_of("e", "E"),
            flat_optional(any_char_of("-", "+")),
            any_char_of(chars_between("0", "9")),
            flat_zero_or_more_of(
                non_capturing_group(
                    flat_optional("_"),
                    any_char_of(chars_between("0", "9")),
                ),
            ),
        )

        re_dot_float = flat(
            non_capturing_group(
                any_of(
                    re_number_dot_optional_scale,
                    re_dot_number,
                ),
            ),
            flat_optional(
                non_capturing_group(re_exponent_part),
            ),
        )

        re_number_float = flat(
            any_char_of(chars_between("0", "9")),
            flat_zero_or_more_of(
                non_capturing_group(
                    flat_optional("_"),
                    any_char_of(chars_between("0", "9")),
                ),
            ),
            re_exponent_part,
        )

        return define(regex(any_of(re_dot_float, re_number_float)))

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> float:
        return float(token.value)
