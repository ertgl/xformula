from xformula.syntax.core.features.abc import Feature

__all__ = [
    "IdentifierFeature",
]


class IdentifierFeature(Feature):
    class Meta:
        fqn = "xformula.core.Identifier"

    def setup(self) -> None:
        from xformula.syntax.core.features.identifiers.definitions.non_terminals import (
            Identifier,
        )
        from xformula.syntax.core.features.identifiers.definitions.terminals import (
            IDENTIFIER,
        )

        self.non_terminal_types.append(Identifier)
        self.terminal_types.append(IDENTIFIER)
