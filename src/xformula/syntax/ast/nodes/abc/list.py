from typing import TypeVar

from xformula.syntax.ast.nodes.abc.container import Container
from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "List",
]


T = TypeVar("T")


class List(
    Container[T],
    Node,
):
    class Meta(
        Container.Meta,
        Node.Meta,
    ):

        abstract = True

        is_list = True
