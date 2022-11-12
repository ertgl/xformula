from typing import Generic, TypeVar

from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasOwner",
]


T = TypeVar("T")


class HasOwner(
    Generic[T],
    Node,
):

    owner: T

    class Meta(Node.Meta):

        abstract = True

        has_owner_attribute = True
