from typing import Generic, TypeVar

from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasCallee",
]


T = TypeVar("T")


class HasCallee(
    Generic[T],
    Node,
):

    callee: T

    class Meta(Node.Meta):

        abstract = True

        has_callee_attribute = True
