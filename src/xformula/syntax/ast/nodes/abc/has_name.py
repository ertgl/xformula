from typing import Generic, TypeVar

from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasName",
]


T = TypeVar("T")


class HasName(
    Generic[T],
    Node,
):

    name: T

    class Meta(Node.Meta):

        abstract = True

        has_name_attribute = True
