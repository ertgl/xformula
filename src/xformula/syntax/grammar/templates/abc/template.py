from abc import ABC
from typing import Generic, TypeVar

from xformula.syntax.grammar.definitions.abc import Definition, DefinitionType

__all__ = [
    "Template",
]


T = TypeVar("T")


class Template(
    Definition,
    ABC,
    Generic[T],
):
    class Meta(Definition.Meta):

        abstract = True

        type = DefinitionType.TEMPLATE

    @staticmethod
    def arg(name: str) -> str:
        from xformula.syntax.grammar.ebnf import arg

        return arg(name)
