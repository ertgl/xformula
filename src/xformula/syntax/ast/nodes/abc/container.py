from typing import TypeVar

from xformula.syntax.ast.nodes.abc.has_elements import HasElements
from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.term import Term

__all__ = [
    "Container",
]


T = TypeVar("T")


class Container(
    Term,
    HasElements[list[T]],
    Node,
):
    class Meta(
        Term.Meta,
        HasElements.Meta,
        Node.Meta,
    ):

        abstract = True

        is_container = True
