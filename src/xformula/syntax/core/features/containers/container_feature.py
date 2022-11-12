from xformula.syntax.core.features.abc import Feature

__all__ = [
    "ContainerFeature",
]


class ContainerFeature(Feature):
    class Meta:
        fqn = "xformula.core.Container"

    def setup(self) -> None:
        from xformula.syntax.core.features.containers.definitions.non_terminals import (
            List,
            Set,
            Tuple,
        )

        self.non_terminal_types.extend(
            [
                List,
                Tuple,
                Set,
            ],
        )
