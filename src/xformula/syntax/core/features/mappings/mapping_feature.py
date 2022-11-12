from xformula.syntax.core.features.abc import Feature

__all__ = [
    "MappingFeature",
]


class MappingFeature(Feature):
    class Meta:
        fqn = "xformula.core.Mapping"

    def setup(self) -> None:
        from xformula.syntax.core.features.mappings.definitions.non_terminals import (
            Dict,
            DictPair,
        )

        self.non_terminal_types.extend(
            [
                DictPair,
                Dict,
            ],
        )
