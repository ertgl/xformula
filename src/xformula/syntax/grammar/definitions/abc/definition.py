from typing import Any, Callable

from xformula.arch.meta import Configurable
from xformula.syntax.core.context import SyntaxContext
from xformula.syntax.grammar.definitions.abc.definition_meta import DefinitionMeta
from xformula.syntax.grammar.definitions.abc.definition_type import DefinitionType
from xformula.syntax.grammar.definitions.abc.ebnf_expression_builder_protocol import (
    EBNFExpressionBuilderProtocol,
)
from xformula.syntax.grammar.definitions.abc.regex_expression_builder_protocol import (
    RegexExpressionBuilderProtocol,
)

__all__ = [
    "Definition",
]


class Definition(
    Configurable,
    metaclass=DefinitionMeta,
):

    context: SyntaxContext

    ebnf: EBNFExpressionBuilderProtocol

    regex: RegexExpressionBuilderProtocol

    class Meta(Configurable.Meta):

        abstract: bool = True

        definition_name: str = ""

        atomic: bool = False

        retain_anonymous_literals: bool = False

        type: DefinitionType = DefinitionType.UNDEFINED

        arguments: list[str] = []

        priority: int = 0

        tags: dict[str, int | float] = dict()

        transform: str | Callable[..., Any] = "transform"

    def __init__(
        self,
        context: SyntaxContext,
    ) -> None:
        self.context = context
        self.ebnf = self.context.ebnf_expression_builder_class(self)
        self.regex = self.context.regex_expression_builder_class(self)

    def build_grammar(self) -> str:
        raise NotImplementedError(
            f"{self.__class__.__qualname__}.build_grammar is not implemented"
        )
