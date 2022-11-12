from xformula.syntax.ast.nodes.abc.has_context import HasContext
from xformula.syntax.ast.nodes.abc.has_name import HasName
from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.term import Term

__all__ = [
    "Identifier",
]


class Identifier(
    Term,
    HasName[str],
    HasContext,
    Node,
):
    class Meta(
        Term.Meta,
        HasName.Meta,
        HasContext.Meta,
        Node.Meta,
    ):

        abstract = True

        is_identifier = True
