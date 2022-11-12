from typing import Generic, Sequence, TypeVar

from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasElements",
]


S = TypeVar("S", bound=Sequence)


class HasElements(
    Generic[S],
    Node,
):

    elements: S

    class Meta(Node.Meta):

        abstract = True

        has_elements_attribute = True
