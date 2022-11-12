import dataclasses

from xformula.syntax.ast.nodes.abc import Attribute as _Attribute
from xformula.syntax.ast.nodes.abc import Context, Identifier, Node

__all__ = [
    "Attribute",
]


@dataclasses.dataclass()
class Attribute(_Attribute):

    owner: Node = dataclasses.field(
        kw_only=True,
        default_factory=Node,
    )

    name: Identifier = dataclasses.field(
        kw_only=True,
        default_factory=Identifier,
    )

    context: Context = dataclasses.field(
        kw_only=True,
        default=Context.UNDEFINED,
    )
