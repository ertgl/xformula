from xformula.syntax.core.features.abc import Feature

__all__ = [
    "WrapperFeature",
]


class WrapperFeature(Feature):
    class Meta:
        fqn = "xformula.core.Wrapper"

    def setup(self) -> None:
        from xformula.syntax.core.features.wrappers.definitions.templates import (
            WrapOneOrMoreOf,
            WrapZeroOrMoreOf,
        )

        self.template_types.extend(
            [
                WrapZeroOrMoreOf,
                WrapOneOrMoreOf,
            ],
        )
