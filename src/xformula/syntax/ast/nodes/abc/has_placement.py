from xformula.syntax.ast.nodes.abc.node import Node
from xformula.syntax.ast.nodes.abc.placement import Placement

__all__ = [
    "HasPlacement",
]


class HasPlacement(Node):

    placement: Placement

    class Meta(Node.Meta):

        abstract = True

        has_placement_attribute = True
