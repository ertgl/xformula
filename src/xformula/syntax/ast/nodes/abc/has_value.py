from typing import Generic, TypeVar

from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasValue",
]


T = TypeVar("T")


class HasValue(
    Generic[T],
    Node,
):

    value: T

    class Meta(Node.Meta):

        abstract = True

        has_value_attribute = True
