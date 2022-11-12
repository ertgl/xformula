from typing import TypeVar

from xformula.syntax.ast.nodes.abc.container import Container
from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.pair import Pair

__all__ = [
    "Mapping",
]


K = TypeVar("K")

V = TypeVar("V")


class Mapping(
    Container[Pair[K, V]],
    Node,
):
    class Meta(
        Container.Meta,
        Node.Meta,
    ):

        abstract = True

        is_mapping = True
