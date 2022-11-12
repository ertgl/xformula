from xformula.syntax.ast.nodes.abc.context import Context
from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "HasContext",
]


class HasContext(Node):

    context: Context

    class Meta(Node.Meta):

        abstract = True

        has_context_attribute = True
