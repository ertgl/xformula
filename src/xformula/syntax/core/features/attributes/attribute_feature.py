from xformula.syntax.core.features.abc import Feature

__all__ = [
    "AttributeFeature",
]


class AttributeFeature(Feature):
    class Meta:
        fqn = "xformula.core.Attribute"

    def setup(self) -> None:
        from xformula.syntax.core.features.attributes.definitions.non_terminals import (
            Attribute,
        )

        self.non_terminal_types.append(Attribute)
