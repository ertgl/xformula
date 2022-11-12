from xformula.syntax.core.features.abc import Feature

__all__ = [
    "SeparatorFeature",
]


class SeparatorFeature(Feature):
    class Meta:
        fqn = "xformula.core.Separator"

    def setup(self) -> None:
        from xformula.syntax.core.features.separators.definitions.templates import (
            SeparatedOneOrMoreOf,
            SeparatedPair,
            SeparatedZeroOrMoreOf,
        )

        self.template_types.extend(
            [
                SeparatedPair,
                SeparatedZeroOrMoreOf,
                SeparatedOneOrMoreOf,
            ],
        )
