from xformula.syntax.ast.nodes.abc.has_arguments import HasArguments
from xformula.syntax.ast.nodes.abc.has_callee import HasCallee
from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.term import Term

__all__ = [
    "Call",
]


class Call(
    Term,
    HasCallee[Node],
    HasArguments[list[Node]],
    Node,
):
    class Meta(
        Term.Meta,
        HasCallee.Meta,
        HasArguments.Meta,
        Node.Meta,
    ):

        abstract = True

        is_call = True
