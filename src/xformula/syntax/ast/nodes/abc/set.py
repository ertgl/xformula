from typing import TypeVar

from xformula.syntax.ast.nodes.abc.container import Container
from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "Set",
]


T = TypeVar("T")


class Set(
    Container[T],
    Node,
):
    class Meta(
        Container.Meta,
        Node.Meta,
    ):

        abstract = True

        is_set = True
