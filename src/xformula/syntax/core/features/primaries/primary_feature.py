from xformula.syntax.core.features.abc import Feature

__all__ = [
    "PrimaryFeature",
]


class PrimaryFeature(Feature):
    class Meta:
        fqn = "xformula.core.Primary"

    def setup(self) -> None:
        from xformula.syntax.core.features.primaries.definitions.non_terminals import (
            Primary,
        )

        self.non_terminal_types.append(Primary)
