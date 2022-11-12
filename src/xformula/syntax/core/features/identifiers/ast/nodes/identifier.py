import dataclasses

from xformula.syntax.ast.nodes.abc import Context
from xformula.syntax.ast.nodes.abc import Identifier as _Identifier

__all__ = [
    "Identifier",
]


@dataclasses.dataclass()
class Identifier(_Identifier):

    name: str = dataclasses.field(
        kw_only=True,
        default=str(),
    )

    context: Context = dataclasses.field(
        kw_only=True,
        default=Context.UNDEFINED,
    )
