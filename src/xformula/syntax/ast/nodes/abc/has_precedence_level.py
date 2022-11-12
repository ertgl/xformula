from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.precedence_level import PrecedenceLevel

__all__ = [
    "HasPrecedenceLevel",
]


class HasPrecedenceLevel(Node):

    precedence_level: PrecedenceLevel

    class Meta(Node.Meta):

        abstract = True

        has_precedence_level_attribute = True
