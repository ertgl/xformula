from xformula.syntax.ast.nodes.abc.associativity import Associativity
from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasAssociativity",
]


class HasAssociativity(Node):

    associativity: Associativity

    class Meta(Node.Meta):

        abstract = True

        has_associativity_attribute = True
