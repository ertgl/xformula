from contextlib import suppress
from typing import TYPE_CHECKING, Iterable, Protocol, Union, runtime_checkable

if TYPE_CHECKING:
    from xformula.syntax.core.context.abc.syntax_context import SyntaxContext
    from xformula.syntax.core.symbols.abc.symbol_type import SymbolType
    from xformula.syntax.grammar.definitions.abc.definition import Definition
    from xformula.syntax.grammar.definitions.abc.definition_type import DefinitionType

__all__ = [
    "EBNFExpressionBuilderProtocol",
]


@runtime_checkable
class EBNFExpressionBuilderProtocol(Protocol):

    _definition: "Definition"

    def __init__(
        self,
        definition: "Definition",
    ) -> None:
        self._definition = definition

    def any_of(
        self,
        *expressions: str,
    ) -> str:
        ...

    def arg(
        self,
        name: str,
    ) -> str:
        ...

    def concat(
        self,
        expressions: Iterable[str],
    ) -> str:
        ...

    def define(
        self,
        *expressions: str,
    ) -> str:
        ...

    def define_rule(
        self,
        definition: "Definition",
    ) -> str:
        ...

    def directive(
        self,
        name: str,
    ) -> str:
        ...

    def document(
        self,
        syntax_context: "SyntaxContext",
    ) -> str:
        ...

    def flat_join(
        self,
        separator: str,
        expressions: Iterable[str],
    ) -> str:
        ...

    def get_normalized_name_by_definition(
        self,
        definition: Union[
            "Definition",
            type["Definition"],
        ],
    ) -> str:
        ...

    def group(
        self,
        *expressions: str,
    ) -> str:
        ...

    def indent(
        self,
        *block: str,
        width: int = 4,
    ) -> str:
        ...

    def keyword(
        self,
        name: str,
    ) -> str:
        ...

    def literal(
        self,
        value: str,
    ) -> str:
        ...

    def non_terminal(
        self,
        name: str,
    ) -> str:
        ...

    def normalize_name_by_type(
        self,
        name: str,
        definition_type: "DefinitionType",
    ) -> str:
        ...

    def one_or_more_of(
        self,
        *expressions: str,
    ) -> str:
        ...

    def op(
        self,
        symbol: str,
    ) -> str:
        ...

    def optional(
        self,
        *expressions: str,
    ) -> str:
        ...

    def orelse(
        self,
        *expressions: str,
    ) -> str:
        ...

    def regex(
        self,
        *expressions: str,
    ) -> str:
        ...

    def suite(
        self,
        *lines: str,
    ) -> str:
        ...

    def sym(
        self,
        info: tuple["SymbolType", str],
    ) -> str:
        ...

    def define_tagged_alternation(self) -> str:
        from xformula.syntax.core.customization import TaggedDefinitionIterator

        alternation = TaggedDefinitionIterator.iterate(
            self._definition.context,
            self._definition.__class__.options.definition_name,
        )

        branch_iterator = iter(alternation)

        first_branch = ""
        with suppress(StopIteration):
            first_branch = next(branch_iterator).__class__.options.definition_name

        define = self.define
        orelse = self.orelse

        return self.suite(
            define(first_branch) if first_branch else "",
            *[
                orelse(branch.__class__.options.definition_name)
                for branch in branch_iterator
            ],
        )

    def tagged_alternation(self) -> str:
        from xformula.syntax.core.customization import TaggedDefinitionIterator

        alternation = TaggedDefinitionIterator.iterate(
            self._definition.context,
            self._definition.__class__.options.definition_name,
        )

        return self.any_of(
            *[branch.__class__.options.definition_name for branch in alternation],
        )

    def or_tagged_alternation(self) -> str:
        str_tagged_alternation = self.tagged_alternation()
        if not str_tagged_alternation:
            return ""

        return self.orelse(str_tagged_alternation)

    def template(
        self,
        name: str,
    ) -> str:
        ...

    def terminal(
        self,
        name: str,
    ) -> str:
        ...

    def use_directive(
        self,
        name: str,
        *expressions: str,
    ) -> str:
        ...

    def use_template(
        self,
        name: str,
        *arguments: str,
    ) -> str:
        ...
