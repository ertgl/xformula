from typing import TypeVar

from xformula.syntax.ast.nodes.abc.has_value import HasValue
from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.term import Term

__all__ = [
    "Literal",
]


T = TypeVar("T")


class Literal(
    Term,
    HasValue[T],
    Node,
):
    class Meta(
        Term.Meta,
        HasValue.Meta,
        Node.Meta,
    ):

        abstract = True

        is_literal = True
