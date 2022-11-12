from typing import TypeVar

from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.simple_expression import SimpleExpression

__all__ = [
    "Operand",
]


N = TypeVar("N", bound=Node)


class Operand(
    SimpleExpression,
    Node,
):
    class Meta(
        SimpleExpression.Meta,
        Node.Meta,
    ):

        abstract = True

        is_operand = True
