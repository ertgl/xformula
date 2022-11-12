import dataclasses

from xformula.syntax.ast.nodes import Literal

__all__ = [
    "Bool",
]


@dataclasses.dataclass()
class Bool(
    Literal[bool],
):

    value: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )
