from xformula.syntax.core.features.abc import Feature

__all__ = [
    "LiteralFeature",
]


class LiteralFeature(Feature):
    class Meta:
        fqn = "xformula.core.Literal"

    def setup(self) -> None:
        from xformula.syntax.core.features.literals.definitions.non_terminals import (
            Bool,
            Complex,
            Float,
            Int,
            Literal,
            None_,
            Str,
        )
        from xformula.syntax.core.features.literals.definitions.terminals import (
            BINARY_INT,
            BOOL,
            COMPLEX,
            DECIMAL_INT,
            FLOAT,
            HEXADECIMAL_INT,
            NONE,
            OCTAL_INT,
            SINGLE_LINE_STR,
        )

        self.non_terminal_types.extend(
            [
                None_,
                Bool,
                Int,
                Float,
                Complex,
                Str,
                Literal,
            ],
        )

        self.terminal_types.extend(
            [
                NONE,
                BOOL,
                BINARY_INT,
                OCTAL_INT,
                DECIMAL_INT,
                HEXADECIMAL_INT,
                FLOAT,
                COMPLEX,
                SINGLE_LINE_STR,
            ],
        )
