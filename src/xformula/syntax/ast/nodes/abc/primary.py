from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.operand import Operand

__all__ = [
    "Primary",
]


class Primary(
    Operand,
    Node,
):
    class Meta(
        Operand.Meta,
        Node.Meta,
    ):

        abstract = True

        is_primary = True
