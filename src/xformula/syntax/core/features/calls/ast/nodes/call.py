import dataclasses

from xformula.syntax.ast.nodes.abc import Call as _Call
from xformula.syntax.ast.nodes.abc import Node

__all__ = [
    "Call",
]


@dataclasses.dataclass()
class Call(_Call):

    callee: Node = dataclasses.field(
        kw_only=True,
        default_factory=Node,
    )

    arguments: list[Node] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )
