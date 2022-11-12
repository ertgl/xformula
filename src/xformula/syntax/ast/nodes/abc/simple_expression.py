from xformula.syntax.ast.nodes.abc.expression import Expression
from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "SimpleExpression",
]


class SimpleExpression(
    Expression,
    Node,
):
    class Meta(
        Expression.Meta,
        Node.Meta,
    ):

        abstract = True

        is_simple_expression = True
