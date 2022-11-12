from xformula.syntax.ast.nodes.abc.arity import Arity
from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasArity",
]


class HasArity(Node):

    arity: Arity

    class Meta(Node.Meta):

        abstract: bool = True

        has_arity_attribute: bool = True
