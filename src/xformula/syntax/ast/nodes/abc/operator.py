from xformula.syntax.ast.nodes.abc.has_arity import HasArity
from xformula.syntax.ast.nodes.abc.has_associativity import HasAssociativity
from xformula.syntax.ast.nodes.abc.has_placement import HasPlacement
from xformula.syntax.ast.nodes.abc.has_precedence_level import HasPrecedenceLevel
from xformula.syntax.ast.nodes.abc.has_symbols import HasSymbols
from xformula.syntax.ast.nodes.abc.node import Node

__all__ = [
    "Operator",
]


class Operator(
    HasArity,
    HasAssociativity,
    HasPlacement,
    HasPrecedenceLevel,
    HasSymbols,
    Node,
):
    class Meta(
        HasArity.Meta,
        HasAssociativity.Meta,
        HasPlacement.Meta,
        HasPrecedenceLevel.Meta,
        HasSymbols.Meta,
        Node.Meta,
    ):

        abstract = True

        is_operator = True
