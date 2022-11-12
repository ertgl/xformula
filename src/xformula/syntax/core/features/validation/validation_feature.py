from typing import NoReturn

from xformula.syntax.core.features.abc import Feature

__all__ = [
    "ValidationFeature",
]

from xformula.syntax.core.features.validation.errors import MissingDefinitionError


class ValidationFeature(Feature):
    class Meta:
        fqn = "xformula.core.Validation"

    def on_ready(self) -> None:
        self.validate()

    def validate(self) -> NoReturn | None:
        from xformula.syntax.core.features.validation.detectors import (
            MissingNonTerminalDetector,
        )

        missing_non_terminals = MissingNonTerminalDetector.detect(
            self.context,
        )

        if len(missing_non_terminals) > 0:
            raise MissingDefinitionError(
                {
                    "non-terminal": missing_non_terminals,
                },
            )

        return None
