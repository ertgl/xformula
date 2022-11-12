from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "SINGLE_LINE_STR",
]


class SINGLE_LINE_STR(  # NOSONAR
    Terminal[str],
):
    class Meta:

        tags = {
            non_terminal("Str"): 1000,
        }

    def build_single_line_quoted_str_regex_pattern(
        self,
        quote: str,
    ) -> str:
        any_char = self.regex.any_char
        any_char_except = self.regex.any_char_except
        any_char_of = self.regex.any_char_of
        any_of = self.regex.any_of
        escape_char = self.regex.escape_char
        flat_zero_or_more_of = self.regex.flat_zero_or_more_of
        non_capturing_group = self.regex.non_capturing_group
        wrap = self.regex.wrap

        return wrap(
            escape_char(quote),
            flat_zero_or_more_of(
                non_capturing_group(
                    any_of(
                        any_char_of(
                            escape_char(r"\\"),
                            any_char(),
                        ),
                        any_char_except(
                            escape_char(quote),
                            r"\n",
                            escape_char(r"\\"),
                        ),
                    ),
                ),
            ),
        )

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        any_of = self.regex.any_of

        re_single_line_single_quoted = self.build_single_line_quoted_str_regex_pattern(
            "'"
        )
        re_single_line_double_quoted = self.build_single_line_quoted_str_regex_pattern(
            '"'
        )

        return define(
            regex(
                any_of(
                    re_single_line_single_quoted,
                    re_single_line_double_quoted,
                ),
            ),
        )

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> str:
        return bytes(token.value[1:-1], "UTF-8").decode("unicode_escape")
