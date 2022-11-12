from xformula.syntax.core.features.abc import Feature

__all__ = [
    "ExpressionFeature",
]


class ExpressionFeature(Feature):
    class Meta:
        fqn = "xformula.core.Expression"

    def setup(self) -> None:
        from xformula.syntax.core.features.expressions.definitions.non_terminals import (
            ParenthesizedSimpleExpression,
            SimpleExpression,
        )

        self.non_terminal_types.extend(
            [
                SimpleExpression,
                ParenthesizedSimpleExpression,
            ],
        )
