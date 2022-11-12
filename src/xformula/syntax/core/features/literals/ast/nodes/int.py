import dataclasses

from xformula.syntax.ast.nodes import Literal

__all__ = [
    "Int",
]


@dataclasses.dataclass()
class Int(
    Literal[int],
):

    value: int = dataclasses.field(
        kw_only=True,
        default=int(),
    )
