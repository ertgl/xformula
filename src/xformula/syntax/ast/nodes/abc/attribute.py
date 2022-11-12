from xformula.syntax.ast.nodes.abc.has_context import HasContext
from xformula.syntax.ast.nodes.abc.has_name import HasName
from xformula.syntax.ast.nodes.abc.has_owner import HasOwner
from xformula.syntax.ast.nodes.abc.identifier import Identifier
from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.term import Term

__all__ = [
    "Attribute",
]


class Attribute(
    Term,
    HasOwner[Node],
    HasName[Identifier],
    HasContext,
    Node,
):
    class Meta(
        Term.Meta,
        HasOwner.Meta,
        HasName.Meta,
        HasContext.Meta,
        Node.Meta,
    ):

        abstract = True

        is_attribute = True
