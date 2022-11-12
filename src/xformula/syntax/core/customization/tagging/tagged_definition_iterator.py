from typing import TYPE_CHECKING, Iterable

from xformula.syntax.core.context.abc import SyntaxContext

if TYPE_CHECKING:
    from xformula.syntax.grammar.definitions.abc.definition import Definition

__all__ = [
    "TaggedDefinitionIterator",
]


class TaggedDefinitionIterator:

    syntax_context: SyntaxContext

    tag: str

    @classmethod
    def iterate(
        cls,
        syntax_context: SyntaxContext,
        tag: str,
    ) -> Iterable["Definition"]:
        iterator = cls(syntax_context, tag)
        return iterator.find_tagged_definitions()

    def __init__(
        self,
        syntax_context: SyntaxContext,
        tag: str,
    ) -> None:
        self.syntax_context = syntax_context
        self.tag = tag

    def find_tagged_definitions(self) -> Iterable["Definition"]:
        alternation = self.syntax_context.tagged_definitions.get(self.tag, [])
        yield from alternation
