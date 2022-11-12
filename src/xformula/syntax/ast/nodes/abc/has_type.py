from typing import Generic, TypeVar

from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasType",
]


T = TypeVar("T")


class HasType(
    Generic[T],
    Node,
):

    type: T

    class Meta(Node.Meta):

        abstract = True

        has_type_attribute = True
