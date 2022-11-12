from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.operand import Operand

__all__ = [
    "HasOperands",
]


class HasOperands(Node):

    operands: list[Operand]

    class Meta(Node.Meta):

        abstract = True

        has_operands_attribute = True
