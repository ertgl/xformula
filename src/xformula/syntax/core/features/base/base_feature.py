from xformula.syntax.core.features.abc import Feature

__all__ = [
    "BaseFeature",
]


class BaseFeature(Feature):
    class Meta:
        fqn = "xformula.core.Base"

    def setup(self) -> None:
        from xformula.syntax.core.features.base.definitions.directives import (
            SkipWhitespace,
        )
        from xformula.syntax.core.features.base.definitions.terminals import WHITESPACE

        self.directive_types.append(SkipWhitespace)
        self.terminal_types.append(WHITESPACE)
