from typing import TYPE_CHECKING

from xformula.arch.meta import Configurable
from xformula.syntax.core.features.abc.feature_meta import FeatureMeta

if TYPE_CHECKING:
    from xformula.syntax.core.context.abc.syntax_context import SyntaxContext
    from xformula.syntax.grammar.directives.abc.directive import Directive
    from xformula.syntax.grammar.non_terminals.abc.non_terminal import NonTerminal
    from xformula.syntax.grammar.templates.abc.template import Template
    from xformula.syntax.grammar.terminals.abc.terminal import Terminal

__all__ = [
    "Feature",
]


class Feature(
    Configurable,
    metaclass=FeatureMeta,
):

    _context: "SyntaxContext"

    _directive_types: list[type["Directive"]]

    _non_terminal_types: list[type["NonTerminal"]]

    _template_types: list[type["Template"]]

    _terminal_types: list[type["Terminal"]]

    class Meta:
        abstract = True

    def __init__(
        self,
        context: "SyntaxContext",
    ) -> None:
        self._context = context
        self._directive_types = []
        self._non_terminal_types = []
        self._template_types = []
        self._terminal_types = []

    @property
    def context(self) -> "SyntaxContext":
        return self._context

    @property
    def directive_types(self) -> list[type["Directive"]]:
        return self._directive_types

    @property
    def non_terminal_types(self) -> list[type["NonTerminal"]]:
        return self._non_terminal_types

    @property
    def template_types(self) -> list[type["Template"]]:
        return self._template_types

    @property
    def terminal_types(self) -> list[type["Terminal"]]:
        return self._terminal_types

    def pre_setup(self) -> None:
        ...

    def setup(self) -> None:
        ...

    def post_setup(self) -> None:
        ...

    def on_ready(self) -> None:
        ...
