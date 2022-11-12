from abc import ABC
from typing import Generic, TypeVar

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.definitions.abc import Definition, DefinitionType
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "NonTerminal",
]


T = TypeVar("T")


class NonTerminal(
    Definition,
    ABC,
    Generic[T],
):
    class Meta(Definition.Meta):

        abstract = True

        type = DefinitionType.NON_TERMINAL

        transform = "transform_parse_tree"

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree,
    ) -> T:
        raise NotImplementedError(
            f"{self.__class__.__qualname__}.transform_parse_tree is not implemented",
        )
