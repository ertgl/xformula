from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.operator import Operator

__all__ = [
    "HasOperator",
]


class HasOperator(Node):

    operator: Operator

    class Meta(Node.Meta):

        abstract = True

        has_operator_attribute = True
