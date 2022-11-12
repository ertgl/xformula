from xformula.arch.meta import Meta
from xformula.syntax.ast.nodes.abc.node_options import NodeOptions

__all__ = [
    "NodeMeta",
]


class NodeMeta(
    Meta[NodeOptions],
):

    options_class = NodeOptions

    options: NodeOptions
