from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "Expression",
]


class Expression(Node):
    class Meta(Node.Meta):

        abstract = True

        is_expression = True
