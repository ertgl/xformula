from typing import Generic, TypeVar

from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasArguments",
]


T = TypeVar("T")


class HasArguments(
    Generic[T],
    Node,
):

    arguments: T

    class Meta(Node.Meta):

        abstract = True

        has_arguments_attribute = True
