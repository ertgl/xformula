from xformula.syntax.ast.nodes.abc.has_operands import HasOperands
from xformula.syntax.ast.nodes.abc.has_operator import HasOperator
from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.simple_expression import SimpleExpression

__all__ = [
    "Operation",
]


class Operation(
    SimpleExpression,
    HasOperator,
    HasOperands,
    Node,
):
    class Meta(
        SimpleExpression.Meta,
        HasOperator.Meta,
        HasOperands.Meta,
        Node.Meta,
    ):

        abstract = True

        is_operation = True
