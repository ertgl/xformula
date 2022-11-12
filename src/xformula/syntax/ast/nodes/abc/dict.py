from typing import TypeVar

from xformula.syntax.ast.nodes.abc.mapping import Mapping
from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "Dict",
]


K = TypeVar("K")

V = TypeVar("V")


class Dict(
    Mapping[K, V],
    Node,
):
    class Meta(
        Mapping.Meta,
        Node.Meta,
    ):

        abstract = True

        is_dict = True
