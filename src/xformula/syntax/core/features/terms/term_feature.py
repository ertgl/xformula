from xformula.syntax.core.features.abc import Feature

__all__ = [
    "TermFeature",
]


class TermFeature(Feature):
    class Meta:
        fqn = "xformula.core.Term"

    def setup(self) -> None:
        from xformula.syntax.core.features.terms.definitions.non_terminals import Term

        self.non_terminal_types.append(Term)
