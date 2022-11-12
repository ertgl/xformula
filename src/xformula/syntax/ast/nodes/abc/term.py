from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.primary import Primary

__all__ = [
    "Term",
]


class Term(
    Primary,
    Node,
):
    class Meta(
        Primary.Meta,
        Node.Meta,
    ):

        abstract = True

        is_term = True
