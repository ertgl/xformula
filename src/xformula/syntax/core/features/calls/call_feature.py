from xformula.syntax.core.features.abc import Feature

__all__ = [
    "CallFeature",
]


class CallFeature(Feature):
    class Meta:
        fqn = "xformula.core.Call"

    def setup(self) -> None:
        from xformula.syntax.core.features.calls.definitions.non_terminals import (
            Call,
            CallArgument,
            CallKeywordArgument,
        )

        self.non_terminal_types.extend(
            [
                CallArgument,
                CallKeywordArgument,
                Call,
            ],
        )
